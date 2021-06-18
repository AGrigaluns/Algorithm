n = int(input("Cik lielu gribi savu dimantu? "))

print("Tagad vari apskatī savu brīnumu")

for i in range(n):
    print(' '*(n-i-1) + '* '*(i+1) )
for i in range(n):
    print(' '*(i+1) + '* '*(n-i-1))
