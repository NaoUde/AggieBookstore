#Naomi Udenze
#09/22/2024
#COMP 163-008
#Aggie Bookstore Pt. 2

#create genre list
genre = ["Fiction", "Narrative", "Mystery","Biography","Science Fiction", "Fantasy"]
inventory = {}

#record initial inventory from user input
for g in genre:
    genreList = []  # book titles for each

    #add the inventory value to the corresponding genre lists
    inventoryCount = int(input(f'What is the inventory count of {g}: '))

    #if there are no books, move to next genre
    if inventoryCount != 0:
        #prompt the user to fill in names for each book in inventory
        for i in range(inventoryCount):
            genreList.append(input(f'What is the {i + 1} book title: '))

    #the final list of books should be stored in the final
    #inventory under the corresponding genre name
    inventory[g] = genreList


#print available genre with inventory >1
print("\nWe offer the following genre book titles:")

for group in inventory:
    print(group)
    if len(inventory[group]) > 0:
        book = 0
        while book < (len(inventory[group])):
            print(f'\t{inventory[group][book]}')
            book += 1
    else:
        print(f"\tSorry we have no books in our inventory.")