#Naomi Udenze
#12/05/2024
#COMP 163-008
#Aggie Bookstore Pt. 4
#List the inventory and total amount in each genre

file = open(input("Enter inventory file: "),'r')

#iterates through every genre in the options list and prints it
def displayMenu(options):
    for i in range(len(options)):
        print(f"{i + 1}) {options[i]}")
    print(f"{len(options) + 1}) Exit")

    #returns collected input as an integer
    return int(input("Enter your choice: "))

#for each book in the chosen genre, prints out its info and tracks the inventory and cost of all copies
def displayGenreInv(genreOption, booksList):
    _Inventory = 0
    _Total = 0.0
    print(genreOption)
    print(f"\t{'Author':<20}{'Title':<30}{'Published':<9} {'QTY':<5}{'Price':<5}")
    for book in booksList:
        print(f"\t{(f"{book[1]} {book[3]} {book[2]}"):<20}{book[4]:<30}{'2024':<9} {book[8]:<5}{float(book[7]):<5}{" "*15}")
        _Inventory += int(book[8])
        _Total += float(book[7]) * int(book[8])
    print('\t' + ("=" * 33))
    print(f"\tInventory count {_Inventory} : Total ${_Total:.2f}")

#returnes a list of the genres provided in the file
def readInv(file):
    genreList = [genre for genre in file]
    return genreList

inventory = {}

#populates inventory with the books, sorted into groups based on genre
#each line is split into a list to better extract necessary information
for line in file.readlines():
    line = line.split(",")
    if line[0] in inventory: inventory[line[0]] += [line]
    else: inventory[line[0]] = [line]

choice = displayMenu(readInv(inventory))

#only if they didn't select the last place in the list (exit), display the inventory based on the index
if choice != len(inventory) + 1:
    choice = readInv(inventory)[choice - 1]
    displayGenreInv(choice, inventory[choice])

#at the very end, regardless:
print("\nAggie Book Store\nGood Bye")