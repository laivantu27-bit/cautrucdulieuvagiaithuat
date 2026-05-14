def snippet_5(n):
    total = 0
    for i in range(n):
        for j in range(i):
            total += 1
    return total


def snippet_6(n):
    k = 1
    total = 0
    while k < n:
        for i in range(n):
            total += 1
            k = k * 2
    return total


def snippet_7(arr):
    count = 0
    for x in arr:
        if x in arr: # kiểm tra x có trong arr
            count += 1
    return count


def snippet_8(arr):
    s = set(arr)
    count = 0
    for x in arr:
        if x in s:
            count += 1
    return count