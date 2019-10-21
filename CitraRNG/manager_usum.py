from manager7 import Manager7

class ManagerUSUM(Manager7):
    def __init__(self):
        Manager7.__init__(self)

    def getOffsets(self):
        self.partyAddress = 0x33F7FA44
        self.wildAddress = 0x3002F9A0
        self.sosAddress = 0x3002F9A0

        self.seedAddress = 0x32663BF0
        self.sfmtStart = 0x330D35D8
        self.sfmtIndex = 0x330D3F98

        self.sosSeedAddress = 0x30038E30
        self.sosSFMTStart = 0x30038E30
        self.sosSFMTIndex = 0x300397F0
        self.sosChainLength = 0x300397F9

        self.eggReady = 0x3307B1E8
        self.eggAddress = 0x3307B1EC
        self.parent1Address = 0x3307B011
        self.parent2Address = 0x3307B0FA
