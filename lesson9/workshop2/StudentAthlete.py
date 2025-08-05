from lesson9.workshop2.Athlete import Athlete
from lesson9.workshop2.Student import Student


class StudentAthlete(Student, Athlete):
    def __init__(self, name, student_id, sport, team):
        Student.__init__(self, name, student_id)
        Athlete.__init__(self, sport, team)

    def show_profile(self):
        print(f"Name: {self.name}, ID: {self.student_id}")
        print(f"Sport: {self.sport}, Team: {self.team}")