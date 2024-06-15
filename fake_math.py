def divide(a, b):
    res = 0

    try:
        res = a / b

    except ZeroDivisionError:
        res = 'Ошибка'
    return res

#if __name__ == '__main__':

    # Вводим значения
first = float(input())
second = float(input())

result = divide(first, second)
print(result)
