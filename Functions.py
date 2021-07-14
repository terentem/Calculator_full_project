import glob


def menu():
    print('**************************************')
    print('**          Calculator              **')
    print('**   Ralised operations (+,-,*,/)   **')
    print('** You can use following commands:  **')
    print('** ________________________________ **')
    print('**  exit (exit from calculator)     **')
    print('**  m  (add result to memory)       **')
    print('**  mr (get from memory to val)     **')
    print('**  cl (clear memory)               **')
    print('**  c (clear result)                **')
    print('**************************************')


# получение числа
def get_value():
    while 1 == 1:
        v = input("input number > ")
        is_command(v)
        if v == 'mr':
            return float(glob.memory)
        if is_number(v):
            return v


# получение оператора
def get_operation():
    while 1 == 1:
        v = input("input operation > ")
        is_command(v)
        if v == '+' or v == '-' or v == '*' or v == '/' or v == '=':
            return v


# проверка на число
def is_number(in_str):
    try:
        float(in_str)
        return True
    except ValueError:
        return False


# проверка и выполнение команды
def is_command(in_str):
    if in_str == 'exit':
        quit()
    if in_str == 'm':
        glob.memory = float(glob.result)
        print("command 'm' is done")
    if in_str == 'cl':
        glob.memory = float(0)
        print("command 'cl' is done")
    if in_str == 'c':
        glob.expr = 'expr: '
        glob.result = float(0)
        glob.op = '+'
        print("command 'c' is done")
    if in_str == 'mr':
        glob.val = float(glob.memory)
        print("command 'mr' is done")


# операция расчета
def calc(d_result, d_op, d_val):
    try:
        if d_op == '+':
            d_result = d_result + d_val
        if d_op == '-':
            d_result = d_result - d_val
        if d_op == '*':
            d_result = d_result * d_val
        if d_op == '/':
            d_result = d_result / d_val
        if d_op == '=':
            d_result = d_result
        return d_result
    except ZeroDivisionError as e:
        print("Деление на ноль!!")
        return float(0)
    except Exception as e:
        print("Ошибка " + e)
        return float(0)
