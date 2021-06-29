import png

width = 200
height = 200
img = []
for y in range(height):
    row = ()
    for x in range(width):
        row = row + (x, max(0, 200 - x - y), y)
    img.append(row)
with open('gradient.png', 'wb') as f:
    w = png.Writer(width, height, greyscale=False)
    w.write(f, img)
