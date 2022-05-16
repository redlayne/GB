import time

# 6.1 ----------------------------

class TrafficLight:
    __colors__ = ['Red', 'Yellow', 'Green']
    __delays__ = [4, 2, 4] #в тз другие значения задержек, но неудобно же ждать 7 секунд

    def run(self):
        for i in range (3):
            for j in range (TrafficLight.__delays__[i]):
                print (f'====[ (({TrafficLight.__delays__[i]-j} {TrafficLight.__colors__[i]:^9} {TrafficLight.__delays__[i]-j})) ]====', end='')
                time.sleep(1)
                print(end='\r')
                print(f'====[ ((  {TrafficLight.__colors__[i]:^9}  )) ]====', end='')
                time.sleep(0.3) #меньше 0.3 постоянно отрабатывает криво
                print(end='\r')

    def workcycle(self, iterations):
        self.iter = iterations
        for i in range(self.iter):
            TrafficLight.run(self)

light1 = TrafficLight()
light1.workcycle(int(input('How many cycles? (but not too much, please)')))

input('\n\nPress Enter to continue...')
print('-'*20, '\n')

# 6.2 ----------------------------

class Road:
    _length_ = 0  # по идее можно не указывать конкретных значений в атрибутах класса, только тип
    _width_ = 0  # т.к. у каждого экземпляра будут свои значения, но можно и указать как умолчальные значения
    _consumption_ = 25  #кг асфальта на квадратный метр

    def __init__(self, l, w):
        self._length_ = l
        self._width_ = w

    def area (self):
        return self._length_ * self._width_

    def tonsfor1cm(self):
        return self._length_ * self._width_ * Road._consumption_/1000


length = int(input('Road length (m)?'))
width = int(input('Road width? (m)'))
thickness = int(input('Thickness of asphalt? (cm)'))

road66 = Road(length, width)
print(f'\nArea of your road is {road66.area()} m\u00b2')
print(f'You need {road66.tonsfor1cm()*thickness} tons of asphalt')

input('\nPress Enter to continue...')
print('-'*20, '\n')

# 6.3 ----------------------------

# логика предлагаемой структуры не очень понятна
# зачем нужен класс Должность, если все данные уже есть у Работника, в т ч название должности
# и к Должности никакие параметры не привязываются
# но тз есть тз

class Worker:
    name = 'Default'
    surname = str
    position = str
    _income_ = {'wage': 20, 'bonus': 10}


class Position(Worker):

    def getfullname(self):
        return self.name+' '+self.surname

    def setincome(self, w, b):  # абсолютно неясно почему не работает objectname._income_['wage'] = 1234. Применяется к атрубуту класса, а не объекта!
        self.w = w
        self.b = b
        self._income_ = {}  # понял, что причина в отсутствии вот этой строки, но почему? ведь в описании класса оно уже определено.
        self._income_['wage'], self._income_['bonus'] = w, b

    def getincome(self):
        return int(self._income_['wage']+self._income_['bonus'])


employee1 = Position()
employee1.name, employee1.surname, employee1.position = 'Vasya', 'Shvabrin', 'Cleaner'
employee1.setincome(15000, 1000)

employee2 = Position()
employee2.name, employee2.surname, employee2.position = 'Ibragim', 'Kandiboberovich', 'Memologist'
employee2.setincome(9000, 69)

employee3 = Position()
employee3.name, employee3.surname, employee3.position = 'Aristarkh', 'Glavnov', 'Director'
employee3.setincome(500, 100000)

employee4 = Position()
employee4.name, employee4.surname, employee4.position = 'Ivan', 'Ivanov', 'Token'

personell = [employee1, employee2, employee3, employee4]

for i in range(len(personell)):
    print(f'{personell[i].position} {personell[i].getfullname()} has income {personell[i].getincome()} RUR' )

input('\nPress Enter to continue...')
print('-'*20, '\n')

# 6.4 ----------------------------

class Car():
    speed = 0
    color = str
    name = str
    is_police = False

    def __init__(self):
        if self.is_police == True:
            print(f'\nPolice car. Flashing lights are on')

    def go(self, speed):
        self.speed = speed
        print('Car goes')

    def stop(self):
        self.speed = 0
        print('Car stops')

    def turn(self, direction):
        self.dir = direction
        if self.dir != 'left' and self.dir != 'right':
            print(f'No such direction - \"{self.dir}\"')
        else:
            print(f'Car turns {self.dir}')

    def showspeed(self):
        print(f'Speed is {self.speed} km/h')

class Towncar(Car):
    is_police = False

    def showspeed(self):
        print(f'Speed is {self.speed} km/h')
        if self.speed > 60:
            print('Speed is over a limit. Get a ticket')

class Sportcar(Car):
    is_police = False

class Workcar(Car):
    is_police = False

    def showspeed(self):
        print(f'Speed is {self.speed} km/h')
        if self.speed > 40:
            print('Speed is over a limit. Get a ticket')

class Policecar(Car):
    is_police = True


Brokenlada = Car()
print(f'Pushed our car')
Brokenlada.go(5)
Brokenlada.turn('left')
Brokenlada.turn('up')
Brokenlada.turn('right')
Brokenlada.showspeed()
Brokenlada.stop()
Brokenlada.showspeed()

ferrari = Sportcar()
ferrari.name = 'Ferrari'
print(f'\nStart {ferrari.name} car')
ferrari.go(180)
ferrari.showspeed()

opel = Towncar()
opel.name = 'Opel'
print(f'\nStart {opel.name} car')
opel.go(220)
opel.showspeed()

ford = Policecar()
ford.go(90)
ford.turn('right')
ford.showspeed()

forklift = Workcar()
print(f'\nStart forklift')
forklift.go(41)
forklift.showspeed()
forklift.stop()
forklift.showspeed()

input('\nPress Enter to continue...')
print('-'*20, '\n')

# 6.5 ----------------------------

class Stationery:
    title = str

    def draw(self):
        print('Start drawing')


class Pen(Stationery):
    def draw(self):
        print('Writing a bad code')


class Pencil(Stationery):
    def draw(self):
        print('Drawing a cat =^..^=')


class Highlighter(Stationery):
    def draw(self):
        print('Let\'s highlight some text')


someitem = Stationery()
parker = Pen()
koh_i_noor = Pencil()
faber_castell = Highlighter()

someitem.draw()
parker.draw()
koh_i_noor.draw()
faber_castell.draw()

input('\nPress Enter to continue...')
print('-'*20, '\n')



