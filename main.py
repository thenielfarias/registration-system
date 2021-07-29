from lib.interface import *
from lib.file import *
from time import sleep

file = 'registrations.txt'

if not fileFound(file):
    createFile(file)

while True:
    r = menu(['View registration list', 'New registration', 'Exit'])
    if r == 1:
        readFile(file)
    elif r == 2:
        header('NEW REGISTRATION')
        name = str(input('Name: '))
        age = readInt('Age: ')
        register(file, name, age)
    elif r == 3:
        print('Program ended.')
        break
    else:
        print('\033[31mERROR! Option does not exist.\033[m')
    sleep(2)


