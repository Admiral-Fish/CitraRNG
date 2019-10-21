from util import uint

class MT:
    def __init__(self, seed):
        self.mt = []
        self.index = 0
        self.seed = seed
        self.mag01 = [ 0x0, 0x9908B0DF ]
        self.initialize()

    def getInitialSeed(self):
        return self.seed

    def initialize(self):
        self.mt.append(self.seed)

        for i in range(1, 624):
            y = 0x6C078965 * (self.mt[i - 1] ^ (self.mt[i - 1] >> 30)) + i
            self.mt.append(uint(y))

    def nextUInt(self):
        if (self.index >= 624):
            self.shuffle()

        y = self.mt[self.index]
        self.index += 1

        #y ^= (y >> 11)
        #y ^= (y << 7) & 0x9D2C5680
        #y ^= (y << 15) & 0xEFC60000
        #y ^= (y >> 18)

        return y

    def shuffle(self):
        for i in range(227):
            y = (self.mt[i] & 0x80000000) | (self.mt[i + 1] & 0x7FFFFFFF)
            self.mt[i] = self.mt[i + 397] ^ (y >> 1) ^ self.mag01[y & 1]

        for i in range(227, 623):
            y = (self.mt[i] & 0x80000000) | (self.mt[i + 1] & 0x7FFFFFFF)
            self.mt[i] = self.mt[i -227] ^ (y >> 1) ^ self.mag01[y & 1]

        y = (self.mt[623] & 0x80000000) | (self.mt[0] & 0x7FFFFFFF)
        self.mt[623] = self.mt[396] ^ (y >> 1) ^ self.mag01[y & 1]

        self.index = 0
