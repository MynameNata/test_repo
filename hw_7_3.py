try:
    f = open('test2.txt', 'rt', encoding='utf-8')
except ValueError:
    print('it is text')
else:
    for line in f:
        g = int(line)
        print('I did it')
finally:
    f.close()