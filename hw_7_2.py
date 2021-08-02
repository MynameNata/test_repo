with open('test.txt', 'w', encoding='utf-8') as inFile:
    line = 'la-la-la\n' * 3
    inFile.write(line)


with open('test.txt', 'rt', encoding='utf-8') as inFile:
    for line in inFile:
        print(f"{line.rstrip()}!")


with open('hw_6.py', 'rt', encoding='utf-8') as f:
    print(f.read())


