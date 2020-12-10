cube = lambda x: x**3

def fibonacci(n):
    if n == 0:
        return []
    elif n == 1:
        return [0]
    a = 0
    b = 1
    i = 2
    numbers = [a, b]
    while i < n:
        numbers.append(a+b)
        temp = a
        a = b
        b += temp
        i += 1
    return numbers


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
