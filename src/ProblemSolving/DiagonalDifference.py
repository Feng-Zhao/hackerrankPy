def diagonalDifference(arr):
    a = 0
    b = 0
    for i in range(0, len(arr)):
        a += arr[i][i]
        b += arr[i][len(arr) - i - 1]
    return abs(a - b)


if __name__ == '__main__':
    arr = [[11, 2, 4],[4, 5, 6],[10, 8, -12]]
    print(diagonalDifference(arr))
