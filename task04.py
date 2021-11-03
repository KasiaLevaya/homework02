import math

def print_error():
    print("НЕ КОРРЕКТНЫЙ ВВОД ВХОДНЫХ ДАННЫХ")

def is_positive_num(str):
    try:
        return float(str) > 0
    except ValueError:
        return False

d = {1: 'прямоугольник', 2: 'треугольник', 3: 'круг'}
print("Сделайте выбор: ", d)
d_key=input('')
if d_key.isdigit() and 0<int(d_key)<4:
    d_key = int(d_key)
    if d_key == 1:
        arg1 = input('Введите длину одной стороны: ')
        arg2 = input('Введите длину второй стороны: ')
        if is_positive_num(arg1) and is_positive_num(arg2):
            print('Площадь (', d.get(d_key), '):')
            print(float(arg1)*float(arg2))
        else:
            print_error()
    elif d_key == 2:
        arg1 = input('Введите длину одной стороны: ')
        arg2 = input('Введите длину второй стороны: ')
        arg3 = input('Введите длину третей стороны: ')
        if is_positive_num(arg1) and is_positive_num(arg2) and is_positive_num(arg3):
            arg1 = float(arg1)
            arg2 = float(arg2)
            arg3 = float(arg3)
            p = (arg1 + arg2 + arg3) / 2
            if is_positive_num(p-arg1) and is_positive_num(p-arg2) and is_positive_num(p-arg3):
                print('Площадь (', d.get(d_key), '):')
                print(math.sqrt(p*(p-arg1)*(p-arg2)*(p-arg3)))
            else:
                print_error()
        else:
            print_error()
    else:
        arg1 = input('Введите радиус: ')
        if is_positive_num(arg1):
            print('Площадь (', d.get(d_key), '):')
            print(math.pi*math.pow(float(arg1),2))
        else:
            print_error()
else:
    print_error()

