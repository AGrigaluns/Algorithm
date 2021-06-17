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
