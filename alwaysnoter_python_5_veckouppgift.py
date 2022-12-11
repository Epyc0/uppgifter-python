import os

notetitle  =[
    'hehe',
    'grejor',
    'important stuff',
    ]


notecontent=[
    'OK',
    'yes',
    'COOL',
    ]

def viewer():
    inputter = input('Enter title > ')
    try:
        location = notetitle.index(inputter)
        print(notecontent[location])
    except:
        print('Nice try, ' + inputter + ' is not valid.')
    input('Press any button to continue....')

    main()


def adder():
    inputter = input('Input title > ')
    notetitle.append(inputter)
    inputterr = input('Input description > ')
    notecontent.append(inputterr)
    input('Press any button to continue....')

    main()



def remover():
    inputter = input('Enter title > ')

    try:
        location = notetitle.index(inputter)
        notetitle.pop(location)
        notecontent.pop(location)

    except:
        print('Write an existing title.')

    input('Press any button to continue....')

    main()

     
def main():
    os.system('cls'if os.name == 'nt' else 'clear')
    print('''
-- Platinum Edition --

* Notes from lectures *
            ''')
    for x in notetitle:
        print('- '+ str(x)) 
    print('''

--------------------
        
view - view note
add  - add note
rm   - remove note
exit - exit program
        ''')

    inputter = input('> ')

    match inputter:
        case 'view':
            viewer()
        case 'add':
            adder()
        case 'rm':
            remover()
        case default:
            print("Follow instructions.")
            main()


main()