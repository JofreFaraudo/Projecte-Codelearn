def getOrientation():
    entrada = raw_input("Would you like to place the boat vertically or horizontally? (v / h) ").upper()
    while entrada != "V" and entrada != "H":
        entrada = raw_input("Sorry, this in not a valid option.\nWould you like to place the boat vertically or horizontally? (v / h) ").upper()
    return entrada
def wrongPosition(position):
    if ":" not in position:
        return True
    else:
        position = position.split(":")
        try:
            position[0] = int(position[0])
            position[1] = int(position[1])
        except:
            return True
        else:
            if position[0]<5 and position[0]>=0 and position[1]<5 and position[1]>=0:
                return False
            else:
                return True
def someBoxOccupied(b,x,y,o):
    for i in range(3):
        if x > 4 or y > 4:
            return True
        if b[x][y] != "W":
            return True
        if o == "V":
            x += 1
        else:
            y += 1
    return False
def applyPlay(b,shoot):
    x = int(shoot[0])
    y = int(shoot[2])
    c = b[x][y]
    if c in ["X","O"]:
        print "This box has already been played! You\'ve missed a shot!"
    elif c == "S":
        print "IMPACT!"
        b[x][y] = "O"
    elif c == "W":
        print "WATER!"
        b[x][y] = "X"
    return b
def final(b):
    a = []
    for i in b:
        a += i
    return "S" not in a
def showBoard(b):
    for i in b:
        print "".join(i)
def startBoard():
    return [ [ "W" for i in range(5) ] for j in range(5) ]
def getPosition():
    positin = raw_input("Initial box [row:column from 0 to 4]: ")
    while(wrongPosition(positin)):
        print "Sorry, this is not a valid position"
        positin = raw_input("Initial box [row:column from 0 to 4]: ")
    return positin
def placeShip(b,i):
    if i != 0:
        print "Reading the 3 positions ship number "+str(i)
    pos = getPosition()
    o = getOrientation()
    x,y = int(pos[0]),int(pos[2])
    if someBoxOccupied(b,x,y,o):
        print "Sorry, some of the positions where you want to place this ship is already occupied or does not exist. Try again"
        return placeShip(b,0)
    for i in range(3):
        b[x][y] = "S"
        if o == "V":
            x += 1
        else:
            y += 1
    return b
def placeShips(b):
    print "You have 3 boats of 3 positions"
    for i in range(3):
        b = placeShip(b,i+1)
    return b
print "Welcome to Battleship game\nPlace your ships playerA"
p1 = placeShips(startBoard())
showBoard(p1)
print "\n\n\nPlace your ships playerB"
p2 = placeShips(startBoard())
showBoard(p2)
print "\n\n"
turn = "A"
while True:
    if final(p1):
        print "Congratulation, you won playerB"
        break
    if final(p2):
        print "Congratulation, you won playerA"
        break
    shoot = raw_input("Select the box to shoot player"+turn+" (row:column from 0 to 4): ")
    while wrongPosition(shoot):
        print "Sorry, this is not a valid position"
        shoot = raw_input("Select the box to shoot player"+turn+" (row:column from 0 to 4): ")
    if turn == "A":
        p2 = applyPlay(p2,shoot)
        print "\n\n"
        showBoard(p2)
    elif turn == "B":
        p1 = applyPlay(p1,shoot)
        print "\n\n"
        showBoard(p1)
    else:
        print "An error was ocurred. Quiting game."
        break
    print "\n\n"
    turn = "A" if turn == "B" else "B"
def getOrientation():
    entrada = raw_input("Would you like to place the boat vertically or horizontally? (v / h) ").upper()
    while entrada != "V" and entrada != "H":
        entrada = raw_input("Sorry, this in not a valid option.\nWould you like to place the boat vertically or horizontally? (v / h) ").upper()
    return entrada
def wrongPosition(position):
    if ":" not in position:
        return True
    else:
        position = position.split(":")
        try:
            position[0] = int(position[0])
            position[1] = int(position[1])
        except:
            return True
        else:
            if position[0]<5 and position[0]>=0 and position[1]<5 and position[1]>=0:
                return False
            else:
                return True
def someBoxOccupied(b,x,y,o):
    for i in range(3):
        if x > 4 or y > 4:
            return True
        if b[x][y] != "W":
            return True
        if o == "V":
            x += 1
        else:
            y += 1
    return False
def applyPlay(b,shoot):
    x = int(shoot[0])
    y = int(shoot[2])
    c = b[x][y]
    if c in ["X","O"]:
        print "This box has already been played! You\'ve missed a shot!"
    elif c == "S":
        print "IMPACT!"
        b[x][y] = "O"
    elif c == "W":
        print "WATER!"
        b[x][y] = "X"
    return b
def final(b):
    a = []
    for i in b:
        a += i
    return "S" not in a
def showBoard(b):
    for i in b:
        print "".join(i)
def startBoard():
    return [ [ "W" for i in range(5) ] for j in range(5) ]
def getPosition():
    positin = raw_input("Initial box [row:column from 0 to 4]: ")
    while(wrongPosition(positin)):
        print "Sorry, this is not a valid position"
        positin = raw_input("Initial box [row:column from 0 to 4]: ")
    return positin
def placeShip(b,i):
    if i != 0:
        print "Reading the 3 positions ship number "+str(i)
    pos = getPosition()
    o = getOrientation()
    x,y = int(pos[0]),int(pos[2])
    if someBoxOccupied(b,x,y,o):
        print "Sorry, some of the positions where you want to place this ship is already occupied or does not exist. Try again"
        return placeShip(b,0)
    for i in range(3):
        b[x][y] = "S"
        if o == "V":
            x += 1
        else:
            y += 1
    return b
def placeShips(b):
    print "You have 3 boats of 3 positions"
    for i in range(3):
        b = placeShip(b,i+1)
    return b
print "Welcome to Battleship game\nPlace your ships playerA"
p1 = placeShips(startBoard())
showBoard(p1)
print "\n\n\nPlace your ships playerB"
p2 = placeShips(startBoard())
showBoard(p2)
print "\n\n"
turn = "A"
while True:
    if final(p1):
        print "Congratulation, you won playerB"
        break
    if final(p2):
        print "Congratulation, you won playerA"
        break
    shoot = raw_input("Select the box to shoot player"+turn+" (row:column from 0 to 4): ")
    while wrongPosition(shoot):
        print "Sorry, this is not a valid position"
        shoot = raw_input("Select the box to shoot player"+turn+" (row:column from 0 to 4): ")
    if turn == "A":
        p2 = applyPlay(p2,shoot)
        print "\n\n"
        showBoard(p2)
    elif turn == "B":
        p1 = applyPlay(p1,shoot)
        print "\n\n"
        showBoard(p1)
    else:
        print "An error was ocurred. Quiting game."
        break
    print "\n\n"
    turn = "A" if turn == "B" else "B"
