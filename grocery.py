#simple grocery list application to learn dictionaries and lists in Python

grocery_list = []

#add item to grocery list
def add_item(name, quantity, category, bought= False):
    item = {
        "name": name,
        "quantity": quantity,
        "category": category,
        "bought": bought
    }
    grocery_list.append(item)

#display all items
def display_items():
    for item in grocery_list:
        print(item, end="\n")

#mark as bought
def mark_as_bought(name):
    for item in grocery_list:
        if item["name"] == name:
            item["bought"] = True
            print(f"{name} has been marked as bought.")
            return
    print(f"{name} not found in the grocery list.")

#remove item from grocery list
def remove_item(name):
    for item in grocery_list:
        if item["name"] == name:
            grocery_list.remove(item)
            print(f"{name} has been removed from the grocery list.")
            return
    print(f"{name} not found in the grocery list.")


def main():
    while True:
        print("\nGrocery List Menu:")
        print("1. Add Item")
        print("2. Display Items")
        print("3. Mark Item as Bought")
        print("4. Remove Item")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            category = input("Enter category: ")
            add_item(name, quantity, category)
        elif choice == '2':
            display_items()
        elif choice == '3':
            name = input("Enter item name to mark as bought: ")
            mark_as_bought(name)
        elif choice == '4':
            name = input("Enter item name to remove: ")
            remove_item(name)
        elif choice == '5':
            print("Exiting the grocery list application.")
            break
        else:
            print("Invalid choice, please try again.")

main()