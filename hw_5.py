while True:
    try:
        num_1 = input('enter first number ')
        num_2 = input('enter second number ')
    except NameError:
        print(num_1 + num_2)
    else:
        print(num_1 + num_2)


def my_input():
    while True:
        try:
            x = float(input('enter number '))
            break
        except ValueError:
            continue
        else:
            return x
    print(x)

my_input()




def my_string():
    while True:
        r = input('enter word ')
        if ' ' in r or ' ' is r:
            continue

        elif r.startswith(' ') or r.endswith(' '):
            return r
            break
        else:
            print(r)
            break


my_string()

def year_leap():
    year = int(input('enter year '))
    if year % 4 == 0 or year % 400 == 0 and year % 100 == 1:
        return True
    else:
        return False


year_leap()


def triangle(a, b, c):
    # a = float(input('enter num1 '))
    # b = float(input('enter num2 '))
    # c = float(input('enter num3 '))
    if a == 0 or b == 0 or c == 0:
        return False
    else:
        return True

a = float(input('enter num1 '))
b = float(input('enter num2 '))
c = float(input('enter num3 '))
print(triangle(a, b, c))


def type_of_triangle(q, w, e):
    if q == w and w == e and e == q:
        print('Equilateral triangle (равносторонний)')
    elif q == w or w == e or e == q and q != 0 and w != 0 and e != 0:
        print('Isosceles triangle (равнобедренный)')
    elif q != w and w != e and e != q and q != 0 and w != 0 and e != 0:
        print('Versatile triangle (разносторонний)')
    elif q == 0 or w == 0 or e == 0:
        print('не треугольник (Not a triangle)')


q = float(input('enter num1 '))
w = float(input('enter num2 '))
e = float(input('enter num3 '))
type_of_triangle(q, w, e)


def distance(x1, x2, y1, y2):
    point_a = x1 - x2
    point_b = y1 - y2
    print('Point A is', point_a, 'Point B is', point_b, end='')

x1 = int(input('enter x1 '))
x2 = int(input('enter x2 '))
y1 = int(input('enter y1 '))
y2 = int(input('enter y2 '))
distance(x1, x2, y1, y2)

