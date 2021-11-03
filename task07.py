def is_num(str):
    try:
        float(str)
        return True
    except ValueError:
        return False

arg1=input('Введите сумму вклада:\n')
arg2=input('Введите число лет вклада:\n')
if is_num(arg1) and arg2.isdigit() and int(arg2) > 0 and float(arg1) > 0:
    arg1 = float(arg1)
    arg2 = int(arg2)
    for i in range(0,arg2):
        arg1 = arg1 + arg1 * 0.1
    print(arg1)
else:
    print("НЕ КОРРЕКТНЫЙ ВВОД ВХОДНЫХ ДАННЫХ")

