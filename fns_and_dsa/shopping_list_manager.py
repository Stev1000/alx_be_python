def display_menu():
    """Display the menu options."""
    print("Shopping List Manager")  # Ensure this line is included
    print("1. Add item")
    print("2. Remove item")
    print("3. View list")
    print("4. Exit")

def main():
    shopping_list = []  # Initialize an empty shopping list
    while True:
        display_menu()  # Show the menu
        choice = input("Choose an option (1-4): ")

        if choice == '1':  # Add item
            item = input("Enter the item to add: ")
            shopping_list.append(item)
            print(f"{item} has been added to the shopping list.")

        elif choice == '2':  # Remove item
            item = input("Enter the item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"{item} has been removed from the shopping list.")
            else:
                print(f"{item} not found in the shopping list.")

        elif choice == '3':  # View list
            print("\nCurrent Shopping List:")
            if shopping_list:
                for index, item in enumerate(shopping_list, start=1):
                    print(f"{index}. {item}")
            else:
                print("The shopping list is empty.")

        elif choice == '4':  # Exit
            print("Exiting the Shopping List Manager. Goodbye!")
            break  # Exit the loop

        else:
            print("Invalid choice. Please select a valid option (1-4).")

if __name__ == "__main__":
    main()
