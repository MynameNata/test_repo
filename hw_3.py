from math import sqrt

s = str(input("Enter row "))
print(s[2])
print(s[-2])
print(s[0:6])
print(s[0:-2])
print(s[1::2])
print(s[0::2])
print(s[::-1])
print(s[-1::-2])
print(s[-2:0:-1])
print(len(s))

s_2 = str(input("Enter row "))
if len(s_2) % 2 == 0:
    a = s_2[0:len(s_2)//2]
    b = s_2[len(s_2)//2:]
    print(a + ' ' + b)
elif len(s_2) % 2 == 1:
    a = s_2[0:len(s_2) // 2]
    b = s_2[len(s_2) // 2:]
    a, b = b, a
    print(a + ' ' + b)
year = int(input("enter year "))
if year % 4 == 0 or year % 400 == 0 and year % 100 == 1:
    print('Yes')
else:
    print('No')

a= int
b= int
c=0
if a == 0 or b == 0 or c == 0:
    print('No')
else:
    print('Yes')

a = int(input('first num '))
b = int(input('second num '))
c = int(input('one more num '))
if (a>b):
    a,b = b,a
if (b>c):
    b,c = c,b
if (a>b):
    a,b = b,a
print(a,b,c)

d = int(input("first "))
e = int(input("second "))
r = int(input("one more "))
if d == e == r:
    print("3")
elif d == e or d == r or e==r:
    print('2')
elif d != e and d != r and e!= r:
    print("0")

x= 0
while x <= 10:
    print(x)
    x += 1

y = 20
while y >= 1:
    print(y, end = ' ')
    y -= 1

num_a = int(input("enter number "))
res=[]
while num_a % 2 == 0:
    num_a /= 2
    res.append(num_a//2)
print(len(res))

li_2 = [1, 33.33, 'abc', 123, [6,7,8]]
while len(li_2) >0:
     print(li_2)
     li_2.pop(0)

s_4 = 'hello world'
while len(s_4)>0:
    print(s_4)
    s_4  = s_4[1::]


def find_gip(a,b):
    print(sqrt(a**2 + b**2))

find_gip(3, 4)
find_gip(4, 4)
find_gip(1, 2)

string_1 = "We are not what we should be! We are not what we need to be. But at least we are not what we used to be"
print(string_1)
print(len(string_1.split(' ')))
s = string_1.split(' ')
s.sort()
print(s)















