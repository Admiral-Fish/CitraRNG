import time
import threading

from Manager import Manager
from Util import hexify, colorIV, colorPSV, findButton, findComboBox, findLabel, findLineEdit, findSpinBox
from PySide2.QtWidgets import QMainWindow, QComboBox, QPushButton, QLineEdit, QLabel, QSpinBox
from PySide2.QtCore import QFile, QObject, Signal, Slot
from PySide2.QtUiTools import QUiLoader

class MainWindow(QMainWindow):
    update = Signal()

    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)
        self.loadUi()
        self.delay = 0.5
        
        findButton(self.ui, "pushButtonConnect").clicked.connect(self.connectCitra)
        findButton(self.ui, "pushButtonUpdatePokemon").clicked.connect(self.updatePokemon)
        findButton(self.ui, "pushButtonUpdateMainRNG").clicked.connect(self.updateMainRNG)
        findButton(self.ui, "pushButtonUpdateEggRNG").clicked.connect(self.updateEggRNG)
        findSpinBox(self.ui, "spinBoxDelay").valueChanged.connect(self.updateDelay)

        self.update.connect(self.updateMainRNG)

    def loadUi(self):
        file = QFile("MainWindow.ui")
        file.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.ui = loader.load(file)
        self.ui.show()
        file.close()

    def connectCitra(self):
        comboBox = findComboBox(self.ui, "comboBoxGameSelection")
        index = comboBox.currentIndex()
        self.manager = Manager(index)

        if self.manager.isConnected == True:
            self.toggleEnable(True)
            findLabel(self.ui, "labelStatus").setText("Connected")

            t = threading.Thread(target=self.autoUpdateMain)
            time.sleep(1)
            t.start()
            self.updateEggRNG()
        else:
            self.toggleEnable(False)
            findLabel(self.ui, "labelStatus").setText("Connection failed")

    def toggleEnable(self, flag):
        findComboBox(self.ui, "comboBoxPokemon").setEnabled(flag)
        findButton(self.ui, "pushButtonUpdatePokemon").setEnabled(flag)
        findButton(self.ui, "pushButtonUpdateMainRNG").setEnabled(flag)
        findButton(self.ui, "pushButtonUpdateEggRNG").setEnabled(flag)

    @Slot()
    def updateMainRNG(self):
        self.manager.updateFrameCount()

        seed = self.manager.initialSeed
        curr = self.manager.currentSeed
        frame = self.manager.frameCount
        tsv = self.manager.trainerShinyValue()

        findLineEdit(self.ui, "lineEditInitialSeed").setText(hexify(seed))
        findLineEdit(self.ui, "lineEditCurrentSeed").setText(hexify(curr))
        findLineEdit(self.ui, "lineEditFrame").setText(str(frame))
        findLineEdit(self.ui, "lineEditTSV").setText(str(tsv))

    def updateEggRNG(self):
        values = self.manager.eggStatus()

        eggStatus = findLabel(self.ui, "labelEggReadyStatus")
        if values[0] == 0:
            eggStatus.setText("No egg yet")
        else:
            eggStatus.setText("Egg ready")

        findLineEdit(self.ui, "lineEditEggSeed3").setText(hexify(values[1]))
        findLineEdit(self.ui, "lineEditEggSeed2").setText(hexify(values[2]))
        findLineEdit(self.ui, "lineEditEggSeed1").setText(hexify(values[3]))
        findLineEdit(self.ui, "lineEditEggSeed0").setText(hexify(values[4]))

    def updatePokemon(self):
        index = findComboBox(self.ui, "comboBoxPokemon").currentIndex()

        if index < 6:
            pkm = self.manager.partyPokemon(index)
        else:
            pkm = self.manager.wildPokemon()

        findLabel(self.ui, "labelSpeciesValue").setText(pkm.Species())
        findLabel(self.ui, "labelGenderValue").setText(pkm.Gender())
        findLabel(self.ui, "labelNatureValue").setText(pkm.Nature())
        findLabel(self.ui, "labelAbilityValue").setText(pkm.Ability())
        findLabel(self.ui, "labelItemValue").setText(pkm.HeldItem())
        findLabel(self.ui, "labelPSV").setText("PSV: " + colorPSV(pkm.PSV(), pkm.TSV()))
        findLabel(self.ui, "labelTSV").setText("TSV: " + str(pkm.TSV()))
        findLabel(self.ui, "labelHiddenPowerValue").setText(pkm.HiddenPower())
        findLabel(self.ui, "labelFriendshipValue").setText(str(pkm.CurrentFriendship()))
        
        findLabel(self.ui, "labelHPIV").setText("IV: " + colorIV(pkm.IVHP()))
        findLabel(self.ui, "labelAtkIV").setText("IV: " + colorIV(pkm.IVAtk()))
        findLabel(self.ui, "labelDefIV").setText("IV: " + colorIV(pkm.IVDef()))
        findLabel(self.ui, "labelSpAIV").setText("IV: " + colorIV(pkm.IVSpA()))
        findLabel(self.ui, "labelSpDIV").setText("IV: " + colorIV(pkm.IVSpD()))
        findLabel(self.ui, "labelSpeIV").setText("IV: " + colorIV(pkm.IVSpe()))
        findLabel(self.ui, "labelHPEV").setText("EV: " + str(pkm.EVHP()))
        findLabel(self.ui, "labelAtkEV").setText("EV: " + str(pkm.EVAtk()))
        findLabel(self.ui, "labelDefEV").setText("EV: " + str(pkm.EVDef()))
        findLabel(self.ui, "labelSpAEV").setText("EV: " + str(pkm.EVSpA()))
        findLabel(self.ui, "labelSpDEV").setText("EV: " + str(pkm.EVSpD()))
        findLabel(self.ui, "labelSpeEV").setText("EV: " + str(pkm.EVSpe()))
    
        findLabel(self.ui, "labelMove1Name").setText(pkm.Move1())
        findLabel(self.ui, "labelMove2Name").setText(pkm.Move2())
        findLabel(self.ui, "labelMove3Name").setText(pkm.Move3())
        findLabel(self.ui, "labelMove4Name").setText(pkm.Move4())
        findLabel(self.ui, "labelMove1PP").setText("PP: " + str(pkm.Move1PP()))
        findLabel(self.ui, "labelMove2PP").setText("PP: " + str(pkm.Move2PP()))
        findLabel(self.ui, "labelMove3PP").setText("PP: " + str(pkm.Move3PP()))
        findLabel(self.ui, "labelMove4PP").setText("PP: " + str(pkm.Move4PP()))

    def updateDelay(self):
        val = findSpinBox(self.ui, "spinBoxDelay").value()
        if val > 500:
            self.delay = float(val) / 1000.0

    def autoUpdateMain(self):
        while self.manager.connection.is_connected() == True:
            self.update.emit()
            time.sleep(self.delay)