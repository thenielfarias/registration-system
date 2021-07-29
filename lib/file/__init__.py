def fileFound(name):
    try:
        f = open(name, 'rt')
        f.close()
    except FileNotFoundError:
        return False
    else:
        return True
    

def createFile(name):
    try:
        f = open(name, 'wt+')
        f.close()
    except:
       print('An error occurred creating the file.')
    else:
        print(f'{name} successfully created')        


def readFile(name):
    try:
        f = open(name, 'rt')
    except:
        print('An error occurred reading the file.')
    else:
        print('- REGISTRATION LIST')
        for l in f:
            data = l.split(';')
            data[1] = data[1].replace('\n', '')
            print(f'{data[0]:<30}{data[1]:>3} anos')
    finally:
        f.close()


def register(file, name='unknown', age=0):
    try:
        f = open(file, 'at')
    except:
        print('An error occurred opening the file.')
    else:
        try:
            f.write(f'{name};{age}\n')
        except:
            print('An error occurred writing the file.')
        else:
            print(f'New registration of {name} added.')
            f.close()


