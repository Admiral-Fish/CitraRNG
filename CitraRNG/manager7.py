from citra import Citra
from pokemon import Pokemon
from sfmt import SFMT
from util import readByte, readDWord

class Manager7:
    def __init__(self):
        self.citra = Citra()

        self.partyAddress = None
        self.wildAddress = None

        self.initialSeed = None
        self.seedAddress = None
        self.sfmtStart = None
        self.sfmtIndex = None

        self.eggReady = None
        self.eggAddress = None
        self.parent1Address = None
        self.parent2Address = None

        self.sosSeedAddress = None
        self.sosSFMTStart = None
        self.sosSFMTIndex = None
        self.sosChainLength = None
        self.sosInitialSeed = None
        self.sosAddress = None

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
        ready = readDWord(self.citra, self.eggReady)

        seed0 = readDWord(self.citra, self.eggAddress)
        seed1 = readDWord(self.citra, self.eggAddress + 4)
        seed2 = readDWord(self.citra, self.eggAddress + 8)
        seed3 = readDWord(self.citra, self.eggAddress + 12)

        return ready, seed3, seed2, seed1, seed0

    def readInitialSeed(self):
        self.initialSeed = readDWord(self.citra, self.seedAddress)
        self.sfmt = SFMT(self.initialSeed)
        self.currentSeed = self.initialSeed
        self.frameCount = -1

        return self.initialSeed

    def updateFrameCount(self):        
        currSeed = self.getCurrentSeed()
        difference = self.frameCount
        count = 0

        while currSeed != self.currentSeed:
            self.currentSeed = self.sfmt.nextULong()
            count += 1

            # Probably stuck in an infinite loop
            if count > 1000000:
                return None

        self.frameCount += count
        difference = self.frameCount - difference
        return difference, self.initialSeed, self.currentSeed, self.frameCount

    def getCurrentSeed(self):
        index = readDWord(self.citra, self.sfmtIndex)
        pointer = self.sfmtStart if index == 624 else self.sfmtStart + (index * 4)

        seed1 = readDWord(self.citra, pointer)
        seed2 = readDWord(self.citra, pointer + 4)

        return (seed2 << 32) | seed1

    def sosPokemon(self, index):
        address = self.sosAddress + (index * 484)

        blockData = self.citra.read_memory(address, 232)
        statsData = self.citra.read_memory(address + 344, 22)
        data = blockData + statsData

        return Pokemon(data)

    def readSOSInitialSeed(self):
        self.sosInitialSeed = readDWord(self.citra, self.sosSeedAddress)
        self.sosSFMT = SFMT(self.sosInitialSeed)
        self.sosCurrentSeed = self.sosInitialSeed
        self.sosFrameCount = -1

        return self.sosInitialSeed

    def updateSOSFrameCount(self):        
        currSeed = self.getSOSCurrentSeed()
        difference = self.sosFrameCount
        count = 0

        if currSeed == self.sosInitialSeed:
            difference = -2

        while currSeed != self.sosCurrentSeed:
            self.sosCurrentSeed = self.sosSFMT.nextUInt()
            count += 1

            # Probably stuck in an infinite loop
            if count > 100000:
                return None            
            
        self.sosFrameCount += count
        difference = self.sosFrameCount - difference
        return difference, self.sosInitialSeed, self.sosCurrentSeed, self.sosFrameCount, self.sosChainCount()

    def getSOSCurrentSeed(self):
        index = readDWord(self.citra, self.sosSFMTIndex)
        pointer = self.sosSFMTStart if index == 624 else self.sosSFMTStart + (index * 4)
        seed = readDWord(self.citra, pointer)

        return seed

    def sosChainCount(self):
        return readByte(self.citra, self.sosChainLength)