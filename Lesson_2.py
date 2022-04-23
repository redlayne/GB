# 2.1

somelist = ['qwerty', 123, 78.9, [0, 1], (2, 3), {'name': 4, 'age': 5}]

print(somelist)
for i in somelist:
    print(type(i))

print('_'*50)

# 2.2

somemorelist = list()
listsize = int(input('How much elements? '))

for i in range(listsize):
    somemorelist.append(input(f'Element number {i+1} value?'))

reverselist = somemorelist.copy()
for j in range(listsize//2):
    reverselist[j*2], reverselist[j*2+1] = reverselist[j*2+1], reverselist[j*2]

print('before:', somemorelist)
print('after:', reverselist)

print('_' * 50)

# 2.3

monthdata = {'Winter': [1, 2, 12], 'Spring': [3, 4, 5], 'Summer': [6, 7, 8], 'Autumn': [9, 10, 11]}
monthnumber = int(input('Month number?'))  # надо бы проверить, что <= 12, но не будем

for i in monthdata:
    if monthnumber in monthdata[i]:
        print(f'{monthnumber} is {i}')

# 2.3.2

allmonths = ['Winter', 'Winter', 'Spring', 'Spring', 'Spring', 'Summer', 'Summer', 'Summer', 'Autumn', 'Autumn', 'Autumn', 'Winter']
# не самое красивое решение, но зато через list
monthnumber2 = int(input('Month number?'))
print(f'{monthnumber2} is {allmonths[monthnumber2-1]}')

print('_'*50)

# 2.4

longread = input('Tell me everything!').split(' ')

for num, fragment in enumerate(longread, 1):
    print(f'{num}) {fragment[:10]}')

# или так
# for i in range(len(longread)):
#   print(f'{i+1}) {longread[i][:10]}')

print('_' * 50)

# 2.5

hardlist = [9, 9, 7, 8, 6, 6, 5, 2, 0]
print(f'Old rating list {hardlist}')
value = int(input('New rating element?'))

for i, element in reversed(list(enumerate(hardlist))):
     if value <= element:
         hardlist.insert(i+1, value)
         break

print(f'New rating list {hardlist}')

print('_' * 50)

# 2.6

mainbase = list()

productsnumber = int(input('How much products do we have?'))

id = 1
while id <= productsnumber:
    product = dict()  # если определить этот словарь снаружи цикла - ничего не работает. Почему?
    product['Name'] = input(f'ID {id} product name?')
    product['Price'] = int(input(f'ID {id} product price?'))
    product['Qty'] = int(input(f'ID {id} product quantity?'))
    product['Unit'] = input(f'Id {id} product units?')
    mainbase.append(tuple([id, product]))

    if id < productsnumber:
        print('-'*10, 'next product', '-'*10)
    else:
        print('')
        print('-'*10, 'Main base', '-'*10)

    id += 1

print(mainbase)

result = dict()
names = []
prices = []
qtys = []
units = []

for index in range(productsnumber):
    if mainbase[index][1]['Name'] not in names:
        names.append(mainbase[index][1]['Name'])

    if mainbase[index][1]['Price'] not in prices:
        prices.append(mainbase[index][1]['Price'])

    if mainbase[index][1]['Qty'] not in qtys:
        qtys.append(mainbase[index][1]['Qty'])

    if mainbase[index][1]['Unit'] not in units:
        units.append(mainbase[index][1]['Unit'])

result = {'Name': names, 'Price': prices, 'Qty': qtys, 'Unit': units}
print('-'*10, 'Analytics', '-'*10)
print('All names: ', result['Name'])  # почему-то тут не получились f-строки
print('All prices: ', result['Price'])
print('All quantities: ', result['Qty'])
print('All units: ', result['Unit'])