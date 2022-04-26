# 3.1 --------------------

def mydivision (arg1, arg2):
   complete = False
   while not complete:
       try:
           res = arg1 / arg2
           complete = True
       except ZeroDivisionError:
            print('It\'s INFINITE so try again.')
            arg2 = int(input('New denominator?'))
   global garg1 #почему-то нельзя сразу объявить переменную и присвоить значение
   global garg2
   garg1 = arg1
   garg2 = arg2
   return res

res = mydivision(int(input('Numerator?')), int(input('Denominator?')))
print(f'\n{garg1} / {garg2} = {round(res,3)}')

print('-'*20)

# 3.2 ---------------------

def profile (name, surname, byear, city, email, phone):
    phonenum = []
    for n in list(phone):
        if n.isdigit():
            phonenum.append(n)
    phonenum =''.join(phonenum)

    print('\nName: {} {}\nYear of birth: {}, City:{}, Email: {}, Phone: {}'.format(name, surname, byear, city, email, phonenum))

name = input('Name?')
surname =input('Surame?')
yearcomplete = False
while not yearcomplete:
    try:
        byear = int(input('Year of birth?'))
        yearcomplete = True
    except ValueError:
        print ('You don\'t fool us! Numbers only!')
city = input('City?')
email = input('Email?')
phone = input('Phone?')

profile(name, surname, byear, city, email, phone)

print('-'*20)

# 3.3 -------------------------

def biggersum (*args): #с тремя скучно
    temp = sorted(list(args))
    res = temp[len(temp)-1] + temp[len(temp)-2]
    return res
print('Example list: (1, 2, 0, 0, 5, 7, 0, -3, 99, 1, 10')
print('Sum of biggest numbers is', biggersum(1, 2, 3, 5, 7, 7, 0, -3, 99, 1, 10))

print('-'*20)

# 3.4 ---------------------------

def negativepower (num, pwr):
    temp = num
    for i in range(1, abs(pwr)):
        temp = temp*num

    res = 1 / temp
    return round(res, 10)

num = float(input('First number?'))

if num == 0:
    print('Error. No zeroes!')
    num = float(input('Other first number?'))

pwr = int(input('Second number?'))

if pwr > 0:
    pwr = - pwr
    print('I want second number to be negative!')
    print('It will be', pwr)

print(f'\n{num}^{pwr} = {negativepower(num, pwr)}')

print('-'*20)

# 3.5 ---------------------------

def supersum ():
    global finalsum
    global stop
    mystring = input('Input numbers, n for stop')
    mystring = mystring.split()
    for i in mystring:
        if i == 'n':
            stop = True
            print('Enough already!')
            break
        finalsum = finalsum + int(i)

    return finalsum

finalsum = 0
stop = False

while not stop:
    print(f'\n{supersum()} \n')

print('-'*20)

# 3.6, 3.7---------------------------

def Capita(text):
    text = text.capitalize()
    return text

text = input('Enter a word')
print(Capita(text))

bigtext = input('Enter a text')
words = bigtext.split()

newtext = []
for word in words:
    newtext.append(Capita(word))

bigtext = ' '.join(newtext)
print(bigtext)
