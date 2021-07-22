class Room:
    def __init__(self, side_1 = None, side_2 = None):
        self.side_1 = side_1
        self.side_2 = side_2

    def area(self):
        if self.side_1 > 0 and self.side_2 >0:
            res_area = self.side_1 * self.side_2
            return res_area
        elif self.side_1 == 0 or self.side_2 == 0:
            raise ValueError ('Sides can`t be equal 0')

    def perimeter(self):
        if self.side_1 > 0 and self.side_2 >0:
            res_per = 2 * (self.side_1 + self.side_2)
            return res_per
        elif self.side_1 == 0 or self.side_2 == 0:
            raise ValueError ('Sides can`t be equal 0')

room_1 = Room(2, 3)
print(room_1.area())
print(room_1.perimeter())

class Student:
    def __init__(self, full_name = [], speciality = 'dev', start_of_sudy = 2018):
        self.full_name = full_name
        self.speciality = speciality
        self.start_of_sudy = start_of_sudy
        self.list_of_grades = [6, 7]

    def add_grade(self, added_grades):
        self.list_of_grades.append(added_grades)
        return self.list_of_grades

    # не вышло
    # def average(self):
    #     sum(len(self.list_of_grades)) / 2
    #     return self.list_of_grades










s = Student('Petr Petrov', 'dev', 2017)
print(s.add_grade(5))
# print(s.average())


