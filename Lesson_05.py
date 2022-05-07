import functools
from random import randint
import json

# 5.1 -------------------

filecreated = False
counter = 0
filename = 'lesson_05'
while filecreated == False:
    try:
        filevar = open(filename+'.txt', 'x')
        filecreated = True
        print(f'File {filename}.txt created')
    except FileExistsError:
        print (f'File {filename}.txt already exists')
        filename = filename +str(counter)
        counter+=1
        #а еще тут можно создать log.txt и режиме дозаписи сохранять ошибки, но это уже слишком ))

inputline = str
while inputline != '':
    inputline = input('Input your data')
    filevar.write(inputline+'\n')
filevar.close()

with open(filename+'.txt') as text:
    print(text.read())
input('Press Enter to continue...')
print('-'*20, '\n')

# 5.2 -------------------

with open('5_2.txt', 'r') as text:
    print(text.read())
    text.seek(0)
    linescount = 0
    for el in text:
        linescount += 1
        if len(el.split()) == 1:
            print(f'in the {linescount} line {len(el.split())} word')
        else:
            print(f'in the {linescount} line {len(el.split())} words')

input('\nPress Enter to continue...')
print('-'*20, '\n')

# 5.3 -------------------

with open('5_3.txt') as filevar3:
    peoplecount = 0
    income = 0
    for el in filevar3:
        peoplecount += 1
        income += float(el.split()[1])
        if float(el.split()[1]) <= 20000:
            print(f'{el.split()[0]} has only {el.split()[1]} EUR')
    print(f'\nOverall income is {income}')
    print(f'There are {peoplecount} people')
    print(f'Average income is {income/peoplecount}')

input('\nPress Enter to continue...')
print('-'*20, '\n')

# 5.4 -------------------

translation = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open('5_4.txt', 'w', encoding='utf-8') as filevar4:
    # content = ['One — 1', 'Two — 2', 'Three — 3', 'Three — 3', 'Four — 4'] #не понял почему выдает ошибку
    # filevar4.writelines([content])
    filevar4.write('One — 1\n')
    filevar4.write('Two — 2\n')
    filevar4.write('Three — 3\n')
    filevar4.write('Four — 4\n')

with open('5_4.txt', 'r', encoding='utf-8') as filevar4:
    with open('5_4_new.txt', 'w', encoding='utf-8') as filevar4_new:
        for el in filevar4:
            newline = el.split()
            newline[0] = translation[el.split()[0]]
            filevar4_new.write(' '.join(newline)+'\n')

with open('5_4_new.txt', 'r', encoding='utf-8') as filevar4_new:
    print('file created successfully')
    print(filevar4_new.read())

input('\nPress Enter to continue...')
print('-'*20, '\n')


# 5.5 -------------------

with open('5_5.txt', 'w') as filevar5:
    for i in range (randint(3, 10)):
        filevar5.write(str(randint(-50,100))+' ')

with open('5_5.txt', 'r') as filevar5:
    filestr = filevar5.readline()
    sum = 0
    for i in filestr.split():
        sum += int(i)
    print(filestr)
    print(f'Sum is {sum}')

input('\nPress Enter to continue...')
print('-'*20, '\n')

# 5.6 -------------------

disciplines = []
hours = []

with open('5_6.txt') as filevar6:
    for el in filevar6:
        disciplines.append(el[0:el.find(':')]) #название предмета до двоеточия записали в список
        hourstemp = []
        discipline = 0
        for i in range(len(el)):
            if el[i].isdigit():
                hourstemp.append(el[i])
            if el[i] == '(':
                disciplinetemp = int(''.join(hourstemp))
                hourstemp = []
                discipline += disciplinetemp
        hours.append(discipline)

result = {disciplines[i]:hours[i] for i in range(len(disciplines))}
print(result) #боже, оно работает

input('\nPress Enter to continue...')
print('-'*20, '\n')

# 5.7 -------------------

with open('5_7.txt', 'w') as filevar7:
    firmsquantity = int(input('How much companies?')) #здесь надо конечно ограничить количество и проверять на ValueError
    for i in range(1, firmsquantity+1):
        profile = []
        profile.append(input(f'Company {i} name?'))
        profile.append(input(f'Company {i} form of ownership?'))
        profile.append(input(f'Company {i} income?')) #здесь конечно надо либо проверять на ошибку при переводе в int
        profile.append(input(f'Company {i} costs?')) #либо проверять условие функцией isdigit. Но сил нет :)
        filevar7.write(' '.join(profile)+'\n')
print('\n')

with open('5_7.txt') as filevar7:
    profitlist = [] #service value
    averageprofits = {}
    companies = {}
    database = []
    for el in filevar7:
        company = el.split()
        print(f'Company {company[0]} profit is {int(company[2])-int(company[3])}')
        companies [company[0]] = int(company[2])-int(company[3])
        if int(company[2])-int(company[3]) > 0:
            profitlist.append(int(company[2])-int(company[3]))

    averageprofits['Average profit'] = functools.reduce(lambda a, b: a+b, profitlist) / len(profitlist)

    database.append(companies)
    database.append(averageprofits)

with open("database.json", "w") as data:
    json.dump(database, data)

print('Great success! Json created!')

input('\nPress Enter to continue...')
print('-'*20, '\n')






