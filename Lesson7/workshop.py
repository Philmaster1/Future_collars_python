def main():
    initialize_csv()
    while True:
        print("\n")
        print("1.Add a new contact")
        print("2.Display all contacts")
        print("3.Search for a contact by name")
        print("4.Delete a contact")
        print("5.Exit the program")

        choice = input("Choose the number: ")

        if choice == "1":
            print("Add a new contact")
            name = input("Write the name:")
            phone = input("Write the phone:")
            email = input("Write the email:")
            print(add_contacts(name, phone, email))
        elif choice == "2":
            print("Display all contacts")
        elif choice == "3":
            print("Search for a contact by name")
        elif choice == "4":
            print("Delete a contact")
        elif choice == "5":
            print("Exit the program")
            break
        else:
            print("Wrong choice")


if __name__ == "__main__":
    main()
