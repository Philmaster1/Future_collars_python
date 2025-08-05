from lesson9.workshop.Athlete import Athlete
from lesson9.workshop.Student import Student


class StudentAthlete(Student, Athlete):
    def __init__(self, name):
        super().__init__(name)

    def introduce(self):
        print(f" I'm {self.name}; and I'm both")
