import re
from os import path
def menu():
    users = {}
    inp = ""
    while inp != "exit":
        print "=====================================\nWelcome to Social Network\n=====================================\nnew --> Create new user\ncat --> Show user information\nls ---> List users\nadd --> Add friends to an user\nse ---> Search user by pattern\nmv ---> Modify user information\nsave -> Save users to disk\nload -> Load users from disk\nexit -> Logout\n====================================="
        inp = raw_input("Enter option: ").lower()
        while(inp not in ["new","cat","ls","add","se","mv","save","load","exit"]):
            inp = raw_input("Invalid option\nEnter option: ").lower()
        if inp == "new":
            users = newUser(users)
        if inp == "cat":
            searchUser(users)
        if inp == "ls":
            listUsers(users)
        if inp == "add":
            users = acceptUser(users)
        if inp == "se":
            searchPattern(users)
        if inp == "mv":
            users = moveUser(users)
        if inp == "save":
            saveData(users)
        if inp == "load":
            users = loadData()
    if raw_input("Are you sure to logout (y/n)? ").lower() == "y":
        if raw_input("Want to save data (y/n)? ").lower() != "n":
            saveData(users)
        print "Thanks for using Social Network"
        return
    return menu()
def listUser(dni,d):
    u = d[dni]
    print "Dni: "+dni
    print "Name and surname: "+u["name"]+" "+u["surname"]
    for i in ["network","town","preference","email"]:
        try:
            print i[0].upper()+i[1:]+": "+u[i]
        except:
            pass
    if len(u["friends"]) == 0:
        print "No friends found"
    else:
        print str(len(u["friends"]))+" friends found:"
        for j in d.iterkeys():
                if j in u["friends"]:
                    print d[j]["name"]+" "+d[j]["surname"]
def listUsers(d):
    print "=====================================\nList users Social Network\n====================================="
    if len(list(d.iterkeys())) > 0:
        for dni in d.iterkeys():
            listUser(dni,d)
            print "====================================="
    print str(len(list(d.iterkeys())))+" users found in social network\n"
def searchUser(d):
    dni = raw_input("Enter dni: ")
    if dni in d.iterkeys():
        print "User found. Displaying information:"
        listUser(dni,d)
    else:
        print "No user found\n"           
def newUser(d):
    print "=====================================\nCreating new user in Social Network\n====================================="
    dni = raw_input("Enter dni: ")
    if dni in d.iterkeys():
        print "Repeated user in DSN"
        return newUser(d)
    name = raw_input("Enter name: ")
    surname = raw_input("Enter surname: ")
    town = raw_input("Enter town: ")
    preference = raw_input("Enter preference: ")
    email = raw_input("Enter email: ")
    while email in [ i["email"] for i in d.itervalues() ] or not re.match(re.compile(r'^.+@[^.].*\.[a-z]{2,10}$',flags=re.IGNORECASE),email): #Some code of this line is made by https://stackabuse.com/introduction-to-regular-expressions-in-python/
        email = raw_input("Invalid email. Reenter email: ")
    password = raw_input("Enter password: ")
    print "User created"
    d[dni] = {"name":name,"surname":surname,"town":town,"preference":preference,"email":email,"password":password,"friends":[]}
    return d
def acceptUser(d):
    print "=====================================\nMake friends in Social Network\n====================================="
    if len(d) == 0:
        print "NO USERS FOUND"
        return d
    dni1 = raw_input("Enter dni1: ")
    if dni1 not in d.iterkeys():
        print "dni1 is not user of Social Network"
        return d
    dni2 = raw_input("Enter dni2: ")
    if dni2 not in d.iterkeys():
        print "dni2 is not user of Social Network"
        return d
    print "dn1 and dni2 are users of Social Network"
    for i in d.iterkeys():
        if i == dni1:
            d[i]["friends"].append(dni2)
            print "Friends of "+dni1+": "+(str(d[i]["friends"]).replace(","," ").replace("[","").replace("]",""))
        if i == dni2:
            d[i]["friends"].append(dni1)
            print "Friends of "+dni2+": "+(str(d[i]["friends"]).replace(","," ").replace("[","").replace("]",""))
    return d
def searchPattern(d):
    n = 0;
    print "=====================================\nSearch Social Network users\n====================================="
    pattern = raw_input("Enter pattern to search: ")
    print "\n"
    for i in d.iterkeys():
        if pattern in i or pattern in str(d[i].values()).replace(",","").replace("[","").replace("]","").replace("\'",""):
            listUser(i,d)
            print "\n"
            n += 1
    print str(n)+" matching users with pattern washington in Social Network" if n > 0 else "0 users found in Social Network"
def moveUser(d):
    options = {"t":"town","p":"preference","e":"email","n":"name","s":"surname"}
    print "=====================================\nModify User Information Social Network\n====================================="
    dni = raw_input("Enter Dni: ")
    if dni not in d.keys():
        print "User not exists"
        return moveUser(d)
    print "Existing user"
    password = raw_input("Enter password for user "+dni+": ")
    if password != d[dni]["password"]:
        print "Invalid password. Try again."
        return moveUser(d)
    print "Password correct\n\nInformation for user "+dni+":"
    listUser(dni,d)
    print "=====================================\nt. Modify town\np. Modify preference\ne. Modify email\nn. Modify name\ns. Modify surname\nx. Exit"
    option = raw_input("Enter option: ").lower()
    if option not in options.keys():
        print "Invalid option. Quiting to main menu."
    while option != "x":
        val = raw_input("Enter new "+options[option]+": ")
        if option == "e" and val in [ i["email"] for i in d.itervalues() ] and not re.match(re.compile(r'^.+@[^.].*\.[a-z]{2,10}$',flags=re.IGNORECASE),val): #Some code of this line is made by https://stackabuse.com/introduction-to-regular-expressions-in-python/
            print [ i["email"] for i in d.itervalues() ]
            print bool(re.match(re.compile(r'^.+@[^.].*\.[a-z]{2,10}$',flags=re.IGNORECASE),val))
            print "Invalid email. Quiting to main menu."
            break
        d[dni][options[option]] = val
        print "=====================================\nt. Modify town\np. Modify preference\ne. Modify email\nn. Modify name\ns. Modify surname\nx. Exit"
        option = raw_input("Enter option: ").lower()
        if option not in options.keys():
            print "Invalid option. Quiting to main menu."
            break
        print "Changes done"
    return d
def saveData(d):
    print "All information saved to disk in file data.txt"
    dataFile = open("data.txt","w" if path.exists("data.txt") else "a")
    for dni in d.iterkeys():
        data = ""
        for i in ["name","surname","town","preference","email","password","friends"]:
            data += " "+str(d[dni][i]).replace(",","").replace("[","").replace("]","").replace("\'","")
        dataFile.write(dni+data+"\n")
    dataFile.close()
def loadData():
    dataFile = open("data.txt", "r") 
    data = dataFile.readlines()
    d = {}
    for i in data:
        l = i.replace("\n","").split(" ",7)
        d[l[0]] = {"name":l[1],"surname":l[2],"town":l[3],"preference":l[4],"email":l[5],"password":l[6],"friends":[ j for j in l[7].split(" ") ]}
        if "" in d[l[0]]["friends"]:
            d[l[0]]["friends"].remove("")
    dataFile.close()
    print "All information loaded from disk in file data.txt"
menu()
