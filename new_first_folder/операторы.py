#1 Площадь треугольника
a = int(input()) # введите значение A
b = int(input()) # введите значение B
c = int(input()) # введите значение C
p = (a + b + c) / 2
s = (p * (p - a) * (p - b) * (p - c)) ** (1/2)
print(s)

#2 поиск в заданном интервале
a = int(input()) # введите значение A
if (-15 < a <= 12 or 14 < a < 17 or 19 <= a < float('inf')):
    print('True')
else:
    print('False')

#3 Калькулятор
a = float(input()) # введите значение A
b = float(input()) # введите значение B
c = input() # введите значение C
if c == '+' :
    print(a + b)
elif c == '-' :
    print(a - b)
if c == '/' :
    if b == 0 or b == 0.0:
        print('Деление на 0!')
    else:
        print(a / b)
elif c == '*' :
        print(a * b)
elif c == 'pow' :
        print(a ** b)
elif c == 'div' :
    if b == 0 or b == 0.0:
        print('Деление на 0!')
    else:
        print(a // b)
elif c == 'mod' :
    if b == 0 or b == 0.0:
        print('Деление на 0!')
    else:
        print(a % b)

#4 Кпространство комнат
H = input()

if H == 'треугольник':
    a = int(input())
    b = int(input())
    c = int(input())
    p = (a + b + c) / 2
    result = (p * (p - a) * (p - b) * (p - c)) ** (1 / 2)

elif H == 'прямоугольник':
    a = int(input())
    b = int(input())
    result = (a * b)

elif H == 'круг':
    a = int(input())
    result = (3.14 * a ** 2)

print(float(result))

#5 Максимум и минимум
a = int(input())
b = int(input())
c = int(input())
if a >= c >=b:
    print(a)
    print(b)
    print(c)
elif a >= b >= c:
    print(a)
    print(c)
    print(b)
elif a <= b <= c:
    print(c)
    print(a)
    print(b)
elif c >= a >= b:
    print(c)
    print(b)
    print(a)
elif b >= c >= a:
    print(b)
    print(a)
    print(c)
elif b >= a >= c:
    print(b)
    print(c)
    print(a)

#6 Склонение програмистов
a = 'программист'
b = 'программиста'
c = 'программистов'
x = int(input())
v = x % 10
m = x % 100
if x == 1 or v == 1:
    if m == 11 or x == 11:
        print(x, c)
    else:
        print(x, a)
elif v == 2 or v == 3 or v == 4:
    if 12 <= x <= 20 or 12 <= m <= 20:
        print(x, c)
    else:
        print(x, b)
else:
    print(x, c)


#7 Счастливый билет
x = int(input()) # вводим номер билета
a = x // 1000
b = x % 1000
q = a // 100
w = (a // 10) % 10
e = a % 10
r = b // 100
t = (b // 10) % 10
y = b % 10
if (q + w + e) != (r + t + y):
    print('Обычный')
else:
    print('Счастливый')