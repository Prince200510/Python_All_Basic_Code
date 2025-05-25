with open('output.txt', 'w') as file:
    file.write('Prince Maurya')

with open('output.txt', 'r') as file:
    data = file.read()
    print(data)

with open('output.txt', 'a') as file:
    file.write('\n')
    file.write('Python 1 to 100 Interviews codes')

with open('output.txt', 'r') as file:
    data = file.read()
    print(data)