import csv
import os.path

CSV_FILE = "contacts.csv"


def initialize_csv():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, "x", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Phone", "Email"])


def read_csv_file():
    with open(CSV_FILE, "r") as file:
        reader = csv.reader(file)
        return list(reader)


def write_csv_to_file(contacts):
    with open(CSV_FILE, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(contacts)


def add_contact(name, phone, email):
    contacts = read_csv_file()
    contacts.append([name, phone, email])
    write_csv_to_file(contacts)
    return "Contact added successfully"


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
            print(add_contact(name, phone, email))
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

