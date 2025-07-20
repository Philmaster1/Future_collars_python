def package_loading_system():
    try: # try in case of invalid input
        max_items = int(input("Enter the maximum number of items to be shipped: "))
        if max_items <= 0:
            print("The number of items must be greater than 0.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return

    current_package_weight = 0
    package_weights = []
    item_count = 0

    while item_count < max_items:
        try:
            weight = int(input(f"Enter weight for item {item_count + 1} (1-10 kg, or 0 to stop): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 10, or 0 to stop.")
            continue

        if weight == 0:
            print("Terminating input as per user request.")
            break
        elif weight < 1 or weight > 10:
            print("Item weight must be between 1 and 10 kg.")
            continue

        if current_package_weight + weight > 20:
            package_weights.append(current_package_weight)
            current_package_weight = weight
        else:
            current_package_weight += weight

        item_count += 1

    if current_package_weight > 0:
        package_weights.append(current_package_weight)

    num_packages = len(package_weights)
    total_weight = sum(package_weights)
    total_unused_capacity = num_packages * 20 - total_weight
    max_unused = max(20 - w for w in package_weights)
    max_unused_package = package_weights.index(max(package_weights, key=lambda w: 20 - w)) + 1

    print("\n--- Shipping Summary ---")
    print(f"Number of packages sent: {num_packages}")
    print(f"Total weight of packages sent: {total_weight} kg")
    print(f"Total unused capacity: {total_unused_capacity} kg")
    print(f"Package with most unused capacity: Package {max_unused_package} ({max_unused} kg)")

# Run the program
package_loading_system()