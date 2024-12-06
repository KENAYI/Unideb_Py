with open('test.txt') as file:
    for line in file:
        print(line.strip())

with open('out.txt', 'w') as file:
    file.write('plum\n')
    file.writelines(['pear\n', 'tangerine\n'])
print('----------------')
with open('out.txt') as file:
    for line in file:
        print(line.strip())