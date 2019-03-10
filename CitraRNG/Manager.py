from SFMT import SFMT
from Pokemon import Pokemon
from Util import readDWord, readByte
from citra import Citra

class Manager(object):
    def __init__(self):
        self.citra = Citra()

        self.partyAddress = None
        self.wildAddress = None
        self.sosAddress = None

        self.mainSeedAddress = None
        self.mainSFMTStart = None
        self.mainSFMTIndex = None

        self.sosSeedAddress = None
        self.sosSFMTStart = None
        self.sosSFMTIndex = None
        self.sosChainLength = None

        self.eggReady = None
        self.eggAddress = None
        self.parent1Address = None
        self.parent2Address = None

        self.trainerID = None

        self.mainInitialSeed = None
        self.sosInitialSeed = None
        
        self.getOffsets()
		
    def getOffsets(self):
        pass            
            
    def partyPokemon(self, index):
        address = self.partyAddress + (index * 484)

        blockData = self.citra.read_memory(address, 232)
        statsData = self.citra.read_memory(address + 344, 22)
        data = blockData + statsData

        return Pokemon(data)

    def wildPokemon(self):
        address = self.wildAddress

        blockData = self.citra.read_memory(address, 232)
        statsData = self.citra.read_memory(address + 344, 22)
        data = blockData + statsData

        return Pokemon(data)

    def sosPokemon(self, index):
        address = self.sosAddress + (index * 484)

        blockData = self.citra.read_memory(address, 232)
        statsData = self.citra.read_memory(address + 344, 22)
        data = blockData + statsData

        return Pokemon(data)

    def getParent(self, num):
        if num == 1:
            address = self.parent1Address
        else:
            address = self.parent2Address

        blockData = self.citra.read_memory(address, 232)
        statsData = self.citra.read_memory(address + 344, 22)
        data = blockData + statsData

        return Pokemon(data)

    def eggStatus(self):
        val = readDWord(self.citra, self.eggReady)

        seed3 = readDWord(self.citra, self.eggAddress)
        seed2 = readDWord(self.citra, self.eggAddress + 4)
        seed1 = readDWord(self.citra, self.eggAddress + 8)
        seed0 = readDWord(self.citra, self.eggAddress + 12)

        return [ val, seed3, seed2, seed1, seed0 ]

    def readMainInitialSeed(self):
        self.mainInitialSeed = readDWord(self.citra, self.mainSeedAddress)
        self.mainSFMT = SFMT(self.mainInitialSeed)
        self.mainCurrentSeed = self.mainInitialSeed
        self.mainFrameCount = -1

        return self.mainInitialSeed

    def updateMainFrameCount(self):        
        currSeed = self.getMainCurrentSeed()
        difference = self.mainFrameCount

        while currSeed != self.mainCurrentSeed:
            self.mainCurrentSeed = self.mainSFMT.nextULong()
            self.mainFrameCount += 1

        difference = self.mainFrameCount - difference
        return [ difference, self.mainInitialSeed, self.mainCurrentSeed, self.mainFrameCount, self.trainerShinyValue() ]

    def getMainCurrentSeed(self):
        index = readDWord(self.citra, self.mainSFMTIndex)

        if index == 624:
            pointer = self.mainSFMTStart
        else:
            pointer = self.mainSFMTStart + (index * 4)

        seed1 = readDWord(self.citra, pointer)
        seed2 = readDWord(self.citra, pointer + 4)

        return (seed2 << 32) | seed1

    def readSOSInitialSeed(self):
        self.sosInitialSeed = readDWord(self.citra, self.sosSeedAddress)
        self.sosSFMT = SFMT(self.sosInitialSeed)
        self.sosCurrentSeed = self.sosInitialSeed
        self.sosFrameCount = -1

        return self.sosInitialSeed

    def updateSOSFrameCount(self):        
        currSeed = self.getSOSCurrentSeed()
        difference = self.sosFrameCount

        if currSeed == self.sosInitialSeed:
            difference = -2

        while currSeed != self.sosCurrentSeed:
            self.sosCurrentSeed = self.sosSFMT.nextUInt()
            self.sosFrameCount += 1

        difference = self.sosFrameCount - difference
        return [ difference, self.sosInitialSeed, self.sosCurrentSeed, self.sosFrameCount, self.sosChainCount() ]

    def getSOSCurrentSeed(self):
        index = readDWord(self.citra, self.sosSFMTIndex)

        if index == 624:
            pointer = self.sosSFMTStart
        else:
            pointer = self.sosSFMTStart + (index * 4)

        seed = readDWord(self.citra, pointer)

        return seed

    def trainerShinyValue(self):
        val = readDWord(self.citra, self.trainerID)
        return ((val >> 16) ^ (val & 0xffff)) >> 4

    def sosChainCount(self):
        return readByte(self.citra, self.sosChainLength)