def main():
    commands = [
        'balance', 'sale', 'purchase', 'account', 'list', 'warehouse', 'review', 'end'
    ]
    account_balance = 0
    warehouse = {}
    operations = []

    def print_commands():
        print("\nAvailable commands:")
        for cmd in commands:
            print(f"- {cmd}")

    print("Welcome to the Company Account & Warehouse System!")
    print_commands()

    while True:
        cmd = input("\nEnter command: ").strip().lower()
        if cmd not in commands:
            print("Invalid command. Please try again.")
            print_commands()
            continue

        if cmd == 'balance':
            try:
                amount = int(input("Enter amount to add/subtract (use negative for subtract): "))
                account_balance += amount
                operations.append({'command': 'balance', 'amount': amount})
                print(f"Account balance updated: {account_balance}")
            except ValueError:
                print("Invalid amount. Please enter an integer.")

        elif cmd == 'sale':
            name = input("Enter product name: ").strip()
            try:
                price = int(input("Enter sale price per unit: "))
                quantity = int(input("Enter quantity sold: "))
                if name not in warehouse or warehouse[name]['quantity'] < quantity:
                    print("Not enough stock in warehouse.")
                    continue
                warehouse[name]['quantity'] -= quantity
                account_balance += price * quantity
                operations.append({'command': 'sale', 'name': name, 'price': price, 'quantity': quantity})
                print(f"Sold {quantity} of {name}. Account balance: {account_balance}")
            except ValueError:
                print("Invalid input. Price and quantity must be integers.")

        elif cmd == 'purchase':
            name = input("Enter product name: ").strip()
            try:
                price = int(input("Enter purchase price per unit: "))
                quantity = int(input("Enter quantity purchased: "))
                total_cost = price * quantity
                if account_balance - total_cost < 0:
                    print("Insufficient funds for this purchase.")
                    continue
                account_balance -= total_cost
                if name in warehouse:
                    warehouse[name]['quantity'] += quantity
                    warehouse[name]['price'] = price
                else:
                    warehouse[name] = {'price': price, 'quantity': quantity}
                operations.append({'command': 'purchase', 'name': name, 'price': price, 'quantity': quantity})
                print(f"Purchased {quantity} of {name}. Account balance: {account_balance}")
            except ValueError:
                print("Invalid input. Price and quantity must be integers.")

        elif cmd == 'account':
            print(f"Current account balance: {account_balance}")

        elif cmd == 'list':
            if not warehouse:
                print("Warehouse is empty.")
            else:
                print("\nWarehouse Inventory:")
                for name, info in warehouse.items():
                    print(f"- {name}: {info['quantity']} units at {info['price']} each")

        elif cmd == 'warehouse':
            name = input("Enter product name: ").strip()
            if name in warehouse:
                info = warehouse[name]
                print(f"{name}: {info['quantity']} units at {info['price']} each")
            else:
                print(f"Product '{name}' not found in warehouse.")

        elif cmd == 'review':
            from_str = input("From index (leave empty for start): ").strip()
            to_str = input("To index (leave empty for end): ").strip()
            try:
                from_idx = int(from_str) if from_str else 0
                to_idx = int(to_str) if to_str else len(operations)
                if from_idx < 0 or to_idx > len(operations) or from_idx > to_idx:
                    print("Invalid range.")
                    continue
                print("\nRecorded operations:")
                for i, op in enumerate(operations[from_idx:to_idx], start=from_idx):
                    print(f"{i}: {op}")
            except ValueError:
                print("Invalid indices. Please enter integers or leave empty.")

        elif cmd == 'end':
            print("Exiting program. Goodbye!")
            break

        print_commands()

if __name__ == "__main__":
    main()