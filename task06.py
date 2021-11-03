arg1=input('Введите первое число:\n')
arg2=input('Введите второе число:\n')
if arg1.isdigit() and arg2.isdigit():
    arg1 = int(arg1)
    arg2 = int(arg2)
    while (arg1 - arg2) != 0:
        if arg1 > arg2:
            arg1 = arg1 - arg2
        else:
            arg2 = arg2 - arg1
    print(arg1)
else:
    print("НЕ КОРРЕКТНЫЙ ВВОД ВХОДНЫХ ДАННЫХ")

