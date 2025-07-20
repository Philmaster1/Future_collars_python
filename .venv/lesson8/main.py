class Student:
    def __init__(self, firstname, lastname, year=1, group="A"):
        self.firstname = firstname
        self.lastname = lastname
        self.year = year
        self.group = group

    def get_name(self):
        return "{} {}".format(self.firstname, self.lastname)

    def __str__(self):
        return "{} {} {} {}".format(self.firstname, self.lastname, self.year, self.group)

    def get_len_of_name_and_lastname(self):
        return len(self.firstname) + len(self.lastname)

    def __int__(self):
        # return len(self.firstname) + len(self.lastname)
        return self.year

    def __float__(self):
        return float(self.year)

    def __bool__(self):
        # return self.y > 1
        return self.group == "A"

    class FileCache:
        def __init__(self, filepath):
            self.fp = open(filepath)
            self.cache = {}

        def readchar(self, position):
            if position not in self.cache:
                self.fp.seek(position)
                self.cache[position] = self.fp.read(1)

    class FileReader:
        def __init__(self, filepath):
            self.fp = open(filepath)
            self.lines = []
            self.done = False

        def __iter__(self):
            if self.done:
                return iter(self.lines)
            return self

        def __next__(self):
            line = self.fp.readline()
            if not line:
                self.done = True
                self.fp.close()
                raise StopIteration
            self.lines.append(line[:-1])
            return line[:-1]

    # def read_data(path):
    #     with open(path) as fp:
    #         return [line.strip() for line in fp if line and line[0] != "#"]

    # Read data with yield (memory - optimized)
    def read_data(path):
        with open(path) as fp:
            for line in fp:
                if line and line[0] == "#":
                    continue
                yield line.strip()

    fp = open("data.txt")

    def read_line(fp):
        while True:
            line = fp.readline()
            if line == "":
                return None
            if line and line[0] == "#":
                continue
            return line

    def generator_1():
        yield 1

    def generator_2():
        print("line 1")
        yield 1
        print("line 2")
        yield 2
        print("line 3")
        yield 3
        print("end")

    def main():
        for index, line in enumerate(read_data("data.txt")):
            print("{}) {}".format(index + 1, line))

        print("")

        for num in generator_2():
            print(num)

        print("")

        student1 = Student("John", "Doe")
        student2 = Student("Jack", "Smith")

        print("{} {}".format(student1.firstname, student1.lastname))
        print("{} {}".format(student2.firstname, student2.lastname))

        print(student1.get_name())
        print(student2.get_name())

        print(student1)
        print(student2)

        print(int(student1))
        print(int(student2))

        print(float(student1))
        print(float(student2))

        if student1:
            print("Student in group A")

        fileCache = FileCache("data.txt")
        fileCache.readchar(0)
        print(fileCache.cache)
        fileCache.readchar(1)
        print(fileCache.cache)
        fileCache.readchar(1)
        print(fileCache.cache)
        fileCache.readchar(3)
        print(fileCache.cache)
        fileCache.readchar(10)
        print(fileCache.cache)

        print("")

        for line in FileReader("data.txt"):
            print(line)

    main()