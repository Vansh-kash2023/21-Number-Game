# Python code to play 21 Number game

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
    return False

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
                    lose1()
                else:
                    print("\nYour Turn.")
                    print("\nHow many numbers do you wish to enter?")
                    inp = int(input('> '))
                    
                    if inp > 0 and inp <= 3:
                        comp = 4 - inp
                    else:
                        print("Wrong input. You are disqualified from the game.")
                        return False
            
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
                    
                    # checks whether the input
                    # numbers are consecutive
                    if check(xyz) == True:
                        if last == 21:
                            lose1()
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
                        return False
                        
        # player takes the second chance
        elif chance.lower() == "s":
            comp = 1
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
                    lose1()
                else:
                    print("\nYour turn.")
                    print("\nHow many numbers do you wish to enter?")
                    inp = input('> ')
                    try:
                        inp = int(inp)
                    except ValueError:
                        print("Invalid input. Please enter an integer.")
                        return False
                        
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
                        comp = near - last
                        if comp == 4:
                            comp = 3
                    else:
                        # if inputs are not consecutive
                        # automatically disqualified
                        print("\nYou did not input consecutive integers.")
                        return False
            
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
