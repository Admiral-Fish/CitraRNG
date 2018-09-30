import struct

from citra import Citra
from PySide2.QtWidgets import QPushButton, QLabel, QLineEdit, QComboBox, QSpinBox

def convertByte(data, start):
    return struct.unpack("B", data[start:start+1])[0]

def convertWord(data, start):
    return struct.unpack("<H", data[start:start+2])[0]

def convertDWord(data, start):
    return struct.unpack("<I", data[start:start+4])[0]

def readByte(citra, address):
    data = citra.read_memory(address, 1)
    return convertByte(data, 0)

def readWord(citra, address):
    data = citra.read_memory(address, 2)
    return convertWord(data, 0)

def readDWord(citra, address):
    data = citra.read_memory(address, 4)
    return convertDWord(data, 0)

def hexify(num):
    return str(hex(num))[2:].upper()

def colorIV(iv):
    if iv == 30 or iv == 31:
        return "<b><font color ='green'>" + str(iv) + "</font></b>"
    elif iv == 0 or iv == 1:
        return "<b><font color = 'red'>" + str(iv) + "</font></b>"
    else:
        return str(iv)

def colorPSV(psv, tsv):
    if psv == tsv:
        return "<b><font color ='green'>" + str(psv) + "</font></b>"
    else:
        return str(psv)

def findComboBox(ui, name):
    return ui.findChild(QComboBox, name)

def findButton(ui, name):
    return ui.findChild(QPushButton, name)

def findLabel(ui, name):
    return ui.findChild(QLabel, name)

def findLineEdit(ui, name):
    return ui.findChild(QLineEdit, name)

def findSpinBox(ui, name):
    return ui.findChild(QSpinBox, name)

def uint(val):
    return val & 0xFFFFFFFF
