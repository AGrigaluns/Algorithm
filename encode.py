with open('alvis.txt', 'rb') as f:
    bytestring = f.read()
type(bytestring)

for ch in bytestring:
    print(ch, end=' ')

bytestring.decode('utf-8')
