import os
todoarray = ['cooool ( )',]

def saver():
    file = open("todothingies.txt", "w")
    data = "\n".join(todoarray)
    file.write(data)

def loader(i):
    if(os.path.exists('todothingies.txt')):
            file = open("todothingies.txt", "r")
            for x in todoarray:
                todoarray.pop(i)
                i = i + 1
            for x in file:
                todoarray.append(x)
    else:
        file = open("todothingies.txt", "w")
        loader(i)

def adder():
    picker = input('Add your TODO -> ')
    todoarray.append(picker+' ( )' + '\n')
    print("Added.")
    input('Press any button to continue....')
    main()

def check():
    inputter = int(input('Insert id of the todo you want to check -> '))
    if(inputter < len(todoarray)):
        if("( )") in todoarray[inputter]:
            todoarray[inputter] = todoarray[inputter].replace("( )", "(X)")
            print('Checked successfully')
        else:
            todoarray[inputter] = todoarray[inputter].replace("(X)", "( )")
            print('Unchecked successfully')

    else:
        print('Inputted overrange value')
    input('Press any button to continue....')
    main()
    
def delete(i):
    inputter = int(input('\nWrite the id of the todo you want to delete -> '))
    if(inputter < len(todoarray)):
        todoarray.pop(inputter)
    else:
        print('Inputted overrange value')
    input('Press any button to continue....')
    main()

def main():
    i = 0
    os.system('cls'if os.name == 'nt' else 'clear')
    print("""**************************************
              Todoify
--------------------------------------

list   ┃  List todos
add    ┃  Add todo
check  ┃  Check todo
delete ┃  Delete todo
--------------------------------------
save   ┃ Save all todos
load   ┃ Load all todos
    """)
    picker = input("Pick -> ")
    picker = picker.lower()
    if(todoarray):
        if (picker == "list" or picker == 'check' or picker=='delete'):
            for x in todoarray:
                print(str(i) + ' : ' + str(todoarray[i]))
                i = i + 1
            if(picker == 'list'):
                input('Press any button to continue....')

        if (picker == 'check'):
            check()
        if (picker == 'delete'):
            delete(i)
    if (picker == 'add'):
        adder()
    if(picker == 'save'):
        saver()
    if(picker == 'load'):
        loader(i)
    if not(todoarray):
        print('Since there is nothing in your todo list, theres no reason for you to use list, check and delete.')
        input('Press any button to continue....')
    main()

main()