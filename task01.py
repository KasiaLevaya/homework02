def is_num(str):
    try:
        float(str)
        return True
    except ValueError:
        return False

arg1 = input('Введите первый аргумент:\n')
arg2 = input('Введите второй аргумент:\n')

if ((is_num(arg1) and (3 <= float(arg1) <= 21)) and
    (isdigit(arg2) and (3 <= float(arg2) <= 21))):
    print (abs(float(arg1) - float(arg2)))
else:
    print(arg1+arg2)