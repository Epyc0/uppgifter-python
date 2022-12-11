from array import array

todoer = [ #array
    'run 100 kilometres',
    'swim 2 meters',
    'walk 9000 micrometer',
  
    
    ]

def main(nexter): #main function
    print('\n'*40)

    if(len(todoer) > 0): #if array larger than 0 then print out array values 0-2
        print('Today: '+ todoer[nexter])
    else:
        print('Today: Nothing')

    if(len(todoer) > 1):
        print('Tomorrow: '+ todoer[nexter+1])
    else:
        print('Tomorrow: Nothing')
    
    if(len(todoer) > 2):
        print('Later: '+ todoer[nexter+2])
    else:
        print('Later: Nothing')

    print("\n")

    inputter = input('n │ Next day \n' + 'c │ Change goal \n' + 'd │ Delete todo \n' + 'e │ Exit program \n > ') #input menu
    inputter = inputter.lower()
    if(inputter == 'n'): #if press n then next day

        if (len(todoer) > 0):
            todoer.pop(0)
            todoer.append('Nothing')
            for x in todoer:
                print(x)


    if(inputter == 'c'):#if press c then prompt user to change 
        inputter = input('0 for today\n' + '1 for tomorrow\n' + '2 for later\n' + '> ')
        textinputter = input('Write what you want to put in: ')
        
        if(inputter == '0' or inputter == "1" or inputter == "2"): #if 0 then change 'today' to the value user inputted
            todoer[int(inputter)] = textinputter
        else:
            print('Follow the instructions. ')
            main()


    if(inputter == 'd'):
        inputter = int(input('0 for today\n' + '1 for tomorrow\n' + '2 for later\n' + '> '))
        todoer.pop(inputter)
        todoer.append('Nothing')

    if(inputter == 'e'):#exit if press e
        exit(9)

    else:
        print('Follow instructions.')
    main(nexter)



nexter = 0 
main(nexter)

