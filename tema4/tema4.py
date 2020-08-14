def func2(a, b, c):
    min = 10000
    for x in range(-10, 11):
        ec = a * x ** 2 - 2 * b * x + c
        if min > ec:
            min = ec
            var = x
    return var


def func1(a, b, c):
    return func2(a, b, c)


print(func1(1, 3, 5))

