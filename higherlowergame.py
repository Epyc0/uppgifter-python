import random

for i in range(1, 100): #Makes the outputs in bottom
    print("\n")


def game(): #function.
    howmanytimesguessed = 1 #makes it 1 incase the player gets correct one on first try.
    randomnumber = random.randint(0,99) #randomise

    while (1):
        inputter = int(input('Your guess: ')) #input 
        
        if (inputter >= 0 or inputter <= 99): #if in range



            if (inputter == randomnumber): #if correct
                print('Correct.')
                break #break the loop if correct
            elif (inputter > randomnumber): #if inputted too high
                print('Lower.')
            elif (inputter < randomnumber): #if inputted too low
                print('Higher.')
            howmanytimesguessed = howmanytimesguessed + 1 #increase guessed variable

        else:
            print('Input a value HIGHER or EQUAL to 0 or a value LOWER or EQUAL to 99 ') #if player guesses value out of range
            
    print('----------------------------------')
    print('Nice, it was ' + str(randomnumber) + '. Took you this amount of tries: ' + str(howmanytimesguessed)) #stats
    print('----------------------------------')

    menu() #goes back to menu




def menu():
    print('Hello, press 1 to play the game or press 2 to exit')
    inputter = input()

    if (inputter == '1'):
        for i in range(1, 100): #Makes the outputs in bottom
            print("\n")
        game()
    elif(inputter == '2'):
        exit('User pressed ' + inputter) #quit
    else:
        print('Follow the instructions.') #if player doesnt follow incruction
        menu()


menu() #starts the menu function