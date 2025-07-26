# Empty
list1 = []
print(list1)

list2 = list()
print(list2)

# Strings
list3 = ["Adam", "John", "Mike", "Mark"]
print(list3)

# Mix
list4 = ["John", 30, False]
print(list4)

# List in list
list5 = ["John", [123, 456]]
print(list5)

print(list3[0])
print(list3[1])

print(list5[0])
print(list5[1])
print(list5[1][1])

list_name = ["Adam", "John", "Mike", "Mark"]
start_index = 2
print(list_name[start_index])
print(list_name[start_index + 1])
print(list_name[start_index - 1])

# Negative index
print(list_name[-1])
print(list_name[-2])

print(len(list_name))

# Range function (the same as [0, 1, 2, 3, 4, 5])
print(range(6))
for index in range(6):
    print(index)

# Iteration
for firstname in list_name:
    print("Name: {}".format(firstname))

# Adding element at end of the list
list_name.append("Ewa")
print(list_name)

# Editting element
list_name[1] = "Bill"
print(list_name)

# Insert between elements
list_name.insert(2, "Anna")
print(list_name)

# Add list to list
list_name_female = ["Anna", "Ewa"]
list_name_male = ["Adam", "Bill", "Mike", "Mark"]

print(list_name_female)
print(list_name_male)

list_name_all = list_name_female + list_name_male
print(list_name_all)

# Delete item
del list_name_all[2]
print(list_name_all)

list_name_all.remove("Mike")
print(list_name_all)

# Remove when duplicated string
firstnames = ["Adam", "Ewa", "Marcin", "Krzysztof", "Jakub", "Anita", "Marcin", "Ewa"]
firstnames.remove("Marcin")
print(firstnames)

# Find index
print(firstnames.index("Ewa"))
print(firstnames.index("Ewa", 2))

# Containment testing
if "Jakub" in firstnames:
    print("Jacob is in the list")

if "John" not in firstnames:
    print("John is not in the list")

# Lists in logical context (bool)
sample_list = []
print(bool(sample_list))

sample_list = ["a", "b"]
print(bool(sample_list))

# =================TUPLES==================
# Tuples are "faster" but cannot be modified
empty_tuple = tuple()

# "()" is not mandatory in this case
integer_tuple = (1, 2, 3, 4, 5)
print(integer_tuple)

mixed_tuple = ("aaa", 123, True)
print(mixed_tuple)

# Tuple in list - remember to use "()"
tuple_inside_of_list = [(1, 2), "aaa", "bbb", (4, 5, 6)]
print(tuple_inside_of_list[0])

# integer_tuple[0] = 123 <- prohibited


# Convert tuple to list or list to tuple
integer_list = list(integer_tuple)
integer_list[0] = 123
print(integer_list)

firstnames_tuple = tuple(firstnames)
print(firstnames_tuple)

# Assigning multiple variables in one ling
# a = 1
# b = 2

a, b = 1, 2

fullnames = [
    ("Adam", "Abacki"),
    ("Bartosz", "Babacki"),
    ("Czeslaw", "Cabacki")
]

for fullname in fullnames:
    print("{}".format(fullname))

for firstname, lastname in fullnames:
    print("Firsname: {} Lastname: {}".format(firstname, lastname))

# Hashable and id
var1 = 1
print(id(var1))

var1 = var1 + 1
print(id(var1))

# ====================SETS================
# Every value is unique, not keep order

empty_set = set()
print(empty_set)

sample_set = {"a", "b", "c", 123, False, (1, 2)}
print(sample_set)

# sample_set = {"a", "b", "c", 123, False, (1, 2), [1, 2]} list is not allowed in set

sample_set.add("d")
print(sample_set)

sample_set.add("a")
print(sample_set)

print("a" in sample_set)

# print(sample_set[0]) <- prohibited


for element in sample_set:
    print(element)

# Convert
list_of_elements = ["a", "b", "c", "d", "c", "c", "a", "e"]
print(list_of_elements)

set_of_elements = set(list_of_elements)
print(set_of_elements)

print("Removed {} duplicates".format(len(list_of_elements) - len(set_of_elements)))