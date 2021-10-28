import re

dote = re.compile("\\.", re.IGNORECASE)
comma = re.compile(",", re.IGNORECASE)

arg1 = input('Введите первый аргумент:\n')
arg2 = input('Введите второй аргумент:\n')

arg1_modified = dote.sub("", arg1)
arg1_modified = comma.sub("", arg1_modified)
arg2_modified = dote.sub("", arg2)
arg2_modified = comma.sub("", arg2_modified)

if ((arg1_modified.isdigit() and (3 <= float(arg1) <= 21)) and
    (arg2_modified.isdigit() and (3 <= float(arg2) <= 21))):
    print (abs(float(arg1) - float(arg2)))
else:
    print(arg1+arg2)