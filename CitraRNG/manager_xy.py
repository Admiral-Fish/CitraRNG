from manager6 import Manager6
from util import readDWord

class ManagerXY(Manager6):
    def __init__(self):
        Manager6.__init__(self)

    def getOffsets(self):
        self.partyAddress = 0x8CE1CF8

        self.initialSeed = None
        self.seedAddress = 0x8c52844
        self.mtStart = 0x8c5284C
        self.mtIndex = 0x8c52848

        self.tinyStart = 0x8c52808

        self.eggReady = 0x8C80124
        self.eggAddress = 0x8c8012c
        self.parent1Address = 0x8C7FF4C
        self.parent2Address = 0x8C8003C

    def getWildOffset(self):
        pointer = readDWord(self.citra, 0x880313c) - 0xA1C
        if pointer < 0x8000000 or pointer > 0x8DF0000:
            return 0x8805614
        else:
            pointer = readDWord(self.citra, pointer)
            if pointer < 0x8000000 or pointer > 0x8DF0000:
                return 0x8805614
            else: 
                return pointer