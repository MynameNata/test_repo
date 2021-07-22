def rend(*args):
    x = [*args]
    x.sort()
    return x[1]

print(rend(17, 3, 4, 0, 5, 4))

class Person:
    def __init__(self, full_name = '', birth_year = ''):
        self.full_name = full_name
        self.birth_year = birth_year

    def take_name(self):
        name = self.full_name.split()
        return name[0]


    def take_surname(self):
        surname = self.full_name.split()
        return surname[1]


    def age(self, current_year):
        if current_year >= 1900 and current_year <= 2021:
            if self.birth_year <= current_year:
                return current_year - self.birth_year
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

    # не работает __str__ поэтому больше не писала
    def __str__(self):
        return f"Name is {self.full_name}, Birth year is {self.birth_year}"

    # тоже самое иначе
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
    def __init__(self, full_name = '', birth_year ='', position ='programmer', experience='', salary=1):
        super().__init__(full_name, birth_year)
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
    def __init__(self, full_name = '', year = '', position = 'programmer', experience='', salary=1):
        super().__init__(full_name, year, position, experience, salary)
        self.skills = []

    def add_skill(self, new_skill):
        self.skills.append(new_skill)
        return new_skill



ivan = Person('Ivan Ipp', 1984)
den = Employee('Den Nm', 1988, position='programmer', experience=7, salary=4000)
it_emp = ITEmployee('Some One', 1980, position='progremmer', experience=10, salary=5000)
print(ivan.full_name)
print(ivan.take_name())
print(ivan.take_surname())
print(ivan.birth_year)
print(ivan.age(current_year=2021))
print(ivan.full_name_check(check_is_string = 'Ivan Jll'))
print(den.type_of_position(works_year=8))
print(den.increase_salary(increase=500))
print(it_emp.add_skill(new_skill='kkkk'))