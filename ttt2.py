# s = 'asdfhh'
# print(len(s[1]))
# print(s[0:-1:2])
# s_1 = 'spam'
# print(s_1[0:2] + 'A' + s_1[3:]
# num1 = int(input('first num: '))
# num_2 = int(input('second num: '))
# res = num1 + num_2
# print(25, 'abc', res, sep = ', ')
# print(25, 'abc', res, sep = '\n')
# print(25, 'abc', res, sep = '')
# print(25, 'abc', res, end='!!!!!!!!!!!!!!!!!!!!!')
# s = 'Hi there!'
# print(s[1:5])
# user = input('Hello!  ')
# if user == 'Hi' or user == 'hi':
#     print('Hello!')
# print('Goodbye!')
#
#
# number = int(input('Enter num: '))
# if number > 0 and number <= 100:
#     print(" Correct num")
# else:
# #     print('Incorrect num')
# l = [1, 2, 3, 4, 5, 6]
# while l != []:
#     print(l.pop())
#     print(l)
# while l:
#     print(l.pop())
# l = [2, 4, 5, 6, 8]
# for el in l:
#     if el % 2 == 0:
#         print(el)
#     elif el % 2 == 1:
#         el += 1
#         print(el)

# l = [2, 4, 5, 7, 13, 2]
# for el in range(len(l)):
#     if l[el]%2 == 1:
#         l[el]=l[el]+1
# print(l)
# l2 = [2, 6, 8, 2, 6]
# l2.append(42)
# print(l2)

l3 = [2, 4, 3, 9.88]
a = []
b = []
c = []
for el in range(len(l3)):
    if l3[el] is l3[el].__float__():
        a.append(l3[el])
    elif l3[el] is l3[el].__int__():
        b.append(l3[el])
    elif l3[el] is l3[el].__str__():
        c.append(l3[el])
print(a)
print(b)
print(c)