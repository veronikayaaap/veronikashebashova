



what = input( "Что делаем? (+, -, /, *): ")


a = float(input( "Введи первое число"))
b = float(input( "Введи второе число"))


if what == "+":
    c = a + b
    print("Результат: " + str(c))
elif what == "-":
    c = a - b
    print("Результат: " + str(c))
elif what == "*":
    c = a * b
    print("Результат: " + str(c))
elif what == "/":
   if b != 0:
       print(a / b)
   else:
       print( "Ошибка!")
else:
    print(" Выбрана неверная операция :(")

input()

