import time

from SFMT import SFMT
from Pokemon import Pokemon
from Util import readDWord
from citra import Citra

SM = 0
USUM = 1

class Manager:
    def __init__(self, game):
        self.connection = Citra()
        
        # is_connected does not seem to work
        if self.connection.is_connected():
            self.isConnected = True
        else:
            self.isConnected = False

        self.currentGame = game

        if self.currentGame == SM:
            self.partyAddress = 0x34195E10
            self.wildAddress = 0x3254F4AC

            self.seedAddress = 0x325A3878
            self.sfmtStart = 0x33195B88
            self.sfmtIndex = 0x33196548

            self.eggReady = 0x3313EDD8
            self.eggAddress = 0x3313eddc
        else:
            self.partyAddress = 0x33F7FA44
            self.wildAddress = 0x32993404

            self.seedAddress = 0x32663BF0
            self.sfmtStart = 0x330D35D8
            self.sfmtIndex = 0x330D3F98

            self.eggReady = 0x3307B1E8
            self.eggAddress = 0x3307B1EC

        if self.isConnected == True:
            self.initialSeed = readDWord(self.connection, self.seedAddress)
            self.sfmt = SFMT(self.initialSeed)
            self.currentSeed = 0
            self.frameCount = -1
            self.updateFrameCount()

    def partyPokemon(self, index):
        address = self.partyAddress + (index * 484)

        blockData = self.connection.read_memory(address, 232)
        statsData = self.connection.read_memory(address + 344, 22)
        data = blockData + statsData

        pkm = Pokemon(data)
        return pkm

    def wildPokemon(self):
        address = self.wildAddress

        blockData = self.connection.read_memory(address, 232)
        statsData = self.connection.read_memory(address + 344, 22)
        data = blockData + statsData

        pkm = Pokemon(data)
        return pkm

    def eggStatus(self):
        val = readDWord(self.connection, self.eggReady)

        seed3 = readDWord(self.connection, self.eggAddress)
        seed2 = readDWord(self.connection, self.eggAddress + 4)
        seed1 = readDWord(self.connection, self.eggAddress + 8)
        seed0 = readDWord(self.connection, self.eggAddress + 12)

        return [ val, seed3, seed2, seed1, seed0 ]

    def updateFrameCount(self):
        currSeed = self.getCurrentSeed()

        while currSeed != self.currentSeed:
            self.currentSeed = self.sfmt.NextULong()
            self.frameCount += 1

    def getCurrentSeed(self):
        index = readDWord(self.connection, self.sfmtIndex)

        if index == 624:
            pointer = self.sfmtStart
        else:
            pointer = self.sfmtStart + (index * 4)

        seed1 = readDWord(self.connection, pointer)
        seed2 = readDWord(self.connection, pointer + 4)

        return (seed2 << 32) | seed1