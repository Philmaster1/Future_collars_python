message = "Hello"
print(message)

message = message + "World"
print(message)

# Integer
counter = 2
print(counter)

# Floating-point number
weight_sum = 10.5
print(weight_sum)

# Boolean
always_true = True
print(always_true)
never_true = False
print(never_true)

# String
message2 = "Message"
print(message2)
message3 = """
Hello 
World
123
xyz
"""
print(message3)

# None
nothing_here = None
print(nothing_here)

# Operations on variables
a = 1.5
b = 0.5

print(a + b)
print(a - b)
print(a * b)
print(a / b)

a = 2
b = 3

print(a ** b)  # 2 * 2 * 2
print(b % a)  # Rest from divide

# Comparing
print(a == b)
print(a != b)
print(a < b)
print(a <= b)
print(a > b)
print(a >= b)

print("")
print("")

# Operating with logical (Boolean) variables
print(False or False)
print(False or True)
print(True or False)
print(True or True)

print("")
print("")

print(False and False)
print(False and True)
print(True and False)
print(True and True)

print("")
print("")

print(not False)
print(not True)

print("")
print("")

# Cast to boolean
print(bool(-1))
print(bool(1))
print(bool(0))
print(bool(""))
print(bool("text"))
print(bool(None))

# Check variable type
variable1 = "text"
print(type(variable1))
print(type(variable1) is str)

variable2 = 123
print(type(variable2))
print(type(variable2) is int)

# Converting variable types
print(2 + 2)  # 4
print("2" + "2")  # 22
print(int("2") + int("2"))  # 4
print(bool(1))

message = "new message"
print(message)
message = 2
print(message)

# Test operation
print("Hello" + " " + "World")
print("Hello " * 5)

print("Text for %s formatting %i" % ("a", 2))  # Deprecated

print("This is the {} program line".format(124))
print("This is the {} program line containing word '{}'".format(125, "Future Collars"))

# Get user input
print("What's your name?")
user_name = input()
print("Hello " + user_name)

print("How old are you?")
age = input()
print("You have {} years old".format(age))

print("Whats your birth year")
birth_year = int(input())
print(2025 - birth_year)

print("1 \n 2 \n 3 \n 4\n")
print("I am using \"quotes\"")