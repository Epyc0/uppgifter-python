
import math

food = [0,8,20.95,4,34.95,1,13.95] #Array with food values in order: 0 as placeholder value + packageamount + price


for i in range(1, 100): #Makes the outputs in bottom
    print("\n")


def main():


    totaler = 0
    doginput = 0
    vegdoginput = 0
    peopletotaler = 0

    dogsummary = 0
    vegdogsummary = 0

    doginput = int(input('OK. How many students wants 2 hotdogs: '))
    peopletotaler = doginput
    dogsummary = doginput * 2
    doginput = int(input('OK. How many students wants 3 hotdogs: '))
    peopletotaler = peopletotaler + doginput
    dogsummary =  dogsummary + doginput * 3
    

    vegdoginput = int(input('OK. How many students want 2 vegan hotdogs: '))
    peopletotaler = peopletotaler + vegdoginput
    vegdogsummary = vegdoginput * 2
    vegdoginput = int(input('OK. How many students want 3 vegan hotdogs: '))
    peopletotaler = peopletotaler + vegdoginput
    vegdogsummary = vegdogsummary + vegdoginput * 3


    sodaamount = peopletotaler #gets the amount of people.
    
    if (sodaamount > 0):
        
        sodatotaler = sodaamount * food[6] #how much the soda will cost, gets price from the array.
        sodatotaler = math.ceil(sodatotaler * 100) / 100 #makes the value up to 2 decimals


       

        print("--------------------------")

        print('OK. ' + str(sodaamount) + " soda's and that will be " + str(sodatotaler) + "Kr")
        totaler = totaler + sodatotaler #adds value to the total variable


    if (doginput > 0):  #if user typed in value less than 1 then the if wont run
        dogresult = dogsummary / food[1] #will take the inputted value and subtract it with package value

        if (dogresult != int(dogresult)): #if result has decimal then make the amount of packages + 1
            dogresult = dogresult + 1

        dogresult = math.trunc(dogresult)
        dogmoneytotal = dogresult * food[2]
        dogmoneytotal = math.ceil(dogmoneytotal * 100) / 100

        print("OK. You need " + str(dogsummary) + " hotdogs and "+ str(dogresult) + " packages of hotdogs, which costs " + str(dogmoneytotal) + "Kr")
        totaler = totaler + dogmoneytotal #adds to the total variable
    
    if (vegdoginput > 0):
        vegdogresult = vegdogsummary / food[3]

        if (vegdogresult != int(vegdogresult)):
            vegdogresult = vegdogresult + 1
        vegdogresult = math.trunc(vegdogresult)
        vegdogmoneytotal = vegdogresult * food[4]
        vegdogmoneytotal = math.ceil(vegdogmoneytotal * 100) / 100


        print("OK. You need "+  str(vegdogsummary) + " vegohotdogs and "+  str(vegdogresult) + " packages of veghotdogs, which costs " + str(vegdogmoneytotal)+"Kr")
        totaler = totaler + vegdogmoneytotal

        print("--------------------------")
    
    totaler = math.ceil(totaler * 100) / 100 #once again makes it up to 2 decimal value

    print("It will be " + str(totaler) + 'Kr in total') #total summary
    print("--------------------------")
    menu()


    







def menu():
    print('Hello, press 1 to run main or press 2 to exit')

    inputter = input()
    for i in range(1, 100): #clears screen
        print("\n")

    if (inputter == "1"):
        main()
    elif(inputter == "2"): #exits
        exit("User inputted " + inputter)
    else: #if user didnt follow instruction for some reason the program will prompt the user to actually follow the instructions.
        for i in range(1, 100): #clears screen
            print("\n")
        print('Try following the instructions above.') 
        menu()




menu()