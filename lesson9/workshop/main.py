from lesson9.workshop.Athlete import Athlete
from lesson9.workshop.Student import Student
from lesson9.workshop.StudentAthele import StudentAthlete


def introduce_person(person):
    person.introduce()

if __name__ == "__main__":
    s1 = Student("Jack")
    s2 = Athlete("Alex")
    s3 = StudentAthlete("Mike")

    s1.introduce()
    s2.introduce()
    s3.introduce()