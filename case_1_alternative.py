

def mather(selector):
    add = False #g�r variablerna falska
    sub = False 
    mul = False 
    div = False
    summa = 0

    if (selector == "add"): #printar ut grejor 
        add = True
        print("x + y = z")
    elif (selector == "sub"):
        sub = True
        print("x - y = z")
    elif (selector == "mul"):
        mul = True
        print("x * y = z")
    elif(selector == "div"):
        div = True
        print("x / y = z")
    elif(selector == 'exit'): #exit ifall anv�ndaren skriver exit
        exit(3)
    else:
        print("Write any word thats listed above. ")
        main()
    
    print('----------------------')
    print("Calculating the variable 'z' ")


    inputterX = input("input x > ") #skriver in vad man vill att programmet ska r�kna ut
    inputterY = input("input y > ")

    if (inputterX.lstrip('-').isdigit() and inputterY.lstrip('-').isdigit()): #kollar ifall v�rderna �r siffror
        inputterX = int(inputterX)
        inputterY = int(inputterY)

        if (add == True):
           summa = inputterX + inputterY
        elif (sub == True):
           summa = inputterX + inputterY
        elif (mul == True):
            summa = inputterX * inputterY
        if (div == True):
            if (inputterX > 0 and inputterY > 0):
                summa = inputterX / inputterY
            else:
                print('Nice try adding negative values when its not mathematically possible')
        print(summa)
    else:
        print('Since we are doing math, input numbers, not letters.') #ifall inte siffra d�...
    print('Go again with the same calculation method or change?')
    inputter = input("Write 'same' to go again or 'change' to go back to the menu > ") #fr�gar anv�ndaren
    inputter = inputter.lower()

    if (inputter == 'same'):
        mather(selector)#startar om funktionen
    else:
        main()#g�r till huvudmenyn


def main():
    print('----------------------') #Meny
    print('Astonishing calculator')
    print('======================')
    print("add -> addition ")
    print("sub -> subtraction ")
    print("mul -> multiplication ")
    print("div -> division ")
    print('exit -> exit program')
    print('======================')


    selector = input('Select method > ')
    selector = selector.lower() #Konverterar till sm� bokst�ver
    
    mather(selector) #Kallar p� funktionen och skickar variabels inneh�ll till funktionen

main()