from Manager import Manager

class ManagerSM(Manager):
    def __init__(self):
        Manager.__init__(self)

    def getOffsets(self):
        self.partyAddress = 0x34195E10
        self.wildAddress = 0x3254F4AC

        self.seedAddress = 0x325A3878
        self.sfmtStart = 0x33195B88
        self.sfmtIndex = 0x33196548

        self.eggReady = 0x3313EDD8
        self.eggAddress = 0x3313eddc

        self.trainerID = 0x330D67D0