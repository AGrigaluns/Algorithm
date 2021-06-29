import png

s = ['1110111',
     '1100011',
     '1110111',
     '1110111',
     '1100011',
     '1110111']

s = [[int(c) for c in row] for row in s]

palette=[(0x00,0x00,0x00), (0x23,0x64,0x42)]
w = png.Writer(len(s[0]), len(s), palette=palette, bitdepth=8)
f = open('logo.png', 'wb')
w.write(f, s)
