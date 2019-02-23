from Manager import Manager

class ManagerUSUM(Manager):
    def __init__(self):
        Manager.__init__(self)

    def getOffsets(self):
        self.partyAddress = 0x33F7FA44
        self.wildAddress = 0x32993404
        self.parent1Address = 0x3307B011
        self.parent2Address = 0x3307B0FA

        self.seedAddress = 0x32663BF0
        self.sfmtStart = 0x330D35D8
        self.sfmtIndex = 0x330D3F98

        self.eggReady = 0x3307B1E8
        self.eggAddress = 0x3307B1EC

        self.trainerID = 0x33012818
