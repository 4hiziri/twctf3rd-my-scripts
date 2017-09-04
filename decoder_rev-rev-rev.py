table = {}
table['-'] = hex(0x4b)
table['.'] = hex(0x8b)
table['/'] = hex(0x0b)
table['0'] = hex(0xf3)
table['1'] = hex(0x73)
table['2'] = hex(0xb3)
table['3'] = hex(0x33)
table['4'] = hex(0xd3)
table['5'] = hex(0x53)
table['6'] = hex(0x93)
table['7'] = hex(0x13)
table['8'] = hex(0xe3)
table['9'] = hex(0x63)
table[':'] = hex(0xa3)
table[';'] = hex(0x23)
table['<'] = hex(0xc3)
table['='] = hex(0x43)
table['>'] = hex(0x83)
table['?'] = hex(0x03)
table['@'] = hex(0xfd)
table['A'] = hex(0x7d)
table['B'] = hex(0xbd)
table['C'] = hex(0x3d)
table['D'] = hex(0xdd)
table['E'] = hex(0x5d)
table['F'] = hex(0x9d)
table['G'] = hex(0x1d)
table['H'] = hex(0xed)
table['I'] = hex(0x6d)
table['J'] = hex(0xad)
table['K'] = hex(0x2d)
table['L'] = hex(0xcd)
table['M'] = hex(0x4d)
table['N'] = hex(0x8d)
table['O'] = hex(0x0d)
table['P'] = hex(0xf5)
table['Q'] = hex(0x75)
table['R'] = hex(0xb5)
table['S'] = hex(0x35)
table['T'] = hex(0xd5)
table['U'] = hex(0x55)
table['V'] = hex(0x95)
table['W'] = hex(0x15)
table['X'] = hex(0xe6)
table['Y'] = hex(0x65)
table['Z'] = hex(0xa5)
table['['] = hex(0x25)
table['\\'] = hex(0xc5)
table[']'] = hex(0x45)
table['^'] = hex(0x85)
table['_'] = hex(0x05)
table['`'] = hex(0xf5)
table['a'] = hex(0x79)
table['b'] = hex(0xb9)
table['c'] = hex(0x39)
table['d'] = hex(0xd9)
table['e'] = hex(0x59)
table['f'] = hex(0x99)
table['g'] = hex(0x19)
table['h'] = hex(0xe9)
table['i'] = hex(0x69)
table['j'] = hex(0xa9)
table['k'] = hex(0x29)
table['l'] = hex(0xc9)
table['m'] = hex(0x49)
table['n'] = hex(0x89)
table['o'] = hex(0x09)
table['p'] = hex(0xf1)
table['q'] = hex(0x71)
table['r'] = hex(0xb1)
table['s'] = hex(0x31)
table['t'] = hex(0xd1)
table['u'] = hex(0x51)
table['v'] = hex(0x91)
table['w'] = hex(0x11)
table['x'] = hex(0xe1)
table['y'] = hex(0x61)
table['z'] = hex(0xa1)
table['{'] = hex(0x21)
table['|'] = hex(0xc1)
table['}'] = hex(0x41)
table['~'] = hex(0x81)

l = ["0x41",
     "0x29",
     "0xd9",
     "0x65",
     "0xa1",
     "0xf1",
     "0xe1",
     "0xc9",
     "0x19",
     "0x9",
     "0x93",
     "0x13",
     "0xa1",
     "0x9",
     "0xb9",
     "0x49",
     "0xb9",
     "0x89",
     "0xdd",
     "0x61",
     "0x31",
     "0x69",
     "0xa1",
     "0xf1",
     "0x71",
     "0x21",
     "0x9d",
     "0xd5",
     "0x3d",
     "0x15",
     "0xd5"]

rev_table = {}
for k, e in table.items():
    rev_table[e] = k

l.reverse()
a = list(map(lambda x: rev_table[x], l))

ans = ""
for c in a:   
    ans += c

print(ans)
