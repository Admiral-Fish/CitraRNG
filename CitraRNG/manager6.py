from citra import Citra
from pokemon import Pokemon
from mt import MT
from util import readByte, readDWord

class Manager6:
    def __init__(self):
        self.citra = Citra()

        self.partyAddress = None
        self.wildAddress = None

        self.initialSeed = None
        self.seedAddress = None
        self.mtStart = None
        self.mtIndex = None

        self.tinyStart = None

        self.eggReady = None
        self.eggAddress = None
        self.parent1Address = None
        self.parent2Address = None

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
        address = self.getWildOffset()

        blockData = self.citra.read_memory(address, 232)
        statsData = self.citra.read_memory(address + 344, 22)
        data = blockData + statsData

        return Pokemon(data)

    def getWildOffset(self):
        pass

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

        seed0 = readDWord(self.citra, self.eggAddress)
        seed1 = readDWord(self.citra, self.eggAddress + 4)

        return [ val, seed1, seed0 ]

    def readInitialSeed(self):
        self.initialSeed = readDWord(self.citra, self.seedAddress)
        self.mt = MT(self.initialSeed)
        self.currentSeed = self.initialSeed
        self.frameCount = -1

        return self.initialSeed

    def updateFrameCount(self):
        # Reseed check
        if readDWord(self.citra, self.seedAddress) != self.initialSeed:
            self.initialSeed = readDWord(self.citra, self.seedAddress)
            self.mt = MT(self.initialSeed)
            self.currentSeed = self.initialSeed
            self.frameCount = -1

        currSeed = self.getCurrentSeed()
        difference = self.frameCount
        count = 0

        while currSeed != self.currentSeed:
            self.currentSeed = self.mt.nextUInt()
            count += 1

            # Probably stuck in an infinite loop
            if count > 100000:
                return None

        self.frameCount += count
        difference = self.frameCount - difference

        tiny0 = readDWord(self.citra, self.tinyStart)
        tiny1 = readDWord(self.citra, self.tinyStart + 4)
        tiny2 = readDWord(self.citra, self.tinyStart + 8)
        tiny3 = readDWord(self.citra, self.tinyStart + 12)

        return [ difference, self.initialSeed, self.currentSeed, self.frameCount, tiny3, tiny2, tiny1, tiny0 ]

    def getCurrentSeed(self):
        index = readDWord(self.citra, self.mtIndex)

        if index == 624:
            pointer = self.mtStart
        else:
            pointer = self.mtStart + (index * 4)

        seed = readDWord(self.citra, pointer)

        return seed