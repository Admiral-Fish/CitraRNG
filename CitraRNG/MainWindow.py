import threading
import time

from PySide2.QtCore import QSettings, Signal, Slot
from PySide2.QtWidgets import QMainWindow, QMessageBox
from ui_MainWindow import Ui_MainWindow

from ManagerSM import ManagerSM
from ManagerUSUM import ManagerUSUM
from Util import hexify

class MainWindow(QMainWindow, Ui_MainWindow):
    update = Signal()

    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.loadSettings()

        self.mainPokemon.setTitle("Main Pokemon")
        self.eggParent1.setTitle("Parent 1")
        self.eggParent2.setTitle("Parent 2")
        self.sosPokemon.setTitle("SOS Pokemon")
        
        self.pushButtonConnect.clicked.connect(self.connectCitra)
        self.pushButtonDisconnect.clicked.connect(self.disconnectCitra)
        self.doubleSpinBoxDelay.valueChanged.connect(self.updateDelay)

        self.pushButtonMainUpdate.clicked.connect(self.toggleMainRNG)
        self.pushButtonEggUpdate.clicked.connect(self.toggleEggRNG)
        self.pushButtonSOSUpdate.clicked.connect(self.toggleSOSRNG)
        
        self.mainPokemon.pushButtonUpdate.clicked.connect(self.updateMainPokemon)
        self.eggParent1.pushButtonUpdate.clicked.connect(self.updateEggParent1)
        self.eggParent2.pushButtonUpdate.clicked.connect(self.updateEggParent2)
        self.sosPokemon.pushButtonUpdate.clicked.connect(self.updateSOSPokemon)

        self.update.connect(self.updateMainRNG)
        self.update.connect(self.updateEggRNG)
        self.update.connect(self.updateSOSRNG)

    def closeEvent(self, event):
        self.saveSettings()
        #return super().closeEvent(event)

    def saveSettings(self):
        settings = QSettings()
        settings.setValue("delay", self.doubleSpinBoxDelay.value())

    def loadSettings(self):
        settings = QSettings()
        self.delay = float(settings.value("delay", 0.5))
        self.doubleSpinBoxDelay.setValue(self.delay)

    def connectCitra(self):
        index = self.comboBoxGameSelection.currentIndex()

        if index == 0:
            self.manager = ManagerSM()
        else:
            self.manager = ManagerUSUM()

        seed = self.manager.readInitialSeed()
        if seed == 0:
            message = QMessageBox()
            message.setText("Initial seed not valid.\nCheck that you are using the correct game or the latest version of the game")
            message.exec_()

            self.manager = None
            return

        self.allowUpdate = True

        self.toggleEnable(True)
        self.labelStatus.setText("Connected")
        self.pushButtonConnect.setEnabled(False)
        self.pushButtonDisconnect.setEnabled(True)

        self.mainRNG = False
        self.eggRNG = False
        self.sosRNG = False

        t = threading.Thread(target=self.autoUpdate)
        time.sleep(1)
        t.start()

    def disconnectCitra(self):
        self.allowUpdate = False
        self.manager = None

        self.toggleEnable(False)
        self.pushButtonConnect.setEnabled(True)
        self.pushButtonDisconnect.setEnabled(False)

        self.toggleMainRNG(False)
        self.toggleEggRNG(False)
        self.toggleSOSRNG(False)

        self.labelStatus.setText("Disconnected")

    def toggleEnable(self, flag):
        self.comboBoxMainIndex.setEnabled(flag)
        self.doubleSpinBoxDelay.setEnabled(flag)

        self.mainPokemon.pushButtonUpdate.setEnabled(flag)
        self.eggParent1.pushButtonUpdate.setEnabled(flag)
        self.eggParent2.pushButtonUpdate.setEnabled(flag)
        self.sosPokemon.pushButtonUpdate.setEnabled(flag)

        self.pushButtonMainUpdate.setEnabled(flag)
        self.pushButtonEggUpdate.setEnabled(flag)
        self.pushButtonSOSUpdate.setEnabled(flag)

    @Slot()
    def updateMainRNG(self):
        if self.mainRNG:
            values = self.manager.updateFrameCount()
            
            # Check to see if frame changed at all
            if values[0] == 0:
                return

            self.lineEditInitialSeed.setText(hexify(values[1]))
            self.lineEditCurrentSeed.setText(hexify(values[2]))
            self.lineEditFrame.setText(str(values[3]))
            self.lineEditTSV.setText(str(values[4]))

    def toggleMainRNG(self, flag = True):
        if self.pushButtonMainUpdate.text() == "Update" and flag:
            self.mainRNG = True
            self.pushButtonMainUpdate.setText("Pause")
        else:
            self.mainRNG = False
            self.pushButtonMainUpdate.setText("Update")

    @Slot()
    def updateEggRNG(self):
        if self.eggRNG:
            values = self.manager.eggStatus()

            if values[0] == 0:
                self.labelEggReadyStatus.setText("No egg yet")
            else:
                self.labelEggReadyStatus.setText("Egg ready")

            self.lineEditEggSeed3.setText(hexify(values[1]))
            self.lineEditEggSeed2.setText(hexify(values[2]))
            self.lineEditEggSeed1.setText(hexify(values[3]))
            self.lineEditEggSeed0.setText(hexify(values[4]))

    def toggleEggRNG(self, flag = True):
        if self.pushButtonEggUpdate.text() == "Update" and flag:
            self.eggRNG = True
            self.pushButtonEggUpdate.setText("Pause")
        else:
            self.eggRNG = False
            self.pushButtonEggUpdate.setText("Update")

    @Slot()
    def updateSOSRNG(self):
        if self.sosRNG:
            print("TODO")

    def toggleSOSRNG(self, flag = True):
        if self.pushButtonSOSUpdate.text() == "Update" and flag:
            self.sosRNG = True
            self.pushButtonSOSUpdate.setText("Pause")
        else:
            self.sosRNG = False
            self.pushButtonSOSUpdate.setText("Update")

    def updateMainPokemon(self):
        index = self.comboBoxMainIndex.currentIndex()

        if index < 6:
            pkm = self.manager.partyPokemon(index)
        else:
            pkm = self.manager.wildPokemon()

        self.mainPokemon.updateInformation(pkm)

    def updateEggParent1(self):
        pkm = self.manager.getParent(1)
        self.eggPokemonParent1.updateInformation(pkm)

    def updateEggParent2(self):
        pkm = self.manager.getParent(2)
        self.eggPokemonParent2.updateInformation(pkm)

    def updateSOSPokemon(self):
        print("TODO")

    def updateDelay(self):
        val = self.doubleSpinBoxDelay.value()
        self.delay = val

    def autoUpdate(self):
        while self.allowUpdate == True:
            self.update.emit()
            time.sleep(self.delay)