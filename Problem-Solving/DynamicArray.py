import math
import os
import random
import re
import sys


def dynamicArray(n, queries):
    sequences = [[] for _ in range(n)]
    last_item = 0
    res = []

    for query in queries:
        index = (query[1] ^ last_item) % n
        
        if query[0] == 1:
            sequences[index].append(query[2])
        else:
            position = query[2] % len(sequences[index])
            last_item = sequences[index][position]
            res.append(last_item)
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
