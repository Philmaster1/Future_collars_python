from datetime import datetime

# Prompt the user for input
recipient_name = input("Enter the recipient's name: ")
year_of_birth = int(input("Enter the recipient's year of birth (e.g., 1990): "))
personal_message = input("Enter a short personalized message: ")
sender_name = input("Enter your name: ")

# Calculate the current year and the recipient's age
current_year = datetime.now().year
age = current_year - year_of_birth

# Generate the birthday card message
birthday_card = f"""
{recipient_name}, let's celebrate your {age} years of awesomeness!
Wishing you a day filled with joy and laughter as you turn {age}!

{personal_message}

With love and best wishes,
{sender_name}
"""

# Print the birthday card
print("\nHere is your personalized birthday card:\n")
print(birthday_card)