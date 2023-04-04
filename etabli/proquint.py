import proquint


def iter_uints(n):
    blocksize = 32
    mask = 2**blocksize - 1
    while True:
        yield n & mask
        n = n >> blocksize
        if not n:
            break


def int2proquint(n):
    return "-".join(proquint.uint2quint(block) for block in list(iter_uints(n))[::-1])
