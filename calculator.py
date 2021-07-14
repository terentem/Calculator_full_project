# Calculator

from Functions import menu, get_value, get_operation, calc
import glob


# вывод меню
menu()

# программма
while 1 == 1:
    # принимаем переменную и выполняем операцию
    glob.val = get_value()
    glob.result = calc(float(glob.result), glob.op, float(glob.val))
    glob.expr = str(glob.expr) + ' ' + str(glob.val)
    print(glob.expr)
    print("отладка: result = " + str(glob.result) + ", memory = " + str(glob.memory) + ", op = " + str(glob.op) + ", val = " + str(glob.val))

    # принимаем операцию
    glob.op = get_operation()
    if glob.op == '=':
        glob.expr = str(glob.expr) + ' ' + str(glob.op) + ' ' + str(glob.result)
        print(glob.expr)
        glob.expr = 'expr: '
        glob.result = float(0)
        glob.op = '+'
        print("отладка: result = " + str(glob.result) + ", memory = " + str(glob.memory) + ", op = " + str(glob.op) + ", val = " + str(glob.val))
    else:
        glob.expr = str(glob.expr) + ' ' + str(glob.op)
        print(glob.expr)
        print("отладка: result = " + str(glob.result) + ", memory = " + str(glob.memory) + ", op = " + str(glob.op) + ", val = " + str(glob.val))