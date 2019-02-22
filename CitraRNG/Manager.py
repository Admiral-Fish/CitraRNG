from SFMT import SFMT
from Pokemon import Pokemon
from Util import readDWord
from citra import Citra

class Manager(object):
    def __init__(self):
        self.connection = Citra()

        self.partyAddress = None
        self.wildAddress = None
        self.seedAddress = None
        self.sfmtStart = None
        self.sfmtIndex = None
        self.eggReady = None
        self.eggAddress = None
        self.trainerID = None
        self.initialSeed = None
        
        self.getOffsets()
		
    def getOffsets(self):
        pass            
            
    def partyPokemon(self, index):
        address = self.partyAddress + (index * 484)

        blockData = self.connection.read_memory(address, 232)
        statsData = self.connection.read_memory(address + 344, 22)
        data = blockData + statsData

        return Pokemon(data)

    def wildPokemon(self):
        address = self.wildAddress

        blockData = self.connection.read_memory(address, 232)
        statsData = self.connection.read_memory(address + 344, 22)
        data = blockData + statsData

        return Pokemon(data)

    def eggStatus(self):
        val = readDWord(self.connection, self.eggReady)

        seed3 = readDWord(self.connection, self.eggAddress)
        seed2 = readDWord(self.connection, self.eggAddress + 4)
        seed1 = readDWord(self.connection, self.eggAddress + 8)
        seed0 = readDWord(self.connection, self.eggAddress + 12)

        return [ val, seed3, seed2, seed1, seed0 ]

    def readInitialSeed(self):
        self.initialSeed = readDWord(self.connection, self.seedAddress)
        self.sfmt = SFMT(self.initialSeed)
        self.currentSeed = 0
        self.frameCount = -1

        return self.initialSeed

    def updateFrameCount(self):        
        currSeed = self.getCurrentSeed()
        difference = self.frameCount

        while currSeed != self.currentSeed:
            self.currentSeed = self.sfmt.nextULong()
            self.frameCount += 1

        difference = self.frameCount - difference
        return [ difference, self.initialSeed, self.currentSeed, self.frameCount, self.trainerShinyValue() ]

    def getCurrentSeed(self):
        index = readDWord(self.connection, self.sfmtIndex)

        if index == 624:
            pointer = self.sfmtStart
        else:
            pointer = self.sfmtStart + (index * 4)

        seed1 = readDWord(self.connection, pointer)
        seed2 = readDWord(self.connection, pointer + 4)

        return (seed2 << 32) | seed1

    def trainerShinyValue(self):
        val = readDWord(self.connection, self.trainerID)
        return ((val >> 16) ^ (val & 0xffff)) >> 4