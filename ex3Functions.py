# Basic function training

def myFunction(name, age):
    print("My name is " + name + " and my age is " + str(age))

myFunction("Alvis", 27)


# print people
def print_people(*people):
  for person in people:
    print("This person is ", person)

print_people("Alvis", "Juris", "Andris")


# do basic math
def do_math(num1, num2):
  return num1 + num2

math1 = do_math(5, 7)
math2 = do_math(11, 34)

print("First sum is", math1, "and the secound sum is", math2)

# python Write a function

def is_leap(year):
    leap = False

    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    else:
        return False

    return leap

year = int(input())
