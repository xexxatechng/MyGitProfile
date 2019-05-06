"""#print a head, using functions
#METHOD 1
def head():
    print("   ||||||||||||||||||||  ")
    print("   |                  |  ")
    print("   |     o       o    |  ")
    print("  _|                  |_ ")
    print(" |_          v         _|")
    print("   |     |_______|    |  ")
    print("   |                  |  ")

head()
"""

#METHOD 2
def head():
    print("   ||||||||||||||||||||  ")
def side():
    print("   |                  |  ")
def eyes():
    print("   |     o       o    |  ")
def ears_nose():
    print("  _|                  |_ ")
    print(" |_          v         _|")
def mouth():
    print("   |     |_______|    |  ")
    print("   |                  |  ")

#call individual functions that makes up the face
head()
side()
eyes()
ears_nose()
mouth()
