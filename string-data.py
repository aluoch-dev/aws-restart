myString = "This is a string"
print(myString)
print(type(myString))
print(myString + " is of type " + str(type(myString)))

firstString = "Water"
secondString = "fall"
thirdString = firstString + secondString

print(thirdString)

name = input("What is your name? ")
print(name)

color = input("What is your favourite color? ")
animal = input("What is your favourite animal? ")

print("{}, you like a {} {}!".format(name, color, animal))