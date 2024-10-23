import time as tm

# Function to perform bubble sort on the inventory values
def bubble_sort(dict_a):
    items = list(dict_a.items())  # Convert dictionary items to list for sorting
    for i in range(len(items) - 1, 0, -1):
        for j in range(i):
            if items[j][1] > items[j + 1][1]:  # Compare by stock values
                items[j], items[j + 1] = items[j + 1], items[j]  # Swap
    # Convert back to dictionary after sorting
    sorted_dict = {key: value for key, value in items}
    return sorted_dict

# Initial inventory
inventory = {
    "burger": 15,
    "fries": 15,
    "soda": 15
}

cond = True

def display_menu(menu):
    print("Menu")
    for key, value in menu.items():
            print(f"{key.capitalize()}: {value}")


display_menu(inventory)
while cond:
    print("\nInput 0 if you want to restock, 1 if you want to sell, 2 if you want to quit...")

    try:
        mod_opt = int(input("Do you want to restock (0)? sell (1)? or quit (2)?: "))

        if mod_opt == 0:
            # Restocking
            print("Restocking...")
            burger = int(input("Burger: "))
            fries = int(input("Fries: "))
            soda = int(input("Soda: "))
            
            # Update inventory by adding restocked amounts
            inventory["burger"] += burger
            inventory["fries"] += fries
            inventory["soda"] += soda

        elif mod_opt == 1:
            # Selling
            print("Selling...")
            burger = int(input("Burger: "))
            fries = int(input("Fries: "))
            soda = int(input("Soda: "))

            # Update inventory by subtracting sold amounts, ensure non-negative
            if burger <= inventory["burger"] and fries <= inventory["fries"] and soda <= inventory["soda"]:
                inventory["burger"] -= burger
                inventory["fries"] -= fries 
                inventory["soda"] -= soda
            else:
                print("Error: Not enough stock to complete the sale.")

        elif mod_opt == 2:
            # Exit the loop to end the program
            print("Ending program...")
            break
        else:
            print("Invalid input, please try again.")
        
        # Sort the inventory by stock values using bubble sort
        inventory = bubble_sort(inventory)

        # Print the sorted inventory
        print("\nSorted Inventory (by stock):")
        display_menu(inventory)
    except ValueError:
        print("Invalid input, please enter a number.")