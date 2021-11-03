x = input('Введите трехзначное число:\n')
if len(x) ==3 and x.isdigit():
    print(int(x[0])+int(x[1])+int(x[2]))
else:
    print("НЕ КОРРЕКТНЫЙ ВВОД ВХОДНЫХ ДАННЫХ")