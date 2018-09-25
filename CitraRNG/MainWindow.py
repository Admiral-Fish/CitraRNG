from Manager import Manager
from Util import hexify
from PySide2.QtWidgets import QMainWindow, QComboBox, QPushButton, QLabel
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader

class MainWindow(QMainWindow):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)
        self.loadUi()
        
        buttonConnect = self.findButton("pushButtonConnect")
        buttonConnect.clicked.connect(self.connectCitra)

        buttonPokemon = self.findButton("pushButtonUpdatePokemon")
        buttonPokemon.clicked.connect(self.updatePokemon)

        buttonMain = self.findButton("pushButtonUpdateMainRNG")
        buttonMain.clicked.connect(self.updateMainRNG)

        buttonEgg = self.findButton("pushButtonUpdateEggRNG")
        buttonEgg.clicked.connect(self.updateEggRNG)

    def loadUi(self):
        file = QFile("MainWindow.ui")
        file.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.ui = loader.load(file)
        self.ui.show()
        file.close()

    def connectCitra(self):
        comboBox = self.findComboBox("comboBoxGameSelection")
        index = comboBox.currentIndex()
        self.manager = Manager(index)

        if self.manager.isConnected == True:
            self.toggleEnable(True)
            connectionStatus = self.findLabel("labelStatus")
            connectionStatus.setText("Connected")
        else:
            self.toggleEnable(False)
            connectionStatus = self.findLabel("labelStatus")
            connectionStatus.setText("Connection failed")

    def toggleEnable(self, flag):
        comboBoxPokemon = self.findComboBox("comboBoxPokemon")
        comboBoxPokemon.setEnabled(flag)

        pushButtonPokemon = self.findButton("pushButtonUpdatePokemon")
        pushButtonPokemon.setEnabled(flag)

        pushButtonMain = self.findButton("pushButtonUpdateMainRNG")
        pushButtonMain.setEnabled(flag)

        pushButtonEgg = self.findButton("pushButtonUpdateEggRNG")
        pushButtonEgg.setEnabled(flag)

    def updateMainRNG(self):
        self.manager.updateFrameCount()

        seed = self.manager.initialSeed
        curr = self.manager.currentSeed
        frame = self.manager.frameCount

        self.findLabel("labelInitialSeedValue").setText(hexify(seed))
        self.findLabel("labelCurrentSeedValue").setText(hexify(curr))
        self.findLabel("labelFrameValue").setText(str(frame))

    def updateEggRNG(self):
        values = self.manager.eggStatus()

        eggStatus = self.findLabel("labelEggReadyStatus")
        if values[0] == 0:
            eggStatus.setText("No egg yet")
        else:
            eggStatus.setText("Egg ready")

        self.findLabel("labelEggSeed3Value").setText(hexify(values[1]))
        self.findLabel("labelEggSeed2Value").setText(hexify(values[2]))
        self.findLabel("labelEggSeed1Value").setText(hexify(values[3]))
        self.findLabel("labelEggSeed0Value").setText(hexify(values[4]))

    def updatePokemon(self):
        index = self.findComboBox("comboBoxPokemon").currentIndex()

        if index < 6:
            pkm = self.manager.partyPokemon(index)
        else:
            pkm = self.manager.wildPokemon()

        self.findLabel("labelSpeciesValue").setText(pkm.Species())
        self.findLabel("labelGenderValue").setText(pkm.Gender())
        self.findLabel("labelNatureValue").setText(pkm.Nature())
        self.findLabel("labelAbilityValue").setText(pkm.Ability())
        self.findLabel("labelItemValue").setText(pkm.HeldItem())
        self.findLabel("labelPSVValue").setText(str(pkm.PSV()))
        self.findLabel("labelHiddenPowerValue").setText(pkm.HiddenPower())
        self.findLabel("labelFriendshipValue").setText(str(pkm.CurrentFriendship()))
        
        self.findLabel("labelHPValue").setText("IV: " + str(pkm.IVHP()) + "    EV: " + str(pkm.EVHP()))
        self.findLabel("labelAtkValue").setText("IV: " + str(pkm.IVAtk()) + "    EV: " + str(pkm.EVAtk()))
        self.findLabel("labelDefValue").setText("IV: " + str(pkm.IVDef()) + "    EV: " + str(pkm.EVDef()))
        self.findLabel("labelSpAValue").setText("IV: " + str(pkm.IVSpA()) + "    EV: " + str(pkm.EVSpA()))
        self.findLabel("labelSpDValue").setText("IV: " + str(pkm.IVSpD()) + "    EV: " + str(pkm.EVSpD()))
        self.findLabel("labelSpeValue").setText("IV: " + str(pkm.IVSpe()) + "    EV: " + str(pkm.EVSpe()))
    
        self.findLabel("labelMove1Value").setText("PP: " + str(pkm.Move1PP()) + ",    " + pkm.Move1())
        self.findLabel("labelMove2Value").setText("PP: " + str(pkm.Move2PP()) + ",    " + pkm.Move2())
        self.findLabel("labelMove3Value").setText("PP: " + str(pkm.Move3PP()) + ",    " + pkm.Move3())
        self.findLabel("labelMove4Value").setText("PP: " + str(pkm.Move4PP()) + ",    " + pkm.Move4())

    def findComboBox(self, name):
        return self.ui.findChild(QComboBox, name)

    def findButton(self, name):
        return self.ui.findChild(QPushButton, name)

    def findLabel(self, name):
        return self.ui.findChild(QLabel, name)
