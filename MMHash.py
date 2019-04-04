from functools import reduce

def MMHash(s: str, x: int = 256):
    L = (x // 8) * 2
    f = lambda ords: str(hex(reduce(lambda x, y: int(x) * int(y),  ords) + int("".join(ords))))
    s = s + str(x)
    while len(s) < L:
        s = f(str((n + x) * x) + str(ord(i)) for n, i in enumerate(s))
    
    return s[-L//2:]
      
