# ASCII program
import random
import time

# Program starts here
for data in range(5):
    randomNum = random.randint(33, 126)
    data = chr(randomNum)
    print('Random number is ' + str(randomNum))
    print('My character is ' + str(data))
    time.sleep(1)
