def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fibonacci(n-1) + fibonacci(n-2)


# print(fibonacci(5))

def lucas(num):
    if num == 0:
        return 2
    if num == 1:
        return 1

    return lucas(num-1) + lucas(num-2)

# print(lucas())


def sum_series(nth, first = 0, second = 1):
    if nth == 0:
        return first
    if nth == 1:
        return second

    return sum_series(nth-1, first, second) + sum_series(nth-2, first, second)


print(sum_series(0, 2, 1))
