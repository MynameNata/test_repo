# def rend(*args):
#     x = [*args]
#     x.sort()
#     return x[1]
#
# print(rend(17, 3, 4, 0, 5, 4))

class Person:
    def __init__(self, full_name = '', year = ''):
        self.full_name = full_name
        self.year = year

    def take_name(self):
        name = self.full_name.split()
        return name[0]

    def take_surname(self):
        surname = self.full_name.split()
        return surname[1]

    def age(self, birth_year, current_year):
        if current_year >= 1900 and current_year <= 2021:
            if birth_year <= current_year:
                return current_year - birth_year
            else:
                raise ValueError ('you wasn`t born yet')
        else:
            raise ValueError ("It`s not your century!")



    def full_name_check(self, check_is_string):
        try:
            check_is_string.isalpha()
            x = check_is_string.split()
            if len(x) == 2:
                return check_is_string
            else:
                raise ValueError ('not 2 words')
        except AttributeError:
            print('enter string')
        else:
            return check_is_string

        # try:
        #     self.full_name.isalpha()
        #     x = self.full_name.split()
        #     if len(x) == 2:
        #         return self.full_name
        #     else:
        #         raise ValueError ('not 2 words')
        # except AttributeError:
        #     print('enter string')
        # else:
        #     return self.full_name





class Employee(Person):
    def __init__(self, full_name = '', year = '', position = 'programmer', experience='', salary=1):
        super().__init__(full_name, year)
        self.position = position
        self.experience = experience
        self.salary = salary

    def type_of_position(self, works_year=1, j = 'Junior', m = 'Middle', s = 'Senior'):
        if works_year <= 3:
            return self.position + ' ' + j
        elif works_year >= 3 and works_year <= 6:
            return self.position + ' ' + m
        elif works_year > 6:
            return self.position + ' ' + s

    def increase_salary(self, increase):
        return self.salary + increase


class ITEmployee(Employee):
    def __init__(self, full_name = '', year = '', position = 'programmer', experience='', salary=1, add_skill=[]):
        super().__init__(full_name, year, position, experience, salary)




ivan = Person('Ivan Ipp', 1984)
den = Employee('Den Nm', 1988, position='programmer', experience=7, salary=4000)

print(ivan.take_name())
print(ivan.take_surname())
print(ivan.year)
print(ivan.age(birth_year=1984, current_year=2021))
print(ivan.full_name_check(check_is_string = 'Ivan Jll'))
print(den.type_of_position(works_year=8))
print(den.increase_salary(increase=500))

