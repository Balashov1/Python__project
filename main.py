# 13 - Исключения (Конструкция try - except)

x = int(input())
y = int(input())

try:
    res = x / y
except ZeroDivisionError:
    print("Вы ввели нуль")
    res = 0
print(res)

try:
    x = int(input())
except ValueError:
    print("Вы ввели не число!!!")
    x = 0
print(x)

try:
    x = int(input())
except ValueError:
    print("Вы ввели не число")
    x = 0
try:
    y = int(input())
except ValueError:
    print("Вы ввели не число")
    y = 0
else:
    print("OK")
finally:
    print("OK--100%")

try:
    res = x / y
except ZeroDivisionError:
    print("Вы ввели нуль")
    res = 0
print(res)