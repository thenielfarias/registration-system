def readInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERROR! Enter a valid option.\033[m')
        else:
            return n


def line(size=40):
    return '-' * size


def header(txt):
    print(line())
    print(txt.center(40))
    print(line())


def menu(lst):
    header('MAIN MENU')
    c=1
    for i in lst:
        print(f'{c}) \033[36m{i}\033[m')
        c+=1
    print(line())
    opt = readInt(f'\033[33mEnter your option: \033[m')
    return opt


