dictionary = {}

while True:
    print("\nDictionary Management System")
    print("1. Add a Word")
    print("2. Search for Meaning")
    print("3. Display All Words")
    print("4. Update Meaning")
    print("5. Delete Word")
    print("6. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == '1':
        word = input("Enter the word: ").lower().strip()
        if word in dictionary:
            print(f"The given word '{word}' is already exists in the dictionary")
        else:
            meaning = input("Enter the meaning: ").strip()
            dictionary[word] = meaning
            print("Word added successfully!")            

    elif choice == '2':
        word = input("Enter the word to search: ").lower().strip()
        if word in dictionary:
            print("Meaning:", dictionary[word])
        else:
            print("Word not found in the dictionary.")

    elif choice == '3':
        if dictionary:
            print("Words and their meanings:")
            for word, meaning in dictionary.items():
                print(f"{word}: {meaning}")
        else:
            print("Dictionary is empty.")

    elif choice == '4':
        word = input("Enter the word to update meaning: ").lower().strip()
        if word in dictionary:
            new_meaning = input("Enter the new meaning: ").strip()
            print("Are you sure you want to update?")
            check_point_1 = input("Type Y/N: ").lower().strip()
            if check_point_1 == "y":
                dictionary[word] = new_meaning
                print("Meaning updated successfully!")
                print("Updated Meaning:", dictionary[word])
            elif check_point_1 == "n":
                print("Updation aborted!")
            else:
                print("Invalid choice!")
        else:
            print("Word not found in the dictionary.")

    elif choice == '5':
        word = input("Enter the word to delete: ").lower().strip()
        if word in dictionary:
            print("Are you sure you want to delete?")
            check_point_2 = input("Type Y/N: ").lower().strip()
            if check_point_2 == "y":
                del dictionary[word]
                print("Word deleted successfully!")
            elif check_point_2 == "n":
                print("Deletion aborted!")
            else:
                print("Invalid choice!")
        else:
            print("Word not found in the dictionary.")

    elif choice == '6':
        print("Are you sure you want to exit?")
        check_point_3 = input("Type Y/N: ").lower().strip()
        if check_point_3 == "y":
            print("Exiting program...")
            break
        elif check_point_3 == "n":
            print("Welcome back!")
        else:
            print("Invalid option!")

    else:
        print("Invalid choice! Please enter a valid option.")



