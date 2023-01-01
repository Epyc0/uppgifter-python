nextplate = 1

while True:
    plate = input("input ")
    plateint = int(plate[-3:])
    print(plateint)
    if(plateint == nextplate):
        print(plate)
        nextplate+= 1
