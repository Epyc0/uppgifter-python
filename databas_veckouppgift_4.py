import csv

def searcher(inputter,method):
    with open('database.csv') as fil:
        readerz = csv.DictReader(fil)
        next(readerz)
        for line in readerz:
            if(method == "exit"):
                exit(69)
            if(method == "get_id"):
                if (line['ID'] == inputter):
                    print(f"ID: {line['ID']} FORENAME: {line['FORENAME']} SURNAME: {line['SURNAME']} GENDER: {line['GENDER']} YEAR: {line['YEAR']}")
            elif(method == "scan_f"):
                if (line['FORENAME'] == inputter):
                    print(f"{line['ID']} {line['FORENAME']} {line['SURNAME']} {line['GENDER']} {line['YEAR']}")

            elif(method == "scan_s"):
                if (line['SURNAME'] == inputter):
                    print(f"{line['ID']} {line['FORENAME']} {line['SURNAME']} {line['GENDER']} {line['YEAR']}")

            else:
                print("no one has the id/name that you inputted!!")

    main()

def main():
    method = 'blah'

    print('''
    
    *********************************
    *get_id - Get person by id      * 
    *scan_f - Get people by forename*
    *scan_s - Get people by surname *
    *exit - exit program            *
    *********************************''')
    inputter = input('> ')
    method = inputter

    inputter = input('Ok, input what u want to search for > ')
    
    searcher(inputter,method)


main()