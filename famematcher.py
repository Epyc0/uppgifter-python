import random

for i in range(1, 100): #Makes the outputs in bottom
    print("\n")


name = [ #Arrays with information
    "yes",
    "Daniel Radcliffe",
    "Rupert Grint",
    "Emma Watson",
    "Selena Gomez",
    "Jackson Freelander",
    "Christopher Chandler",
    "Eva Houdlerson",
    "Houdler Seferson",
    "Sven Svensson"

    
    
    ]

gender = [
    "male",
    "male",
    "male",
    "female",
    "female",
    "male",
    "male",
    "female",
    "female",
    "male"

    ]

haircolor = [ #Even more arrays
    "dark",
    "brown",
    "red",
    "brown",
    "brown",
    "blue",
    "brown",
    "pink",
    "white",
    "gray"
    ]

eyecolor = [ #arrays.
    "green",
    "brown",
    "blue",
    "brown",
    "brown",
    "red",
    "green",
    "gray",
    "lime",
    "blue"

    
    ]



def searcher(): #searcher function
    id = 0 #resets the variable
    found = False #also resets



    arraylength = len(name) #gets array size
    randomday = random.randint(0,arraylength-1) #randomizes the "search of the day" person characteristic
    print("Random celebrity characteristics: " + gender[randomday] + " " + haircolor[randomday] + " " + eyecolor[randomday]) #prints out the characteristics with the randomized number in array box

    genderinput = input("Input gender: ") #inputter
    genderinput = genderinput.lower()
    haircolorinput = input("Input haircolor: ")
    haircolorinput = haircolorinput.lower()

    eyecolorinput = input("Input eyecolor: ")
    eyecolorinput = eyecolorinput.lower()

    print("---------------------------------------------------------------------------------")
    for x in gender: #loops gender
        if (x == genderinput): #if gender was found
            if (haircolorinput == haircolor[id]): #then checks if the person on the same array number has the inputted hair color
                if(eyecolorinput == eyecolor[id]): #then checks eyecolor with the same procedure as stated above
                    print('ok found ' + name[id] + '. The famous person has ' + haircolor[id] + ' hair and ' + eyecolor[id] + ' eyes.') #if OK then prints out the person
                    found = True #checks that the person was found

 
        id = id + 1
    

    if (found == False):
        print("Oops, no one with the characteristics you inputted was found, try again.")
    print("---------------------------------------------------------------------------------")
    menu()



         


def menu():
    print('Hello, press 1 to run matcher or press 2 to exit')
    inputter = input()

    if (inputter == '1'):
        for i in range(1, 100): #Makes the outputs in bottom
            print("\n")
        searcher()
    elif(inputter == '2'):
        exit('User pressed ' + inputter)
    else:
        print('Follow the instructions.')
        menu()


menu()