from functools import reduce

def MMHash(s, x: int = 256) -> str:
    def f(ords) -> str:
        return str(hex(reduce(lambda prev, curr: int(prev) * int(curr),  ords) + int("".join(ords))))
    
    L = (x // 8) * 2
    
    mmhash = ''
    while len(mmhash) < L:
        mmhash = f([str((n + x) * x) + str(ord(i)) for n, i in enumerate(mmhash or (s + str(x)))])
    
    return mmhash[-L // 2:]
