def is_num(str):
    try:
        float(str)
        return True
    except ValueError:
        return False

arg1=input('Введите число (от 3 до 23):\n')
arg2=input('Введите число (от 3 до 23):\n')
arg3= input('Введите операцию (+, -, *, /):\n')
if is_num(arg1) and is_num(arg2) and 3<=float(arg1)<=23 and 3<=float(arg2)<=23 and arg3 in ['+', '-', '*', '/']:
    if arg3=='+':
        print(float(arg1) + float(arg2))
    elif arg3=='-':
        print(float(arg1) - float(arg2))
    elif arg3=='*':
        print(float(arg1) * float(arg2))
    else:
        print(float(arg1) / float(arg2))
else:
    print("НЕ КОРРЕКТНЫЙ ВВОД ВХОДНЫХ ДАННЫХ")

