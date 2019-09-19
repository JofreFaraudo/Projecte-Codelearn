import random
def compare(a,b):
    for c in b:
        if c != a:
            return False
    return True
def game():
    a = [" "," "," "," "," "," "," "," "," "]
    g = [0,1,2,3,4,5,6,7,8]
    b = raw_input("Choose between X or O? ").upper()
    f = "O" if b == "X" else "X"
    b = "O" if f == "X" else "X"
    c = 1
    d = "Computer"
    e = True
    y = {"h1":False,"h2":False,"h3":False,"v1":False,"v2":False,"v3":False,"d1":False,"d2":False}
    o = {"h1":False,"h2":False,"h3":False,"v1":False,"v2":False,"v3":False,"d1":False,"d2":False}
    print "The first player is: "+d+"\n\nTurn number "+str(c)+"\n============\n   |   | \n "+a[6]+" | "+a[7]+" | "+a[8]+"   \n |   | \n-----------\n   |   | \n "+a[3]+" | "+a[4]+" | "+a[5]+" \n   |   | \n-----------\n   |   | \n "+a[0]+" | "+a[1]+" | "+a[2]+" \n   |   | \n============"
    while e:
        if d == "Computer":
            h = random.randint(0,len(g)-1)
            a[g[h]] = f
            k = g[h]
            del g[h]
        else:
            k = int(raw_input("Choose position to play (0-8): "))
            a[k] = b
            g.remove(k)
            c += 1
        print d+" occupies position "+str(k)+"\nTurn number "+str(c)+"\n============\n   |   | \n "+a[6]+" | "+a[7]+" | "+a[8]+" \n   |   | \n-----------\n   |   | \n "+a[3]+" | "+a[4]+" | "+a[5]+" \n   |   | \n-----------\n   |   | \n "+a[0]+" | "+a[1]+" | "+a[2]+" \n   |   | \n============"
        d = "Computer" if d == "Player" else "Player"
        y["h1"] = compare("X",[a[0],a[1],a[2]])
        y["h2"] = compare("X",[a[3],a[4],a[5]])
        y["h3"] = compare("X",[a[6],a[7],a[8]])
        y["v1"] = compare("X",[a[0],a[3],a[6]])
        y["v2"] = compare("X",[a[1],a[4],a[7]])
        y["v3"] = compare("X",[a[2],a[5],a[8]])
        y["d1"] = compare("X",[a[0],a[4],a[8]])
        y["d2"] = compare("X",[a[6],a[4],a[2]])
        o["h1"] = compare("O",[a[0],a[1],a[2]])
        o["h2"] = compare("O",[a[3],a[4],a[5]])
        o["h3"] = compare("O",[a[6],a[7],a[8]])
        o["v1"] = compare("O",[a[0],a[3],a[6]])
        o["v2"] = compare("O",[a[1],a[4],a[7]])
        o["v3"] = compare("O",[a[2],a[5],a[8]])
        o["d1"] = compare("O",[a[0],a[4],a[8]])
        o["d2"] = compare("O",[a[6],a[4],a[2]])
        for i in y:
            if y[i] and e:
                print "Congratulations! Player has won the game" if b == "X" else "Game over! Computer has won the game"
                e = False
        for i in o:
            if o[i] and e:
                print "Congratulations! Player has won the game" if b == "O" else "Game over! Computer has won the game"
                e = False
        if len(g) == 0 and e:
            e = False
            print "Game over! Tie game"
game()
