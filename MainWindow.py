import time

from Manager import Manager
from PySide2.QtWidgets import QMainWindow, QComboBox, QPushButton, QLabel
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader
#from PySide2 import QtCore, QtGui, QtWidgets 

class MainWindow(QMainWindow):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)
        self.loadUi()
        
        buttonConnect = self.ui.findChild(QPushButton, "pushButtonConnect")
        buttonConnect.clicked.connect(self.connectCitra)

        buttonPokemon = self.ui.findChild(QPushButton, "pushButtonUpdatePokemon")
        buttonPokemon.clicked.connect(self.updatePokemon)

        buttonMain = self.ui.findChild(QPushButton, "pushButtonUpdateMainRNG")
        buttonMain.clicked.connect(self.updateMainRNG)

        buttonEgg = self.ui.findChild(QPushButton, "pushButtonUpdateEggRNG")
        buttonEgg.clicked.connect(self.updateEggRNG)

    def loadUi(self):
        file = QFile("MainWindow.ui")
        file.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.ui = loader.load(file)
        self.ui.show()
        file.close()

    def connectCitra(self):
        comboBox = self.ui.findChild(QComboBox, "comboBoxGameSelection")
        index = comboBox.currentIndex()
        self.manager = Manager(index)

        if self.manager.isConnected == True:
            self.toggleEnable(True)
            connectionStatus = self.ui.findChild(QLabel, "labelStatus")
            connectionStatus.setText("Connected")
        else:
            self.toggleEnable(False)
            connectionStatus = self.ui.findChild(QLabel, "labelStatus")
            connectionStatus.setText("Connection failed")

    def toggleEnable(self, flag):
        comboBoxPokemon = self.ui.findChild(QComboBox, "comboBoxPokemon")
        comboBoxPokemon.setEnabled(flag)

        pushButtonPokemon = self.ui.findChild(QPushButton, "pushButtonUpdatePokemon")
        pushButtonPokemon.setEnabled(flag)

        pushButtonMain = self.ui.findChild(QPushButton, "pushButtonUpdateMainRNG")
        pushButtonMain.setEnabled(flag)

        pushButtonEgg = self.ui.findChild(QPushButton, "pushButtonUpdateEggRNG")
        pushButtonEgg.setEnabled(flag)

    def updateMainRNG(self):
        self.manager.updateFrameCount()

        seed = self.manager.initialSeed
        curr = self.manager.currentSeed
        frame = self.manager.frameCount

        seedLabel = self.ui.findChild(QLabel, "labelInitialSeedValue")
        seedLabel.setText(str(hex(seed)))

        currLabel = self.ui.findChild(QLabel, "labelCurrentSeedValue")
        currLabel.setText(str(hex(curr)))

        frameLabel = self.ui.findChild(QLabel, "labelFrameValue")
        frameLabel.setText(str(frame))

    def updateEggRNG(self):
        values = self.manager.eggStatus()

        eggStatus = self.ui.findChild(QLabel, "labelEggReadyStatus")
        if values[0] == 0:
            eggStatus.setText("No egg yet")
        else:
            eggStatus.setText("Egg ready")

        seed3 = self.ui.findChild(QLabel, "labelEggSeed3Value")
        seed3.setText(str(hex(values[1])))

        seed2 = self.ui.findChild(QLabel, "labelEggSeed2Value")
        seed2.setText(str(hex(values[2])))

        seed1 = self.ui.findChild(QLabel, "labelEggSeed1Value")
        seed1.setText(str(hex(values[3])))

        seed0 = self.ui.findChild(QLabel, "labelEggSeed0Value")
        seed0.setText(str(hex(values[4])))

    def updatePokemon(self):
        comboBox = self.ui.findChild(QComboBox, "comboBoxPokemon")
        index = comboBox.currentIndex()

        if index < 6:
            pkm = self.manager.partyPokemon(index)
        else:
            pkm = self.manager.wildPokemon()

        self.ui.findChild(QLabel, "labelSpeciesValue").setText(pkm.Species())
        self.ui.findChild(QLabel, "labelGenderValue").setText(pkm.Gender())
        self.ui.findChild(QLabel, "labelNatureValue").setText(pkm.Nature())
        self.ui.findChild(QLabel, "labelAbilityValue").setText(pkm.Ability())
        self.ui.findChild(QLabel, "labelItemValue").setText(pkm.HeldItem())
        self.ui.findChild(QLabel, "labelPSVValue").setText(str(pkm.PSV()))
        self.ui.findChild(QLabel, "labelHiddenPowerValue").setText(pkm.HiddenPower())
        self.ui.findChild(QLabel, "labelFriendshipValue").setText(str(pkm.CurrentFriendship()))
        
        self.ui.findChild(QLabel, "labelHPValue").setText("IV: " + str(pkm.IVHP()) + "    EV: " + str(pkm.EVHP()))
        self.ui.findChild(QLabel, "labelAtkValue").setText("IV: " + str(pkm.IVAtk()) + "    EV: " + str(pkm.EVAtk()))
        self.ui.findChild(QLabel, "labelDefValue").setText("IV: " + str(pkm.IVDef()) + "    EV: " + str(pkm.EVDef()))
        self.ui.findChild(QLabel, "labelSpAValue").setText("IV: " + str(pkm.IVSpA()) + "    EV: " + str(pkm.EVSpA()))
        self.ui.findChild(QLabel, "labelSpDValue").setText("IV: " + str(pkm.IVSpD()) + "    EV: " + str(pkm.EVSpD()))
        self.ui.findChild(QLabel, "labelSpeValue").setText("IV: " + str(pkm.IVSpe()) + "    EV: " + str(pkm.EVSpe()))
    
        self.ui.findChild(QLabel, "labelMove1Value").setText("PP: " + str(pkm.Move1PP()) + ",    " + pkm.Move1())
        self.ui.findChild(QLabel, "labelMove2Value").setText("PP: " + str(pkm.Move2PP()) + ",    " + pkm.Move2())
        self.ui.findChild(QLabel, "labelMove3Value").setText("PP: " + str(pkm.Move3PP()) + ",    " + pkm.Move3())
        self.ui.findChild(QLabel, "labelMove4Value").setText("PP: " + str(pkm.Move4PP()) + ",    " + pkm.Move4())

        
