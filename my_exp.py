def logic_swap(a,b):
    if (a>b):
        a,b = b,a
    return a,b

# a = int(input('first num '))
# b = int(input('second num '))
# c = int(input('one more num '))
#
# a,b = logic_swap(a,b)
# b,c = logic_swap(b,c)
# a,b = logic_swap(a,b)
# print(a,b,c)

apiUrl = "http://zuzo.com?&id={MYSUPERID}paid=false"
apiUrls = map(lambda x : apiUrl+str(x),  ["a","b","c"]+list(range(10)))   # Преобразую 1 2 3 4 5 6 7 8 9 0 в  =>  СТРОКУ С числом
print(list(apiUrls))

# a = 3
# b = 6
# c = 1
#
# demoList = [a,b,c]
# demoList.sort()
# print(demoList)


newList = map(lambda x: [x,x*-1], demoList)
newList = filter(lambda  x: x % 2 ==0,newList)
print(list(newList))


# li_2 = [1, 33.33, 'abc', 123, [6,7,8]]
#
#  for i in range(len(li_2)):
#      print (li_2[0::])
#      li_2= li_2[1::]


# lis_6 = [1, 9, 5, 1, 9, 0]
# for i in range(len(lis_6)-1):
#     if lis_6[i]==lis_6[i+1]:
#         print(i)