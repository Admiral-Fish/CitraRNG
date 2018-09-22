import struct
import time

from Manager import Manager
from PySide2.QtWidgets import QMainWindow, QLabel
#from PySide2 import QtCore, QtGui, QtWidgets 

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.manager = Manager(0)

        self.label = QLabel()
        self.setCentralWidget(self.label)
        self.setWindowTitle("Test")

        self.getParty()

    def getParty(self):
        text = ""
        for i in range(6):
            pkm = self.manager.PartyPokemon(i)
            if pkm.SpeciesNum() != 0:
                if text == "":
                    text = pkm.Species()
                else:
                    text = text + " " + pkm.Species()
        text = text + "\n" + "Frame Count: " + str(self.manager.frameCount)
        self.label.setText(text)