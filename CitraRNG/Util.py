import struct

from citra import Citra

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
