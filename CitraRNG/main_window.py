import threading
import time
from PySide2.QtCore import QObject, QSettings, Signal, Slot, SIGNAL, SLOT
from PySide2.QtWidgets import QMainWindow, QMessageBox
from ui_MainWindow import Ui_MainWindow
from manager_oras import ManagerORAS
from manager_sm import ManagerSM
from manager_usum import ManagerUSUM
from manager_xy import ManagerXY
from util import hexify

class MainWindow(QMainWindow, Ui_MainWindow):
    update = Signal()

    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.loadSettings()

        self.mainPokemon6.setTitle("Main Pokemon")
        self.eggParent1_6.setTitle("Parent 1")
        self.eggParent2_6.setTitle("Parent 2")

        self.mainPokemon7.setTitle("Main Pokemon")
        self.eggParent1_7.setTitle("Parent 1")
        self.eggParent2_7.setTitle("Parent 2")
        self.sosPokemon.setTitle("SOS Pokemon")
        
        self.pushButtonConnect.clicked.connect(self.connectCitra)
        self.doubleSpinBoxDelay.valueChanged.connect(self.updateDelay)
        self.comboBoxGameSelection.currentIndexChanged.connect(self.updateGame)

        self.pushButtonMainUpdate6.clicked.connect(self.toggleMainRNG6)
        self.pushButtonEggUpdate6.clicked.connect(self.toggleEggRNG6)

        self.mainPokemon6.pushButtonUpdate.clicked.connect(self.updateMainPokemon6)
        self.eggParent1_6.pushButtonUpdate.clicked.connect(self.updateEggParent1_6)
        self.eggParent2_6.pushButtonUpdate.clicked.connect(self.updateEggParent2_6)

        self.pushButtonMainUpdate7.clicked.connect(self.toggleMainRNG7)
        self.pushButtonEggUpdate7.clicked.connect(self.toggleEggRNG7)
        self.pushButtonSOSUpdate.clicked.connect(self.toggleSOSRNG)
        self.pushButtonSOSReset.clicked.connect(self.resetSOSRNG)
        
        self.mainPokemon7.pushButtonUpdate.clicked.connect(self.updateMainPokemon7)
        self.eggParent1_7.pushButtonUpdate.clicked.connect(self.updateEggParent1_7)
        self.eggParent2_7.pushButtonUpdate.clicked.connect(self.updateEggParent2_7)
        self.sosPokemon.pushButtonUpdate.clicked.connect(self.updateSOSPokemon)

    def closeEvent(self, event):
        self.saveSettings()

    def saveSettings(self):
        settings = QSettings()
        settings.setValue("delay", self.doubleSpinBoxDelay.value())

    def loadSettings(self):
        settings = QSettings()
        self.delay = float(settings.value("delay", 0.5))
        self.doubleSpinBoxDelay.setValue(self.delay)

    def connectCitra(self):
        if self.pushButtonConnect.text() == "Connect":
            self.pushButtonConnect.setText("Disconnect")

            index = self.comboBoxGameSelection.currentIndex()
            self.comboBoxGameSelection.setEnabled(False)

            if index == 0:
                self.manager = ManagerXY()
            elif index == 1:
                self.manager = ManagerORAS()
            elif index == 2:
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

            self.toggleEnable(True, index)
            self.labelStatus.setText("Connected")

            self.mainRNG = False
            self.eggRNG = False
            self.sosRNG = False
            
            QObject.disconnect(self, SIGNAL("update()"), self, SLOT("updateMainRNG6()"))
            QObject.disconnect(self, SIGNAL("update()"), self, SLOT("updateEggRNG6()"))
            QObject.disconnect(self, SIGNAL("update()"), self, SLOT("updateMainRNG7()"))
            QObject.disconnect(self, SIGNAL("update()"), self, SLOT("updateEggRNG7()"))
            QObject.disconnect(self, SIGNAL("update()"), self, SLOT("updateSOSRNG()"))
            if index == 0 or index == 1:
                self.update.connect(self.updateMainRNG6)
                self.update.connect(self.updateEggRNG6)
            else:
                self.update.connect(self.updateMainRNG7)
                self.update.connect(self.updateEggRNG7)
                self.update.connect(self.updateSOSRNG)

            t = threading.Thread(target=self.autoUpdate)
            time.sleep(1)
            t.start()
        else:
            self.pushButtonConnect.setText("Connect")

            self.allowUpdate = False
            self.manager = None

            self.toggleEnable(False, self.comboBoxGameSelection.currentIndex())

            index = self.comboBoxGameSelection.currentIndex()
            if index == 0 or index == 1:
                self.pushButtonMainUpdate6.setText("Update")
                self.pushButtonEggUpdate6.setText("Update")
            else:
                self.pushButtonMainUpdate7.setText("Update")
                self.pushButtonEggUpdate7.setText("Update")
                self.pushButtonSOSUpdate.setText("Update")

            self.labelStatus.setText("Disconnected")
            self.comboBoxGameSelection.setEnabled(True)        

    def toggleEnable(self, flag, index):
        self.doubleSpinBoxDelay.setEnabled(flag)

        if index == 0 or index == 1:
            self.comboBoxMainIndex6.setEnabled(flag)

            self.mainPokemon6.pushButtonUpdate.setEnabled(flag)
            self.eggParent1_6.pushButtonUpdate.setEnabled(flag)
            self.eggParent2_6.pushButtonUpdate.setEnabled(flag)

            self.pushButtonMainUpdate6.setEnabled(flag)
            self.pushButtonEggUpdate6.setEnabled(flag)
        else:
            self.comboBoxMainIndex7.setEnabled(flag)
            self.comboBoxSOSIndex.setEnabled(flag)

            self.mainPokemon7.pushButtonUpdate.setEnabled(flag)
            self.eggParent1_7.pushButtonUpdate.setEnabled(flag)
            self.eggParent2_7.pushButtonUpdate.setEnabled(flag)
            self.sosPokemon.pushButtonUpdate.setEnabled(flag)

            self.pushButtonMainUpdate7.setEnabled(flag)
            self.pushButtonEggUpdate7.setEnabled(flag)
            self.pushButtonSOSUpdate.setEnabled(flag)
            self.pushButtonSOSReset.setEnabled(flag)

    @Slot()
    def updateMainRNG6(self):
        if self.mainRNG:
            values = self.manager.updateFrameCount()

            # Handle infinite loop
            if values is None:
                self.toggleMainRNG6()

                message = QMessageBox()
                message.setText("Exiting an infinite loop. Make sure no patches are installed and the game is on the latest version")
                message.exec_()

                return

            difference, initialSeed, currentSeed, frameCount, save, tiny3, tiny2, tiny1, tiny0 = values
            
            # Check to see if frame changed at all
            if difference != 0:
                self.lineEditInitialSeed6.setText(hexify(initialSeed))
                self.lineEditCurrentSeed6.setText(hexify(currentSeed))
                self.lineEditFrame6.setText(str(frameCount))
                self.lineEditSaveVariable.setText(hexify(save))
                self.lineEditTiny3.setText(hexify(tiny3))
                self.lineEditTiny2.setText(hexify(tiny2))
                self.lineEditTiny1.setText(hexify(tiny1))
                self.lineEditTiny0.setText(hexify(tiny0))

    def toggleMainRNG6(self):
        if self.pushButtonMainUpdate6.text() == "Update":
            self.mainRNG = True
            self.pushButtonMainUpdate6.setText("Pause")
        else:
            self.mainRNG = False
            self.pushButtonMainUpdate6.setText("Update")

    @Slot()
    def updateEggRNG6(self):
        if self.eggRNG:
            ready, seed1, seed0 = self.manager.eggStatus()

            if ready == 0:
                self.labelEggReadyStatus6.setText("No egg yet")
            else:
                self.labelEggReadyStatus6.setText("Egg ready")

            self.lineEditEggSeed1_6.setText(hexify(seed1))
            self.lineEditEggSeed0_6.setText(hexify(seed0))

    def toggleEggRNG6(self):
        if self.pushButtonEggUpdate6.text() == "Update":
            self.eggRNG = True
            self.pushButtonEggUpdate6.setText("Pause")
        else:
            self.eggRNG = False
            self.pushButtonEggUpdate6.setText("Update")

    @Slot()
    def updateMainRNG7(self):
        if self.mainRNG:
            values = self.manager.updateFrameCount()

            # Handle infinite loop
            if values is None:
                self.toggleMainRNG7()

                message = QMessageBox()
                message.setText("Exiting an infinite loop. Make sure no patches are installed and the game is on the latest version")
                message.exec_()

                return

            difference, initialSeed, currentSeed, frameCount = values

            # Check to see if frame changed at all
            if difference != 0:
                self.lineEditInitialSeed7.setText(hexify(initialSeed))
                self.lineEditCurrentSeed7.setText(hexify(currentSeed))
                self.lineEditFrame7.setText(str(frameCount))

    def toggleMainRNG7(self):
        if self.pushButtonMainUpdate7.text() == "Update":
            self.mainRNG = True
            self.pushButtonMainUpdate7.setText("Pause")
        else:
            self.mainRNG = False
            self.pushButtonMainUpdate7.setText("Update")

    @Slot()
    def updateEggRNG7(self):
        if self.eggRNG:
            ready, seed3, seed2, seed1, seed0 = self.manager.eggStatus()

            if ready == 0:
                self.labelEggReadyStatus7.setText("No egg yet")
            else:
                self.labelEggReadyStatus7.setText("Egg ready")

            self.lineEditEggSeed3_7.setText(hexify(seed3))
            self.lineEditEggSeed2_7.setText(hexify(seed2))
            self.lineEditEggSeed1_7.setText(hexify(seed1))
            self.lineEditEggSeed0_7.setText(hexify(seed0))

    def toggleEggRNG7(self):
        if self.pushButtonEggUpdate7.text() == "Update":
            self.eggRNG = True
            self.pushButtonEggUpdate7.setText("Pause")
        else:
            self.eggRNG = False
            self.pushButtonEggUpdate7.setText("Update")

    @Slot()
    def updateSOSRNG(self):
        if self.sosRNG:
            if self.manager.sosInitialSeed is None:
                self.manager.readSOSInitialSeed()
            
            values = self.manager.updateSOSFrameCount()

            # Handle infinite loop
            if values is None:
                message = QMessageBox()
                message.setText("Exiting an infinite loop. Retry the battle and start updating before taking any actions.")
                message.exec_()

                self.toggleSOSRNG()
                return
            
            difference, initialSeed, currentSeed, frameCount, chainCount = values

            # Check to see if frame changed at all
            if difference != 0:
                self.lineEditSOSInitialSeed.setText(hexify(initialSeed))
                self.lineEditSOSCurrentSeed.setText(hexify(currentSeed))
                self.lineEditSOSFrame.setText(str(frameCount))
                self.lineEditSOSChainCount.setText(str(chainCount))

    def toggleSOSRNG(self):
        if self.pushButtonSOSUpdate.text() == "Update":
            self.sosRNG = True
            self.pushButtonSOSUpdate.setText("Pause")
        else:
            self.sosRNG = False
            self.pushButtonSOSUpdate.setText("Update")

    @Slot()
    def resetSOSRNG(self):
        self.manager.sosInitialSeed = None
        
    def updateMainPokemon6(self):
        index = self.comboBoxMainIndex6.currentIndex()

        if index < 6:
            pkm = self.manager.partyPokemon(index)
        else:
            pkm = self.manager.wildPokemon()

        self.mainPokemon6.updateInformation(pkm)

    def updateEggParent1_6(self):
        pkm = self.manager.getParent(1)
        self.eggParent1_6.updateInformation(pkm)

    def updateEggParent2_6(self):
        pkm = self.manager.getParent(2)
        self.eggParent2_6.updateInformation(pkm)

    def updateMainPokemon7(self):
        index = self.comboBoxMainIndex7.currentIndex()

        if index < 6:
            pkm = self.manager.partyPokemon(index)
        else:
            pkm = self.manager.wildPokemon()

        self.mainPokemon7.updateInformation(pkm)

    def updateEggParent1_7(self):
        pkm = self.manager.getParent(1)
        self.eggParent1_7.updateInformation(pkm)

    def updateEggParent2_7(self):
        pkm = self.manager.getParent(2)
        self.eggParent2_7.updateInformation(pkm)

    def updateSOSPokemon(self):
        index = self.comboBoxSOSIndex.currentIndex()
        pkm = self.manager.sosPokemon(index)
        self.sosPokemon.updateInformation(pkm)

    def updateDelay(self):
        val = self.doubleSpinBoxDelay.value()
        self.delay = val

    def updateGame(self):
        index = self.comboBoxGameSelection.currentIndex()

        if index == 0 or index == 1:
            self.tabWidget.widget(0).setEnabled(True)
            self.tabWidget.widget(1).setEnabled(False)
        else:
            self.tabWidget.widget(0).setEnabled(False)
            self.tabWidget.widget(1).setEnabled(True)

    def autoUpdate(self):
        while self.allowUpdate and self.manager.citra.is_connected():
            self.update.emit()
            time.sleep(self.delay)