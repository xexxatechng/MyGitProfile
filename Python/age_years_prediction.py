"""Exercise 1 (and Solution)

Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

Extras:

    Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
    Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)
    Also tell if the year is a leap year"""

Name = input("Enter your name: ")
Age = int(input("Enter your age: "))
Year = int(input("Enter current year: "))
Prediction = Year + (100 - Age)
#print(Prediction)
print("Dear " + Name + " your will turn a 100 years in " + str(Prediction))
print()
for i in range(3):
    print("Dear " + Name + " your will turn a 100 years in " + str(Prediction))
if Prediction % 4 == 0:
    print(str(Prediction) + " is a leap year.")
else:
    print(str(Prediction) + " is not a leap year.")
