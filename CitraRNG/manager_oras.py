from manager6 import Manager6
from util import readDWord

class ManagerORAS(Manager6):
    def __init__(self):
        Manager6.__init__(self)

    def getOffsets(self):
        self.partyAddress = 0x8CFB26C

        self.initialSeed = None
        self.seedAddress = 0x8c59e40
        self.mtStart = 0x8c59e48
        self.mtIndex = 0x8c59e44

        self.tinyStart = 0x8C59E04

        self.eggReady = 0x8C88358
        self.eggAddress = 0x8C88360
        self.parent1Address = 0x8C88180
        self.parent2Address = 0x8C88270

    def getWildOffset(self):
        pointer = readDWord(self.citra, 0x880313C) - 0x22C0
        if pointer < 0x8000000 or pointer > 0x8DF0000:
            return 0x8804064 if readDWord(self.citra, 0x8804060) == 0 else 0x8804060
        else:
            pointer = readDWord(self.citra, pointer)
            if pointer < 0x8000000 or pointer > 0x8DF0000:
                return 0x8804064 if readDWord(self.citra, 0x8804060) == 0 else 0x8804060
            else:
                return pointer