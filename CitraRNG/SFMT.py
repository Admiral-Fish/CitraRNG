from Util import uint

class SFMT:
    def __init__(self, seed):
        self.sfmt = []
        self.index = 0
        self.Initialize(seed)

    def Initialize(self, seed):
        self.sfmt.append(seed)

        for i in range(1, 624):
            y = 0x6C078965 * (self.sfmt[i - 1] ^ (self.sfmt[i - 1] >> 30)) + i
            self.sfmt.append(uint(y))

        self.PeriodCertificaion()
        self.Shuffle()

    def PeriodCertificaion(self):
        inner = 0
        work = 0
        parity = [ 0x1, 0x0, 0x0, 0x13c9e684 ]

        for i in range(4):
            inner ^= self.sfmt[i] & parity[i]
        for i in [ 16, 8, 4, 2, 1 ]:
            inner ^= inner >> i
        if (inner & 1) == 1:
            return

        for i in range(4):
            work = 1
            for j in range(32):
                if (work & parity[i]) != 0:
                    self.sfmt[i] ^= work
                    return
                work <<= 1

    def NextUInt(self):
        if (self.index >= 624):
            self.Shuffle()
            self.index = 0

        val = self.sfmt[self.index]
        self.index += 1

        return val

    def NextULong(self):
        if (self.index >= 624):
            self.Shuffle()
            self.index = 0

        low = self.sfmt[self.index]
        self.index += 1
        high = self.sfmt[self.index]
        self.index += 1

        return (high << 32) | low

    def Shuffle(self):
        a = 0
        b = 488
        c = 616
        d = 620
        while a < 624:
            self.sfmt[a + 3] = self.sfmt[a + 3] ^ (uint(self.sfmt[a + 3] << 8)) ^ (self.sfmt[a + 2] >> 24) ^ (self.sfmt[c + 3] >> 8) ^ ((self.sfmt[b + 3] >> 11) & 0xbffffff6) ^ (uint(self.sfmt[d + 3] << 18))
            self.sfmt[a + 2] = self.sfmt[a + 2] ^ (uint(self.sfmt[a + 2] << 8)) ^ (self.sfmt[a + 1] >> 24) ^ (uint(self.sfmt[c + 3] << 24)) ^ (self.sfmt[c + 2] >> 8) ^ ((self.sfmt[b + 2] >> 11) & 0xbffaffff) ^ (uint(self.sfmt[d + 2] << 18))
            self.sfmt[a + 1] = self.sfmt[a + 1] ^ (uint(self.sfmt[a + 1] << 8)) ^ (self.sfmt[a] >> 24) ^ (uint(self.sfmt[c + 2] << 24)) ^ (self.sfmt[c + 1] >> 8) ^ ((self.sfmt[b + 1] >> 11) & 0xddfecb7f) ^ (uint(self.sfmt[d + 1] << 18))
            self.sfmt[a] = self.sfmt[a] ^ (uint(self.sfmt[a] << 8)) ^ (uint(self.sfmt[c + 1] << 24)) ^ (self.sfmt[c] >> 8) ^ ((self.sfmt[b] >> 11) & 0xdfffffef) ^ (uint(self.sfmt[d] << 18))
            c = d
            d = a
            a += 4
            b += 4
            if (b >= 624):
                b = 0
