arg1=float(input('Введите число (от 3 до 23):\n'))
arg2=float(input('Введите число (от 3 до 23):\n'))
arg3= input('Введите операцию (+, -, *, /):\n')
if 3<=arg1<=23 and 3<=arg2<=23 and arg3 in ['+', '-', '*', '/']:
    if arg3=='+':
        print(arg1+arg2)
    elif arg3=='-':
        print(arg1 - arg2)
    elif arg3=='*':
        print(arg1 * arg2)
    else:
        print(arg1 / arg2)

