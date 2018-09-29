import struct

from Util import uint

def DecryptArray(encryptedData):
    pv = struct.unpack("<I", encryptedData[0x0:0x4])[0]
    sv = ((pv >> 0xD) & 0x1F) % 24
    start = 8
    end = 232

    header = encryptedData[0:8]
    blocks = ShuffleArray(CryptArray(encryptedData, pv, start, end), sv)
    stats = CryptArray(encryptedData, pv, end, len(encryptedData))

    return header + blocks + stats

def CryptArray(data, seed, start, end):
    result = bytes()
    for i in range(start, end, 2):
        seed = uint(seed * 0x41C64E6D + 0x6073)
        result += Crypt(data, seed >> 16, i)
    return result

def Crypt(data, seed, i):
    value = data[i]
    value ^= (seed & 0xFF)
    result = struct.pack("B", value)

    value = data[i + 1]
    value ^= (seed >> 8)
    result += struct.pack("B", value)

    return result

def ShuffleArray(data, sv):
    blockPosition = [ [ 0, 0, 0, 0, 0, 0, 1, 1, 2, 3, 2, 3, 1, 1, 2, 3, 2, 3, 1, 1, 2, 3, 2, 3 ],
                      [ 1, 1, 2, 3, 2, 3, 0, 0, 0, 0, 0, 0, 2, 3, 1, 1, 3, 2, 2, 3, 1, 1, 3, 2 ],
                      [ 2, 3, 1, 1, 3, 2, 2, 3, 1, 1, 3, 2, 0, 0, 0, 0, 0, 0, 3, 2, 3, 2, 1, 1 ],
                      [ 3, 2, 3, 2, 1, 1, 3, 2, 3, 2, 1, 1, 3, 2, 3, 2, 1, 1, 0, 0, 0, 0, 0, 0 ] ]
    result = bytes()
    for block in range(4):
        start = 56 * blockPosition[block][sv]
        end = start + 56
        result += data[start:end]
    return result
