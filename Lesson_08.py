from random import randint
import time

# 8.1 ----------------------------

# сначала задача кажется простой, а потом ты тратишь на нее 4 часа

class Date():
    monthlist = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    def __init__(self, date_str):
        self.day, self.month, self.year = Date.date_to_int(date_str)

    @staticmethod
    def valid(obj):
        valid = True

        if (obj.year % 4 == 0 and obj.year % 100 != 0) or (obj.year % 400 == 0):
            yeartype = 'leap_year'
            print('It\'s a leap year')
        else:
            yeartype = 'whatever'  # не обязательно, сделал для теста

        # все эти условия можно было в одну строку, но было бы нечитабельно
        if obj.day > 31 or obj.day < 1:
            print('No such day')
            valid = False

        if obj.month == 2 and ((obj.day > 29 and yeartype == 'leap_year') or (obj.day > 28 and yeartype != 'leap_year')):
            print(f'No such day in February in year {obj.year}')
            valid = False

        if obj.day == 31 and obj.month in [4, 6, 9, 11]:
            print(f'No such day in month {obj.month}')
            valid = False

        if obj.month > 12 or obj.month < 1:
            print('No such month')
            valid = False

        if obj.year < 0:
            print('No such year')
            valid = False

        if valid == False:
            return False
        else:
            print('Date is correct')
            return True

    @staticmethod
    def print_date(obj):
        if Date.valid(obj):
            month_name = Date.monthlist[obj.month-1]
            return f'{obj.day} {month_name} {obj.year}\n'
        else:
            return ('Couldn\'t print incorrect date\n')

    @classmethod
    def date_to_int(cls, date):
        d = []
        m = []
        y = []
        d.append(date[0:date.find('-')])
        divider_position = date.find('-')
        d = int(''.join(d))
        m.append(date[divider_position+1:date.find('-', divider_position+1)])
        divider_position = date.find('-', divider_position+1)
        m = int(''.join(m))
        y.append(date[divider_position+1:])
        y = int(''.join(y))
        return d, m, y

# всевозможные примеры чтобы не мучать пользователя вводом
print('input: 13-05-2005')
date1 = Date('13-05-2005')
print(Date.print_date(date1))

print('input: 29-02-2028')
date2 = Date('29-02-2028')
print(Date.print_date(date2))

print('input: 15-35-2005')
date3 = Date('15-35-2005')
print(Date.print_date(date3))

print('input: 40-40-2005')
date4 = Date('40-40-2005')
print(Date.print_date(date4))

print('input: 29-02-2005')
date5 = Date('29-02-2005')
print(Date.print_date(date5))

print('input: 31-04-2005')
date6 = Date('31-04-2005')
print(Date.print_date(date6))

input('\nPress Enter to continue...')
print('-'*20, '\n')

# 8.2 ----------------------------

class Division_zero(Exception):
    consequences  = ['Your computer is vroken now!', 'You lose all your money.', 'Your wife left you with mathematician.', 'Asteroid will hit Earth in 10 minutes.']
    def __init__(self, error_message):
        self.error_message = error_message

divisible = int(input('Divisible?'))

try:
    divisor = int(input('Divisor'))
    if divisor == 0:
        raise Division_zero(f'You divided by zero. {Division_zero.consequences[randint(0,3)]}')
except Division_zero as err:
    print(err)
else:
    print(f'{divisible} / {divisor} = {divisible/divisor}\nYou did well this time. Now hear the words of wisdom...')
finally:
    print('Never divide by zero. Never! It will end badly for you... Believe me.')

input('\nPress Enter to continue...')
print('-'*20, '\n')

# 8.3 ----------------------------

class Not_number(Exception):

    def __init__(self, error_message):
        self.error_message = error_message

main_list = []

print('Input some numbers. No string allowed! Promise?..')
print('Print \"stop\" to stop. Isn\'t that logical?')
while True:
    user_input = input('List element?')
    if user_input == 'stop':
        break
    try:
        if user_input.isdigit():
            main_list.append(user_input)
        else:
            raise Not_number(f'{user_input} is not a number! Try again.')
    except Not_number as err:
        print(err)

print(f'\nHere is your list:\n{main_list}')

input('\nPress Enter to continue...')
print('-'*20, '\n')

# 8.4-6 ----------------------------

'''
склад техники с несколькими локациями складов, покупкой, продажей и перемещениями между складами
'''
# амбиции были - как минимум переплюнуть "1С - Предприятие"
# но после недели продумывания структуры пришлось вспомнить, что пример учебный и принять условности

def money_to(money):  # анимация продажи товара
    for i in range(1,7):
        print(chr(127978), end='')
        print(' ' * i, end='')
        print(chr(127873), end='')
        print(' ' * (7 - i), end='')
        print(chr(127968), end='')
        time.sleep(0.3)
        print(end='\r')
    for i in range(1, 7):
        print(chr(127978), end='')
        print(' ' * (7 - i), end='')
        print(chr(128176), end='')
        print(' ' * i, end='')
        print(chr(127968), end='')
        time.sleep(0.3)
        print(end='\r')
    print(f'{chr(127978)} +{money}$\n')


def money_from(money):  # анимация закупки товара
    for i in range(1 , 7):
        print(chr(127978), end='')
        print(' ' * i, end='')
        print(chr(128176), end='')
        print(' ' * (7 - i), end='')
        print(chr(127981), end='')
        time.sleep(0.3)
        print(end='\r')
    for i in range(1, 7):
        print(chr(127978), end='')
        print(' ' * (7 - i), end='')
        print(chr(128674), end='')
        print(' ' * i, end='')
        print(chr(127981), end='')
        time.sleep(0.3)
        print(end='\r')
    print(f'{chr(127978)} -{money}$\n')


def go_repair(discount):  # анимация отправки в сервис
    for i in range(1 , 7):
        print(chr(127978), end='')
        print(' ' * i, end='')
        print(chr(128176), end='')
        print(' ' * (7 - i), end='')
        print(chr(128736), end='')
        time.sleep(0.3)
        print(end='\r')
    print(f'{chr(127978)} Discount {discount}%\n')

def random_item():  # создание случайного товара
    templist = []
    templist.append(Item.category_list[randint(0, 2)])
    templist.append(Item.brand_list[randint(0, 2)])
    templist.append(Item.spec_list[randint(0, 5)])
    templist.append(randint(5, 10)*10)
    return templist

def manual_item():  # создание товара вручную
    templist = []
    templist.append(input('Category?'))
    templist.append(input('Brand?'))
    templist.append(input('Specification?'))
    while True:
        try:
            templist.append(int(input('Price?')))
            break
        except ValueError:
            print('Numbers only!')
    return templist

class Warehouse:
    def __init__(self, capacity):  # у склада есть вместительность (в штуках товара)
        self.capacity = capacity
        self.storage = [0 for i in range(capacity)]  # 0 - свободная полка на складе

    def show_content(self):  # визуализация занятости мест на складе
        templist = ['_' if self.storage[i] == 0 else chr(11197) for i in range(self.capacity)]
        return '[ '+' '.join(templist)+' ]'

    def show_items(self):  # показывает сдержимое подробно
        for i in range(self.capacity):
            print (f'{i+1}.')
            if self.storage[i] == 0:
                print('Empty place')
            else:
                print(self.storage[i], '\n')


    def move_item(self, pos, destination_obj):  # перемещение товара со склада (по номеру позиции) на другой склад (на свободное место)
        if pos > (self.capacity-1):
            print('No such position in your warehouse')
            return
        if self.storage[pos] == 0:
            print('Position is empty, nothing to move')
            return
        for i in range(destination_obj.capacity):
            if destination_obj.storage[i] == 0:
                destination_obj.storage[i] = self.storage[pos]
                self.storage[pos] = 0
                print(f'{destination_obj.storage[i].category} {destination_obj.storage[i].brand} moved')
                return
        print('No free space in the destination warehouse')
        return


class Hub(Warehouse):  # основной склад - может принимать поставки
    def shipment(self, item_obj):  # ищем свободное место на складе, грузим туда товар
        success = False
        global balance
        if item_obj.buy_price > balance:
            print('Insufficient money. Go get some more.')
            return
        for i in range(self.capacity):
            if self.storage[i] == 0:
                self.storage[i] = item_obj
                print(f'{item_obj.category} {item_obj.brand} received for {item_obj.buy_price}$')
                balance -= item_obj.buy_price
                print(f'Balance: {balance}$\n')
                success = True
                break
        if not success:
            print('No free space in the warehouse.')


class Store(Warehouse):  # магазин - может продать товар
    def sell(self, pos):
        global balance
        global vat
        global margin
        if self.storage[pos] == 0:
            print('Position is empty, nothing to move')
            return
        if self.storage[pos].discount != 0:
            income = (self.storage[pos].buy_price * margin * (100 - self.storage[pos].discount) / 100)
        else:
            income = self.storage[pos].buy_price * margin
        print(f'Item is sold for {int(income)} but {int(income * vat / 100)} goes to state. Life\'s tough')
        money_to(int(income - income * vat / 100))
        balance += int(income - income * vat / 100)
        print(f'Current balance: {balance}')


class Service(Warehouse):  # сервис - может принять сломанный товар и поставить скидку +50% после ремонта
    def repair(self, pos):
        if pos > (self.capacity-1):
            print('No such position in your warehouse')
            return
        if self.storage[pos] == 0:
            print('Position is empty, nothing to repair')
            return
        self.storage[pos].discount += 50
        if self.storage[pos].discount > 90:
            self.storage[pos].discountt = 90
        print('Item ready. Repaired items get +50% discount')
        go_repair(50)


class Item:
    category_list = ['Notebook', 'Smartphone', 'Tv']
    brand_list = ['Sony', 'Samsung', 'Xiaomi']
    spec_list = ['69k nano matrix', 'Radiation resistant', 'Bio eco panda-friendly', '99 Megawatt',
                 'Self destructing model', '666 Megapixels']

    def __init__(self, category, brand, specs, buy_price, discount=0):
        self.category = category
        self.brand = brand
        self.specs = specs
        self.buy_price = buy_price
        self.discount = discount

    @classmethod
    def set_specs(cls, spec_list):
        category, brand, specs, buy_price = spec_list[0], spec_list[1], spec_list[2], spec_list[3]
        return Item(category, brand, specs, buy_price)

    def __str__(self):
        if self.discount == 0:
            return f'{self.category} {self.brand}\n{self.specs}\nPrice: {self.buy_price} $'
        else:
            return f'{self.category} {self.brand}\n{self.specs}\nPrice: {self.buy_price} $\nDiscount: {self.discount}%'


balance = 3000  # деньги
vat = 20  # налог. Не несет серьезного значения для учебного примера, но напоминает о тщетности бытия и трудностях бизнеса
margin = 2.5  # маржинальность

# mainhub.shipment(Item.set_specs(random_item()))
# Считаю, вот классная конструкция. Можно насоздавать огромное количество объектов, не именуя их руками в скрипте
# Главное в конструкторе в объект (список) добавить элемент с уникальным номером. Вроде ID товара
# Например взять просто глобальную int переменную и добавлять единицу после каждого назначения
# А так делают вообще?? Жаль идея пришла поздно, не стал всё переписывать.

print('\nCreate main hub, store and service facilities')
mainhub = Hub(4)
eldoradio = Store(3)
wrenchers = Service(2)

print('Main hub:', mainhub.show_content())
print('Service:', wrenchers.show_content())
print('Store: ', eldoradio.show_content())

input('\nPress Enter to continue...')

item1 = Item.set_specs(random_item())
item2 = Item.set_specs(random_item())
item3 = Item.set_specs(random_item())

print('\nCreate 3 items shipment')
mainhub.shipment(item1)
mainhub.shipment(item2)
mainhub.shipment(item3)

print('\nMain hub:', mainhub.show_content())

input('\nPress Enter to continue...')

print('\nMoving item from pythonic position 1 to service, initiating repairs')
mainhub.move_item(1, wrenchers)
wrenchers.repair(0)

print('Main hub:', mainhub.show_content())
print('Service:', wrenchers.show_content())

input('\nPress Enter to continue...')

print('\nMoving items from main hub and service to store\n')
mainhub.move_item(0, eldoradio)
wrenchers.move_item(0, eldoradio)

print('Main hub:', mainhub.show_content())
print('Service:', wrenchers.show_content())
print('Store: ', eldoradio.show_content())

input('\nPress Enter to continue...')

print('\nLet\'s see what\'s in store\n')
eldoradio.show_items()

input('\nPress Enter to continue...')

print('\nNow let\'s create product manually and get it to main storage')
item4 = Item.set_specs(manual_item())
print('Well done! Now watch this awesome animation for your effort!')
money_from(item4.buy_price)
mainhub.shipment(item4)

input('\nPress Enter to continue...')

print('\nNow we move your product to store and sell the goods')
mainhub.move_item(0, eldoradio)

print('Store: ,', eldoradio.show_content(),'\n')

eldoradio.show_items()
eldoradio

for i in range(eldoradio.capacity):
    eldoradio.sell(i)

print(f'\nYou end up with {balance}$ and earn {balance-3000}$')

input('\nPress Enter to continue...')
print('-'*20, '\n')

# 8.7 ----------------------------

class Complex:

    def __init__(self, re, im):
        self.real = re
        self.imaginary = im

    def __str__(self):
        if self.imaginary > 0:
            return f'{self.real}+{self.imaginary}i'
        elif self.imaginary < 0:
            return f'{self.real}{self.imaginary}i'
        else:
            return f'{self.real}'

    def __add__(self, other):
        return Complex(self.real+other.real, self.imaginary+other.imaginary)

    def __sub__(self, other):
        return Complex(self.real-other.real, self.imaginary-other.imaginary)

    def __mul__(self, other):
        return Complex(self.real*other.real-self.imaginary*other.imaginary, self.real*other.imaginary+self.imaginary*other.real)

    def __truediv__(self, other):

        #  а как идеологически обрабатываются случаи ошибок например с делением на ноль.
        #  остановка? возврат none?
        try:
            #  более длинная запись для читаемости
            new_real = (self.real*other.real + self.imaginary*other.imaginary) / (other.real**2 + other.imaginary**2)
            new_imaginary =  (other.real*self.imaginary - self.real*other.imaginary) / (other.real**2 + other.imaginary**2)
            return Complex(new_real, new_imaginary)

        except ZeroDivisionError:
            print('Division by zero')
            return None  #  кажется, что это не очень правильно, но тут воде как не мешает дальнейшей работе скрипта

a = Complex(2,3)
b = Complex(-1,1)

print(f'{a} + ({b}) = {a+b}')
print(f'{a} - ({b}) = {a-b}')
print(f'{a} * ({b}) = {a*b}')
print(f'{a} / ({b}) = {a/b}')



