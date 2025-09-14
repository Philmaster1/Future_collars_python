import os
import ast

BALANCE_FILE = "balance.txt"
INVENTORY_FILE = "inventory.txt"
HISTORY_FILE = "history.txt"

def load_data(filename, default):
    if not os.path.exists(filename):
        return default
    try:
        with open(filename, "r") as f:
            return ast.literal_eval(f.read())
    except Exception as e:
        print(f"Error loading {filename}: {e}")
        return default

def save_data(filename, data):
    try:
        with open(filename, "w") as f:
            f.write(repr(data))
    except Exception as e:
        print(f"Error saving {filename}: {e}")


# Load at startup
balance = load_data(BALANCE_FILE, 0)
inventory = load_data(INVENTORY_FILE, {})
history = load_data(HISTORY_FILE, [])


def shutdown():
    save_data(BALANCE_FILE, balance)
    save_data(INVENTORY_FILE, inventory)
    save_data(HISTORY_FILE, history)
    print("Data saved. Goodbye!")

# Example main loop
try:
    # ... main program loop ...
    pass
finally:
    shutdown()