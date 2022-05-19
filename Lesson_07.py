import random
from abc import ABC, abstractmethod

# 7.1 ----------------------------

class Matrix():

    def __init__(self, m, n):
        self.matrixcontent = []  # почему это не работает, если делать его атрибутом класса
        self.m = m
        self.n = n

        # можно создавать всё вручную, но это тааак долго
        for i in range(self.m):
            column = []
            for j in range(self.n):
                column.append(random.randint(-99, 99))
            self.matrixcontent.append(column)

    def __str__(self):
        resultstring = ''
        for i in range(self.n):
            resultstring += '| '
            for j in range(self.m):
                resultstring += f'{self.matrixcontent[j][i]:^5}'
            resultstring += ' |\n'
            if i < self.n-1:
                resultstring += f'|'
                resultstring +=' '*(self.m*5+2)
                resultstring +='|\n'
        return resultstring

    def __add__(self, other):
        additionresult = Matrix(other.m, other.n)
        # по идее можем просто делать список списков, но нам же надо вернуть объект типа Matrix
        for i in range(self.m):
            for j in range(self.n):
                additionresult.matrixcontent[i][j] = self.matrixcontent[i][j] + other.matrixcontent[i][j]
        return additionresult


m = int(input('Columns quantity?'))
if m > 10:
    print('Too much. Let\'s take 10')
    m = 10
n = int(input('Rows quantity?'))
if n > 10:
    print('Too much. Let\'s take 10')
    n = 10
print('')

neo = Matrix(m,n)
print('You take the blue pill...\nMatrix was just created\n')
print(neo)

trinity = Matrix(m,n)
print('You take the red pill...\nMatrix was just created\n')
print(trinity)

morpheus = neo + trinity
print('Wake up, Neo. The Matrix has you...\nHere is your sum\n')
print(morpheus)

input('\nPress Enter to continue...')
print('-'*20, '\n')

# 7.2 ----------------------------

class Clothes(ABC):

    @abstractmethod
    def fabricconsumption (self, size):
        pass


class Coat(Clothes):
    sizelist = [46, 48, 50, 52, 54, 56]

    def __init__(self, size=46):
        self.size = size

    def fabricconsumption(self):
        fabric = self.size / 6.5 + 0.5  # адский расход! по 9 метров на пальто!
        return round(fabric, 1)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if size not in self.sizelist:
            self.__size = min(self.sizelist, key=lambda el: abs(el - size))
            print(f'Closest size is {self.__size}')
        else:
            self.__size = size


class Suit(Clothes):
    sizelist = [152, 158, 164, 170, 176, 182]

    def __init__(self, size=152):
        self.size = size

    def fabricconsumption(self):
        fabric = self.size * 0.02 + 0.3
        return round(fabric, 1)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if size not in self.sizelist:
            self.__size = min(self.sizelist, key=lambda el: abs(el - size))
            print(f'Closest height is {self.__size}')
        else:
            self.__size = size


coatsize = int(input('Coat size?'))
redcoat = Coat(coatsize)
print(f'You need {redcoat.fabricconsumption()} m of fabric\n')

suitsize = int(input('Suit height?'))
blacksuit = Suit(suitsize)
print(f'You need {blacksuit.fabricconsumption()} m of fabric\n')

input('\nPress Enter to continue...')
print('-'*20, '\n')

# 7.3 ----------------------------

class Infusoria():

    def __init__(self, cellsnum):
        self.cellsnum = cellsnum


    def __add__(self, other):
        newcellnum = self.cellsnum + other.cellsnum
        return Infusoria(newcellnum)

    def __sub__(self, other):
        if self.cellsnum > other.cellsnum:
            newcellnum = self.cellsnum - other.cellsnum
            return Infusoria(newcellnum)
        else:
            print('Can\'t subtract. Infusoria is dead\n')
            return Infusoria(0)
            # можно возвращать None например. Или продумать логику удаления объекта если этот параметр 0
            # но я не разобрался как. Попробовал в конструкторе что-то типа
            # if self.cellsnum == 0: del self. Но так не работает

    def __mul__(self, other):
        newcellnum = self.cellsnum * other.cellsnum
        return Infusoria(newcellnum)

    def __truediv__(self, other):
        newcellnum = self.cellsnum // other.cellsnum
        return Infusoria(newcellnum)

    def make_order(self, cellsinrow):
        self.cellsinrow = cellsinrow
        rows = self.cellsnum // self.cellsinrow
        remain = self.cellsnum % self.cellsinrow
        neworder = ''
        for i in range(rows):
            neworder += '*'*self.cellsinrow+'\n'
        neworder += '*'*remain+'\n'
        return neworder

infu1 = Infusoria(20)
print('Infusoria of 20 cells in order 5')
print(infu1.make_order(5))

infu2 = Infusoria(15)
print('Infusoria of 15 cells in order 6')
print(infu2.make_order(6))

infu3 = infu1 + infu2
print(f'Infusoria of {infu3.cellsnum} cells in order 10')
print(infu3.make_order(10))

infu4 = infu2 - infu1

infu5 = infu1 - infu2
print(f'Infusoria of {infu5.cellsnum} cells in order 7')
print(infu5.make_order(7))

infu6 = infu3 / infu2
print(f'Infusoria of {infu6.cellsnum} cells in order 1')
print(infu6.make_order(1))

infu7 = infu1*infu2
print(f'Infusoria of {infu7.cellsnum} cells in order 70')
print(infu7.make_order(70))

input('\nPress Enter to continue...')
print('-'*20, '\n')




