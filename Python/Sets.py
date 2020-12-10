def average(array):
    distinct = set(array)
    total = 0
    for item in distinct:
        total += item
    avg = total / len(distinct)
    return avg


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
