NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

roomdesc = [
    [ "A", "B", "C", "D", "E" ],
    [ "F", "G", "H", "I", "J" ],
    [ "K", "L", "M", "N", "O" ],
    [ "P", "Q", "R", "S", "T" ],
    [ "U", "V", "W", "X", "Y" ],
]

roomexit = [
    [(False, False, True, False), (False, True, False, False), (False, True, True, True), (False, True, True, True), (False, False, True, True)],
    [(True, False, True, False), (False, True, True, False), (True, True, True, True), (True, False, False, True), (True, False, True, False)],
    [(True, False, True, False), (True, False, False, False), (True, False, True, False), (False, True, False, False), (True, False, True, True)],
    [(True, False, True, False), (False, True, True, False), (True, True, False, True), (False, True, False, True), (True, False, True, False)],
    [(True, True, False, False), (True, False, False, True), (False, False, False, False), (True, False, False, False), (True, False, False, False)]
]

position = (2,2)
x, y = position

while (True):
    
    description = roomdesc[x][y]
    print("You are in room " + description)
    
    print("What now...")
    command = input()
    
    if command == "north":
        if roomexit[x][y][NORTH]:
            print ("You move north...")
            x += 1
        else:
            print("You can't move north!")
    elif command == "south":
        if roomexit[x][y][SOUTH]:
            print ("You move south...")
            x -= 1
        else:
            print("You can't move south!")
    elif command == "south":
        if roomexit[x][y][EAST]:
            print ("You move east...")
            y += 1
        else:
            print("You can't move east!")
    elif command == "west":
        if roomexit[x][y][WEST]:
            print ("You move west...")
            y -= 1
        else:
            print("You can't move west!")
    elif command == "exit":
        break
    else:
        print("I don't know " + command)        
