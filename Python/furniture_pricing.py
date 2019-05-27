#Code written by:       Christian Nwachukwu
#Date:                  25/05/2019
#Application puppose:   Application gives the correct price if the right options and chosen else prompts for re-entry.

while True:
    print()
    print("Enter 1, 2 or 3 to obtain prices")
    option = int(input())
    if option == 1:
        print("Pine Table = $100")
    elif option == 2:
        print("Oak Table = $225")
    elif option == 3:
        print("Mahogany Table = $310")
    else:
        print("Invalid code, price = $0")
        print("Enter 1, 2 or 3 to obtain prices")
        print("Press 'y' to re-enter")
        selection = input()
        if selection != 'y':
            break
        else:
            continue
