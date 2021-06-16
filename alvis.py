# UTF-8
data = 'Alvis Grigaļūns'

print(data.encode('utf-8'))

# ASCII
data = 'Alvis Grigaļūns'

data.encode('ascii', 'replace')

# Bubble sort
def bubbleSort(data):
    n = len(data)

    # loop go through all array elements
    for i in range(n):

        #  i elements go to right place
        for j in range(0, n-i-1):

            # array go from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if data[j] > data[j+1] :
                data[j], data[j+1] = data[j+1], data[j]

# Driver code to test above
data = [65, 108, 118, 105, 115]

bubbleSort(data)

print ("Sorted data is:")
for i in range(len(data)):
    print ("%d" %data[i])
