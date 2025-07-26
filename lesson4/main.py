# import "filename"
# from "filename" import class, function, or variable
# from "filename" import something as "own name"

# from helper import TPL_FORMAT
# from helper import print_hello
# from helper2 import print_hello as print_formal_hello
# from helper import Point

import helper
import helper2

PATH_EXAMPLE_FILE = "example.txt"
PATH_EXAMPLE_FILE_2 = "example2.txt"

print(helper.TPL_FORMAT.format("Mark"))

helper.print_hello("John")
helper2.print_hello("John")

p1 = helper.Point(3, 4)
p2 = helper.Point(5, 12)

print(p1.length() + p2.length())

print("\n")

# Reading files
fd = open(PATH_EXAMPLE_FILE)  # Open file before start reading
# print(fd.read()) #Read entire file, returns content as string
print("\n")
# print(fd.read(8)) #Read entire file, returns content based on provided size (limit)
# print(fd.readline()) #Read single line from file, return content as string
# print(fd.readline(5)) #Read single line from file, returns content based on provided size (limit)
print(fd.readlines())  # Read entire file, return content as list of strings
# print(fd.readline(16)) #Read entire file, return content as list of strings, based on provided size (limit)
fd.close()

print("\n")

# Read by lines in loop
reader = open(PATH_EXAMPLE_FILE)
counter = 0
james_counter = 0
for line in reader:
    print("Line{}: {}".format(counter, line))
    if line.__contains__('James'):
        james_counter += 1
    counter += 1

reader.close()
print("Found {} James".format(james_counter))

print("\n")

# Reading with automatic close
with open(PATH_EXAMPLE_FILE) as fd:
    for line in fd:
        print(line)
print("The file is closed")

# Writing to file text
writer = open(PATH_EXAMPLE_FILE_2, "w")  # w - overwrite, an - append to file
writer.write("My text\n")
writer.close()

my_list = ["Line 1\n", "Line 2\n", "Line 3\n"]
writer = open(PATH_EXAMPLE_FILE_2, "a")
writer.writelines(my_list)
writer.close()