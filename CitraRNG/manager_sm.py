from manager7 import Manager7

class ManagerSM(Manager7):
    def __init__(self):
        Manager7.__init__(self)

    def getOffsets(self):
        self.partyAddress = 0x34195E10
        self.wildAddress = 0x3002F7B8
        self.sosAddress = 0x3002F7B8

        self.mainSeedAddress = 0x325A3878
        self.mainSFMTStart = 0x33195B88
        self.mainSFMTIndex = 0x33196548

        self.sosSeedAddress = 0x30038C44
        self.sosSFMTStart = 0x30038C44
        self.sosSFMTIndex = 0x30039604
        self.sosChainLength = 0x3003960D

        self.eggReady = 0x3313EDD8
        self.eggAddress = 0x3313EDDC
        self.parent1Address = 0x3313EC01
        self.parent2Address = 0x3313ECEA