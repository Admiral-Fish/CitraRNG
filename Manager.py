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
        self.currentGame = game

        if self.currentGame == SM:
            self.partyAddress = 0x34195E10
            self.seedAddress = 0x325A3878
            self.pointerStart = 0x33195B88
            self.seedIndex = 0x33196548
        else:
            self.partyAddress = 0x33F7FA44
            self.seedAddress = 0x32663BF0
            self.pointerStart = 0x330D35D8
            self.seedIndex = 0x330D3F98

        self.frameCount = 0
        seed = self.connection.read_memory(self.seedAddress,4)
        self.initialSeed = struct.unpack("<I", seed[0:4])[0]
        self.sfmt = SFMT(self.initialSeed)
        self.currentSeed = 0

        self.UpdateFrameCount()

    def PartyPokemon(self, index):
        address = self.partyAddress + (index * 484)

        partyData = self.connection.read_memory(address, 232)
        statsData = self.connection.read_memory(address + 344, 22)
        data = partyData + statsData

        pkm = Pokemon(data)
        return pkm

    def UpdateFrameCount(self):
        currSeed = self.GetCurrentSeed()

        while currSeed != self.currentSeed:
            self.currentSeed = self.sfmt.NextULong()
            self.frameCount += 1

    def GetCurrentSeed(self):
        index = self.connection.read_memory(self.seedIndex, 4)
        index = struct.unpack("<I", index[0:4])[0]

        if index == 624:
            pointer = self.pointerStart
        else:
            pointer = self.pointerStart + (index * 4)

        seed1 = self.connection.read_memory(pointer, 4)
        seed2 = self.connection.read_memory(pointer + 4, 4)
        seed1 = struct.unpack("<I", seed1[0:4])[0]
        seed2 = struct.unpack("<I", seed2[0:4])[0]

        return (seed2 << 32) | seed1