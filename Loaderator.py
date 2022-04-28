# забабахал шикарные лоадеры!

import time

def loader1():
    for i in range (3):
        print('Loading', end='')
        for i in range(5):
            time.sleep(0.3)
            print('.', end='')
        print(end='\r')
    print('Bad code ready\n')

def loader2():
    for i in range(12):
        print('Loading [', end='')
        print('|'*i+' '*(11-i)+']', end='')
        time.sleep(0.3)
        print(end='\r')
    print('Errors ready\n')

def loader3():
    for i in range (4):
        print('Loading |', end='')
        time.sleep(0.3)
        print(end='\r')
        print('Loading '+chr(92), end='')
        time.sleep(0.3)
        print(end='\r')
        print('Loading --', end='')
        time.sleep(0.3)
        print(end='\r')
        print('Loading /', end='')
        time.sleep(0.3)
        print(end='\r')
    print('Cat coder go coding! ~(=^‥^)')

