def bubbleSort(data):
    n = len(data)

    for i in range(n):
        for j in range(0, n-i-1):
            if data[j] > data[j+1] :
                data[j], data[j+1] = data[j+1], data[j]

data = [65, 108, 118, 105, 115]

bubbleSort(data)

print ("Sorted array:")
for i in range(len(data)):
    print ("%d" %data[i])
