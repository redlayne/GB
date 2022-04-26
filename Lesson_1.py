
# Задание 1.1

answer = input('Дружок, ты устал?')

if answer == 'да':
    children = input('Дети есть?')
    job = int(input('А сколько у тебя работ?'))
    sleep = int(input('А сколько часов ты сегодня спал?'))
    if children == 'да' and job > 1 and sleep < 6:
        print('Понимаю тебя, сходи отдохни, дорогой')
    else:
        print('Ты врешь')
        if children != 'да':
            print('У тебя же нет детей, какая еще усталость?')
        elif job == 1:
            print('Всего одна работа? Ты точно не устал!')
        elif job < 1:
            print('Ты же безработный! Ты точно не устал!')
        elif sleep >= 6:
            print('Ты выспался! На тебе пахать можно!')
        else:
            print('error') #чек на всякий случай
        print('Хватит бездельничать')
else:
    print('Врешь небось. Ну ладно.')

print('_'*50)

# Задание 1.2

sec = int(input('Сколько секунд?'))
hour = sec//3600
if hour != 0:
    sec = sec - hour*3600
min = sec//60
if min != 0:
    sec = sec - min*60
print(f'Результат: {hour}:{min}:{sec}')

print('_'*50)

# Задание 1.3

userinput = (input('Напиши число'))
num1 = int(userinput)
num2 = int(userinput*2)
num3 = int(userinput*3)
print(f'{num1} + {num2} + {num3} =', num1+num2+num3)

print('_'*50)

# Задание 1.4

num = int(input('Напиши число'))
last = num % 10
largest = last
while num !=0:
    num = num // 10
    last = num % 10
    if last > largest:
        largest = last

print('самая большая цифра', largest)

print('_'*50)

# Задание 1.5 + 1.6

income = int(input('Сколько денег заработал?'))
costs = int(input('Сколько денег потратил?'))
profit = income - costs
if profit > 0:
    print('Твоя прибыль составила', profit, ',молодец!')
    print(f'Рентабельность составила {int(profit/income*100)}%')
    empl = int(input('А сколько у тебя сотрудников?'))
    print(f'Прибыль на одного сотрудника {profit / empl}. Маловато. Уволь кого-нибудь.')
elif profit == 0:
    print('Так дело не пойдет, на', profit, 'ты себе ничего не купишь')
else:
    print('Твои убытки составили', 0-profit,'Надо что-то менять!')

print('_' * 50)


