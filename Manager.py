import struct
import time

from SFMT import SFMT
from Pokemon import Pokemon
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
            seed = self.connection.read_memory(self.seedAddress,4)
            self.initialSeed = struct.unpack("<I", seed[0:4])[0]
            self.sfmt = SFMT(self.initialSeed)
            self.currentSeed = 0
            self.frameCount = 0
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
        val = self.connection.read_memory(self.eggReady, 4)
        val = struct.unpack("<I", val[0:4])[0]

        seed3 = self.connection.read_memory(self.eggAddress, 4)
        seed3 = struct.unpack("<I", seed3[0:4])[0]

        seed2 = self.connection.read_memory(self.eggAddress + 4, 4)
        seed2 = struct.unpack("<I", seed2[0:4])[0]

        seed1 = self.connection.read_memory(self.eggAddress + 8, 4)
        seed1 = struct.unpack("<I", seed1[0:4])[0]
        
        seed0 = self.connection.read_memory(self.eggAddress + 12, 4)
        seed0 = struct.unpack("<I", seed0[0:4])[0]

        return [ val, seed3, seed2, seed1, seed0 ]

    def updateFrameCount(self):
        currSeed = self.getCurrentSeed()

        while currSeed != self.currentSeed:
            self.currentSeed = self.sfmt.NextULong()
            self.frameCount += 1

    def getCurrentSeed(self):
        index = self.connection.read_memory(self.sfmtIndex, 4)
        index = struct.unpack("<I", index[0:4])[0]

        if index == 624:
            pointer = self.sfmtStart
        else:
            pointer = self.sfmtStart + (index * 4)

        seed1 = self.connection.read_memory(pointer, 4)
        seed2 = self.connection.read_memory(pointer + 4, 4)
        seed1 = struct.unpack("<I", seed1[0:4])[0]
        seed2 = struct.unpack("<I", seed2[0:4])[0]

        return (seed2 << 32) | seed1