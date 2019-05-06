"""
A version of the old macdonald rhymes, using a function with more than one parameter.
"""
def EiEio():
    print("Ee-igh, Ee-igh, oh!")
def Refrain():
    print("Old Macdonald had a farm, ")
    print(str(EiEio()))

def HadA(animal):
    print("And on the farm he had a " + animal)
    print(str(EiEio()))

def WithA(noise):
    print("With a " + noise + " " + noise + " here")
    print("And a " + noise + " " + noise + " there")
    print("Here a " + noise)
    print("there a " + noise)
    print("everywhere a " + noise + " " + noise)

def Verse(animal, noise):
    Refrain()
    print()
    HadA(animal)
    print()
    WithA(noise)
    print()
    Refrain()
    print()
    print()


#Verse("pig", "oink")

animal = input("Enter animal name: ")
noise = input("Enter noise made by animal: ")
print()
Verse(animal, noise)
