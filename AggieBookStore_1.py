#Naomi Udenze
#09/22/2024
#COMP 163-008
#Aggie Bookstore Pt. 1

#create genre list
genre = [["Fiction"], ["Narrative"], ["Mystery"],["Biography"],["Science Fiction"], ["Fantasy"]]

#record initial inventory from user input
for g in genre:
    #add the inventory value to the corresponding genre lists
    inventory = int(input(f'What is the inventory count of {g[0]}: '))
    g.append(inventory)

#print each genre and inventory
for g in genre:
    print(f'{g[0]}: {g[1]}')


#print available genre with inventory >1
print("\nWe offer the following genre:")
i = False
for g in genre:
    if(g[1] > 0):
        print(g[0])
        i = True

if not i:
    print("Sorry we have no genres in our inventory.")