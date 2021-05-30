from math import sqrt

str = 'hello  world.'
# является ли строк записью числа
print(str.isdigit())

# сколько пробелов в строке
print(str.count(' '))

# сколько точке в строке
print(str.count('.'))

# стока длянной 100 символов заполенная по бокам пробелами
str_2 = "Homework"
str_new = str_2.center(100, '+')
print(str_new)
print(len(str_new))

# все слова с большой буквы
print(str.title())

# заканчивается ли подстрока на 'ing'
str_3 = 'Looking for and aa'
print(str_3.find('ing', 0, -1))

# инлекс певого вхождения "а"
print(str_3.find('a', 0, -1))

# разбить строку на подстроки
str_4 = 'hellow world'
print(str_4.split())

# удалить начальные и конечные пробелы
str_5 = " aaa bbb ccc "
print(str_5.strip())

# вычислить гипотенузу
a = 367
b = 127
print(sqrt(a**2 + b**2))

# сколько десятков
num_1 = 543
print(num_1 // 10 % 10)

# дробная часть
num_2 = 6.3
print(num_2%1)

# первая цифра после десятичной точки
x = 8.3456
print(int(x * 10) % 10)

# 3-е с конца слово из списка
l = ['name', 'age', 'address', 'position']
print(l[-3])
# 1-й символ второго слова
print(l[1][0])
# последний символ последнего слова
print(l[-1][-1])
# добавить слово в список
l_2 = [23, 'abc', 6, 'rrr']
l_2.append('jjjjj')
print(l_2)
# вставить слово в середину списка
l_2.insert(1, 'added_word')
print(l_2)
# удадить первое слово из списка
l_2.remove(23)
print(l_2)

# удалить слово 'world' если оно есть в списке
l_3 = [45, 'game', 'world', 999, [1, 77]]
for el in l_3:
    if el == 'world':
        l_3.remove('world')
        print(l_3)

# добавить пару в список.
dic_1 = {'title': 'fruit', 'price': 8, 'ingredients': ['apple', 'banana', 'pear']}
dic_1.update({'description':'red'})
print(dic_1)

# увеличить цену на 100
dic_1['price'] += 100
print(dic_1)

# добвить еще один ингридиент
dic_1['ingredients'].append('kkkkkkkkkkkkk')
print(dic_1)

# колличество ингридиентов
print(dic_1['ingredients'].__len__())

# удалить значение с ключом 'description'
del dic_1['description']
print(dic_1)
