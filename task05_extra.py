x = input('Введите число:\n')
if x.isdigit():
    result = 0
    for i in range(0, len(x)):
        result = result + int(x[i])
    print(result)
else:
    print("НЕ КОРРЕКТНЫЙ ВВОД ВХОДНЫХ ДАННЫХ")