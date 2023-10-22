import random

# returns the nearest multiple to 4
def nearestMultiple(num):
    if num >= 4:
        near = num + (4 - (num % 4))
    else:
        near = 4
    return near

def lose1():
    print("\n\nYOU LOSE !")
    print("Better luck next time !")
    return True

# checks whether the numbers are consecutive
def check(xyz):
    i = 1
    while i < len(xyz):
        if (xyz[i] - xyz[i-1]) != 1:
            return False
        i = i + 1
    return True

# starts the game
def start1():
    xyz = []
    last = 0
    while True:
        print("Enter 'F' to take the first chance.")
        print("Enter 'S' to take the second chance.")
        chance = input('> ')
        
        # player takes the first chance
        if chance.lower() == "f":
            while True:
                if last == 21:
                    return lose1()

                print("\nYour Turn.")
                print("\nHow many numbers do you wish to enter (1-4)?")
                inp = int(input('> '))
                
                if inp > 0 and inp <= 4:
                    comp = random.randint(1, 4)  # Randomly choose the number of numbers for the computer
                    i = 1

                    print("Now enter the values")
                    while i <= inp:
                        try:
                            a = int(input('> '))
                            xyz.append(a)
                            i = i + 1
                        except ValueError:
                            print("Invalid input. Please enter an integer.")
                    
                    # store the last element of xyz.
                    last = xyz[-1]
                    
                    # checks whether the input numbers are consecutive
                    if check(xyz) == True:
                        if last == 21:
                            return lose1()
                        else:
                            # "Computer's turn."
                            j = 1
                            while j <= comp:
                                xyz.append(last + j)
                                j = j + 1
                            print("Order of inputs after computer's turn is: ")
                            print(xyz)
                            last = xyz[-1]
                    else:
                        print("\nYou did not input consecutive integers.")
                        return True
                else:
                    print("Invalid input. You can enter 1 to 4 numbers at a time.")
                    return True
                        
        # player takes the second chance
        elif chance.lower() == "s":
            comp = random.randint(1, 4)  # Randomly choose the number of numbers for the computer
            last = 0
            while last < 21:
                # "Computer's turn"
                j = 1
                while j <= comp:
                    xyz.append(last + j)
                    j = j + 1
                print("Order of inputs after computer's turn is:")
                print(xyz)
                if xyz[-1] == 21:
                    return lose1()
                else:
                    print("\nYour turn.")
                    print("\nHow many numbers do you wish to enter (1-4)?")
                    inp = input('> ')
                    try:
                        inp = int(inp)
                    except ValueError:
                        print("Invalid input. Please enter an integer.")
                        return True
                        
                    i = 1
                    print("Enter your values")
                    while i <= inp:
                        try:
                            xyz.append(int(input('> ')))
                            i = i + 1
                        except ValueError:
                            print("Invalid input. Please enter an integer.")
                    
                    last = xyz[-1]
                    if check(xyz) == True:
                        near = nearestMultiple(last)
                        comp = random.randint(1, 4)  # Randomly choose the number of numbers for the computer
                    else:
                        # if inputs are not consecutive
                        # automatically disqualified
                        print("\nYou did not input consecutive integers.")
                        return True

            print("\n\nCONGRATULATIONS !!!")
            print("YOU WON !")
            return True

        else:
            print("wrong choice")

game = True
while game:
    print("Player 2 is Computer.")
    print("Do you want to play the 21 number game? (Yes / No)")
    ans = input('> ')
    if ans.lower() == 'yes':
        game = start1()
    else:
        print("Do you want to quit the game? (yes / no)")
        nex = input('> ')
        if nex.lower() == "yes":
            print("You are quitting the game...")
            game = False
            break
        elif nex.lower() == "no":
            print("Continuing...")
        else:
            print("Wrong choice")
