
print("Captain Rainbow's Color Checklist")

# Initialize checklist: empty list that we can append to create Captain Rainbow's Color wardrobe
checklist = list()


# ----- an example on how to add to a list in python -----
# checklist.append('Blue')
# print(checklist)
# checklist.append('Orange')
# print(checklist)

#CREATE
def create(item):
    checklist.append(item)

#READ
def read(index):
    if index <= len(checklist) - 1:
        print(checklist[index])
        return checklist[index]
    else:
        print("\nThe index number provided is greater than the list length, please select again.\n")

#UPDATE
def update(index, item):
    if index <= len(checklist) - 1:
        checklist[index] = item
        print("The item has been updated.")
    else:
        print("\nThe index number provided is greater than the list length, please select again.\n")
   
#DESTROY

def destroy(index):
    if index <= len(checklist) - 1:
        checklist.pop(index)
    else:
        print("\nThe index number provided is greater than the list length, please select again.\n")

#LIST ALL Function
def list_all_items():
    index = 0
    for list_item in checklist:
        # print(str(index) + list_item)
        print("{} {}".format(index, list_item))
        index += 1

def mark_completed(index):
    if index <= len(checklist) - 1:
        item_check = "√" + checklist[index]
        message = "Item has been marked completed:"
        print("{} {}".format(message, item_check))
        # print(f"{message}: {item_check}")
    else:
        print("\nThe index number provided is greater than the list length, please select again.\n")
    

def uncheck(index):
    if index <= len(checklist) - 1:
        item_uncheck = checklist[index].replace('√', '')
        message = "Item that was marked completed has been unchecked:"
        print("{} {}".format(message, item_uncheck))
    else:
        print("\nThe index number provided is greater than the list length, please select again.\n")


def user_input(prompt):
    user_input = input(prompt).upper()
    return user_input


def select(function_code):
    # CREATE item
    if function_code == "C":
        input_item = user_input("Add item: ")
        create(input_item)

    # READ item
    elif function_code == "R":
        item_index = int(user_input("Provide the index number of the item that you want to see: "))
        read(item_index)

    # UPDATE an item
    elif function_code == "U":
        item_index = int(user_input("Provide the index number of the item that you want to update: "))
        updated_item = user_input("Provide the name for the item that you want to update it with: ")
        update(item_index, updated_item)
    
    # DESTROY an item
    elif function_code == "D":
        item_index = int(user_input("Provide the index number of the item that you want to delete: "))
        destroy(item_index)
    
    # PRINT all items
    elif function_code == "P":
        list_all_items()

    # MARK an item completed
    elif function_code == 'M':
        item_index = int(user_input("Provide the index number of the item that you want to mark completed: "))
        mark_completed(item_index)

    elif function_code == "X":
        item_index = int(user_input("Provide the index number of the item that you want to un-check: "))
        uncheck(item_index)

    # QUIT Fix the infinite loop by returning a fasle statement to the running condition 
    elif function_code == "Q":
        return False

    # Catch all
    else:
        print("\nUnknown Option")
    return True

# Loop 
running = True
while running:
    selection = user_input(
            "\nPress C to add to list, R to Read from list, P to display list, M to mark completed, X to un-check the completed item, U to update an item with a new one, D to delete an item and Q to quit: \n"
            )   
    running = select(selection)


def test():
    create("purple sox")
    create("red cloak")

    print(read(0))
    # print(read(1))
    update(0, "purple socks")
    destroy(1)
    print(read(0))

    mark_completed(0)

    user_value = user_input("Please Enter a value:")
    print(user_value)
    # Call your new function with the appropriate value
    select("C")
    # View the results
    list_all_items()
    # Call function with new value
    select("R")
    # View results
    list_all_items()
    

# test()



