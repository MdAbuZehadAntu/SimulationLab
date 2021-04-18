arr = [
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 1, 1, 0, 1],
    [0, 1, 0, 0, 1],
    [0, 0, 0, 0, 0]
]

for it in range(21):
    array = []
    for i in range(len(arr)):
        array.append([0 for i in range(len(arr))])
    print(f"Time-{it}")
    for i in range(len(arr)):
        for j in range(len(arr)):
            print(arr[i][j], end=" ")
        print()
    print()

    for i in range(len(arr)):
        for j in range(len(arr)):

            if (i != 0 and i != len(arr) - 1) and (j != 0 and j != len(arr) - 1):
                p = i - 1
                k = j - 1
                c = 0
                for l in range(p, p + 3):
                    for m in range(k, k + 3):
                        if arr[l][m] == 1 and (l != i or m != j):
                            c += 1
                if c < 2 and arr[i][j] == 1:
                    array[i][j] = 0
                elif c > 2 and arr[i][j] == 1:
                    array[i][j] = 0
                elif c == 2 and arr[i][j] == 1:
                    array[i][j] = 1
                if (c == 2 or c == 3) and arr[i][j] == 0:
                    array[i][j] = 1

            elif i == 0 and 1 <= j < len(arr) - 1:
                k = 0
                c = 0
                for l in range(0, 2):
                    for m in range(j - 1, j + 2):
                        if arr[l][m] == 1 and (l != i or m != j):
                            c += 1
                if c < 2 and arr[i][j] == 1:
                    array[i][j] = 0
                elif c > 2 and arr[i][j] == 1:
                    array[i][j] = 0
                elif c == 2 and arr[i][j] == 1:
                    array[i][j] = 1
                if (c == 2 or c == 3) and arr[i][j] == 0:
                    array[i][j] = 1

            elif i == len(arr) - 1 and 1 <= j < len(arr) - 1:
                k = 0
                c = 0
                for l in range(i - 1, i + 1):
                    for m in range(j - 1, j + 2):
                        if arr[l][m] == 1 and (l != i or m != j):
                            c += 1
                if c < 2 and arr[i][j] == 1:
                    array[i][j] = 0
                elif c > 2 and arr[i][j] == 1:
                    array[i][j] = 0
                elif c == 2 and arr[i][j] == 1:
                    array[i][j] = 1
                if (c == 2 or c == 3) and arr[i][j] == 0:
                    array[i][j] = 1

            elif j == 0 and 1 <= i < len(arr) - 1:
                k = 0
                c = 0
                for l in range(i - 1, i + 2):
                    for m in range(j, j + 2):
                        if arr[l][m] == 1 and (l != i or m != j):
                            c += 1
                if c < 2 and arr[i][j] == 1:
                    array[i][j] = 0
                elif c > 2 and arr[i][j] == 1:
                    array[i][j] = 0
                elif c == 2 and arr[i][j] == 1:
                    array[i][j] = 1
                if (c == 2 or c == 3) and arr[i][j] == 0:
                    array[i][j] = 1

            elif j == len(arr) - 1 and 1 <= i < len(arr) - 1:
                k = 0
                c = 0
                for l in range(i - 1, i + 2):
                    for m in range(j - 1, j + 1):
                        if arr[l][m] == 1 and (l != i or m != j):
                            c += 1
                if c < 2 and arr[i][j] == 1:
                    array[i][j] = 0
                elif c > 2 and arr[i][j] == 1:
                    array[i][j] = 0
                elif c == 2 and arr[i][j] == 1:
                    array[i][j] = 1
                if (c == 2 or c == 3) and arr[i][j] == 0:
                    array[i][j] = 1

            elif i == j and (i == 0 or i == len(arr) - 1):

                if i == 0:
                    c = arr[i][j + 1] + arr[i + 1][j] + arr[i + 1][j + 1]
                    if c < 2 and arr[i][j] == 1:
                        array[i][j] = 0
                    elif c > 2 and arr[i][j] == 1:
                        array[i][j] = 0
                    elif c == 2 and arr[i][j] == 1:
                        array[i][j] = 1
                    if (c == 2 or c == 3) and arr[i][j] == 0:
                        array[i][j] = 1

                elif i == len(arr) - 1:
                    c = arr[i][j - 1] + arr[i - 1][j - 1] + arr[i - 1][j]
                    if c < 2 and arr[i][j] == 1:
                        array[i][j] = 0
                    elif c > 2 and arr[i][j] == 1:
                        array[i][j] = 0
                    elif c == 2 and arr[i][j] == 1:
                        array[i][j] = 1
                    if (c == 2 or c == 3) and arr[i][j] == 0:
                        array[i][j] = 1

            elif i == 0 and j == len(arr) - 1:
                c = arr[i][j - 1] + arr[i + 1][j - 1] + arr[i + 1][j]
                if c < 2 and arr[i][j] == 1:
                    array[i][j] = 0
                elif c > 2 and arr[i][j] == 1:
                    array[i][j] = 0
                elif c == 2 and arr[i][j] == 1:
                    array[i][j] = 1
                if (c == 2 or c == 3) and arr[i][j] == 0:
                    array[i][j] = 1

            elif i == len(arr) - 1 and j == 0:
                c = arr[i - 1][j] + arr[i - 1][j + 1] + arr[i][j + 1]
                if c < 2 and arr[i][j] == 1:
                    array[i][j] = 0
                elif c > 2 and arr[i][j] == 1:
                    array[i][j] = 0
                elif c == 2 and arr[i][j] == 1:
                    array[i][j] = 1
                if (c == 2 or c == 3) and arr[i][j] == 0:
                    array[i][j] = 1

    arr = array.copy()
