#Naomi Udenze
#11/09/2024
#COMP 163-008
#Aggie Bookstore Pt. 3
#List the overall inventory and total books stored in each genre

#get book file, genre list and inventory dict
global inventory
file = open(input("Enter genre file: "),'r')

#take the genrelist and print out each genre offered, then return the choice
def displayMenu(options):
    for i in range(len(options)):
        print(f'{i+1}) {options[i]}')

    print(f'{len(options) + 1}) Exit')
    return input("Enter your choice: ")

#return a list of all genres in the file
def readGenre(genreFile):
    fileList = genreFile.readlines()
    genList = []

    for item in fileList:
        line = item.split()
        for item in line:
            genList.append(item)

    return genList

#update inv dict with contents from file
def popInv(invList):
    for item in invList:
        inventory[item[2]] = item

#print the genre, books in it, count, and total
def displayGenreInv(genreOption):
    print(genreOption)
    print(f"\t{"Author":<20}{"Title":<30}{'Published':<9} {"Cost":<5}")
    i = 0
    cost = 0
    for book in inventory:
        if inventory[book][0] == genreOption:
            print(f"\t{inventory[book][1]:<20}{inventory[book][2]:<30}{inventory[book][3]:<9} {float(inventory[book][4]):.2f}")
            i += 1
            cost += float(inventory[book][4])
    print("="*33)
    print(f"Inventory count {i} : Total ${cost:.2f}")


#read the Inventory file into a list
def readInv():
    I = open("Inventory.csv", 'r')
    InvLines = I.readlines()
    invDict = {}

    for i in range(len(InvLines)):
        InvLines[i] = InvLines[i].split(",")
        InvLines[i][-1] = InvLines[i][-1][:-1]
        invDict[InvLines[i][2]] = InvLines[i]

    return invDict

inventory = readInv()
genreList = readGenre(file)

while True:
    while True:
        try:
            opt = int(displayMenu(genreList))
            if opt <= len(genreList) and opt > 0:
                break
            elif opt == len(genreList) + 1 and opt > 0:
                break
        except:
            pass
    if opt == len(genreList) + 1:
        break

    displayGenreInv(genreList[int(opt) - 1])



print(f"Aggie Book Store\nGood Bye")
file.close()