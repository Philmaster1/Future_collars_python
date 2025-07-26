# Example function


# Function declaration
# def function_name(parameter1, parameter2, parameter3, ..., parameter): # colon at the end
#    code to be executed line 1 # pay attention to the indentation
#    code to be executed line 2
#    code to be executed line 3

# Function execute
# function_name(1231, True, "example string") # note missing colon
# function_name(1231, True, "example string2") # note missing colon
# function_name(1231, True, "example string3") # note missing colon
# function_name(1231, True, "example string4") # note missing colon


owner = {"First name": "John", "Last name": "Smith"}
rows = [
    ("January", {"Balance": 1200, "Incomes": 1800, "Expenses": 1300}),
    ("February", {"Balance": 1300, "Incomes": 1900, "Expenses": 1200})
]


def divider():
    print("*" * 15)


def print_dict(name, row):
    divider()
    print(name)
    divider()
    for k, v in row.items():
        print("{}: {}".format(k, v))
    divider()


print_dict("Owner", owner)

for name, row in rows:
    print_dict("Month: {}".format(name), row)


# Mutable objects: dictionaries, sets, lists, objects.
# Immutable objects: integers, floating point numbers, strings, tuples.

# Immutable object (not work)
def double_value(a):
    a = a * 2


my_var = 10
print(id(my_var))
double_value(my_var)
print(my_var)
my_var = my_var + 10
print(id(my_var))

my_string = "Sample String"
double_value(my_string)
print(my_string)


# Mutable object (works)
def double_values(my_row):
    for k, v in my_row.items():
        my_row[k] = v * 2


sample_dictionary = {"a": 10, "b": "Sample String"}

double_values(sample_dictionary)

print(sample_dictionary["a"])
print(sample_dictionary["b"])

print(id(sample_dictionary))
sample_dictionary["a"] += 10
print(id(sample_dictionary))


# ===========OBJECTS=================
# object.property_name
# object.method_name

# print(object.property_name)
# object.property_name += 1


# Class ("template for objects")
class User:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def print_hello(self):
        print("Hello {} {}".format(self.firstname, self.lastname))

    def print_bye(self):
        print("Bye {} {}".format(self.firstname, self.lastname))


user1 = User("John", "Doe")
user2 = User("Mark", "Kowalski")

user1.print_hello()
user1.print_bye()

user2.print_hello()
user2.print_bye()

User.print_hello(user1)

# Operation on properties
print(user1.firstname)
user1.firstname = "Jack"
print(user1.firstname)

collection_of_objects = [user1, user2]


class Logger:
    def __init__(self):
        self.log = []

    def add(self, msg):
        self.log.append(msg)

    def print_log(self):
        print("\n".join(self.log))


logger = Logger()
logger.add("Initialize my_var2 = 5")
my_var2 = 5
logger.add("Multiply my_var2 by 10")
my_var2 *= 10
logger.add("Third message")
logger.print_log()
