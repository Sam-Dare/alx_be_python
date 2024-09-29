# shopping_list_manager.py

def display_menu():
    print(f"Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []  # Initialize the shopping list as an empty list
    
    while True:
        display_menu()  # Call the display_menu function
        
        try:
            # Input choice as a number (int)
            choice = int(input("Enter your choice (number): "))
        except ValueError:
            print("Invalid choice. Please enter a valid number.")
            continue
        
        if choice == 1:
            # Prompt for and add an item to the shopping list
            item = input("Enter the item to add: ")
            shopping_list.append(item)
            print(f"Added '{item}' to the shopping list.")
        
        elif choice == 2:
            # Prompt for and remove an item from the shopping list
            item = input("Enter the item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"Removed '{item}' from the shopping list.")
            else:
                print(f"'{item}' not found in the shopping list.")
        
        elif choice == 3:
            # Display the current shopping list
            print("Current shopping list:")
            if shopping_list:
                for i, item in enumerate(shopping_list, start=1):
                    print(f"{i}. {item}")
            else:
                print("The shopping list is empty.")
        
        elif choice == 4:
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
