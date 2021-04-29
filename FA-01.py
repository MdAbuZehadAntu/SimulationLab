p = [
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 1, 1, 0, 1],
    [0, 1, 0, 0, 1],
    [0, 0, 0, 0, 0]

]

for it in range(20):
    q = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]
    print("At time : ", it, '\n')
    for i in range(5):
        for j in range(5):
            print(p[i][j], end="")
        print()

    for i in range(5):
        for j in range(5):
            count = 0
            if i == 0 and j == 0:

                count = p[0][1] + p[1][0] + p[1][1]

                if p[i][j] == 1 and count < 2:
                    q[i][j] = 0
                elif p[i][j] == 1 and count == 2:
                    q[i][j] = 1
                elif p[i][j] == 1 and count > 2:
                    q[i][j] = 0
                elif p[i][j] == 0 and (count == 2 or count == 3):
                    q[i][j] = 1



            elif i == 0 and (1 <= j <= 3):
                count = p[0][j - 1] + p[0][j + 1] + p[1][j - 1] + p[1][j] + p[1][j + 1]

                if p[i][j] == 1 and count < 2:
                    q[i][j] = 0
                elif p[i][j] == 1 and count == 2:
                    q[i][j] = 1
                elif p[i][j] == 1 and count > 2:
                    q[i][j] = 0
                elif p[i][j] == 0 and (count == 2 or count == 3):
                    q[i][j] = 1
            elif i == 4 and j == 0:
                count = p[4][1] + p[3][1] + p[3][0]

                if p[i][j] == 1 and count < 2:
                    q[i][j] = 0
                elif p[i][j] == 1 and count == 2:
                    q[i][j] = 1
                elif p[i][j] == 1 and count > 2:
                    q[i][j] = 0
                elif p[i][j] == 0 and (count == 2 or count == 3):
                    q[i][j] = 1
            elif i == 0 and j == 4:
                count = p[0][3] + p[1][3] + p[1][4]

                if p[i][j] == 1 and count < 2:
                    q[i][j] = 0
                elif p[i][j] == 1 and count == 2:
                    q[i][j] = 1
                elif p[i][j] == 1 and count > 2:
                    q[i][j] = 0
                elif p[i][j] == 0 and (count == 2 or count == 3):
                    q[i][j] = 1
            elif i == 4 and j == 4:
                count = p[4][3] + p[3][3] + p[3][4]

                if p[i][j] == 1 and count < 2:
                    q[i][j] = 0
                elif p[i][j] == 1 and count == 2:
                    q[i][j] = 1
                elif p[i][j] == 1 and count > 2:
                    q[i][j] = 0
                elif p[i][j] == 0 and (count == 2 or count == 3):
                    q[i][j] = 1
            elif i == 4 and (1 <= j <= 3):
                count = p[4][j - 1] + p[3][j - 1] + p[3][j] + p[3][j + 1] + p[4][j + 1]

                if p[i][j] == 1 and count < 2:
                    q[i][j] = 0
                elif p[i][j] == 1 and count == 2:
                    q[i][j] = 1
                elif p[i][j] == 1 and count > 2:
                    q[i][j] = 0
                elif p[i][j] == 0 and (count == 2 or count == 3):
                    q[i][j] = 1
            elif (1 <= i <= 3) and (1 <= j <= 3):
                count = p[i - 1][j - 1] + p[i - 1][j] + p[i - 1][j + 1] + p[i][j + 1] + p[i + 1][j + 1] + p[i + 1][j] + \
                        p[i + 1][j - 1] + p[i][j - 1]

                if p[i][j] == 1 and count < 2:
                    q[i][j] = 0
                elif p[i][j] == 1 and count == 2:
                    q[i][j] = 1
                elif p[i][j] == 1 and count > 2:
                    q[i][j] = 0
                elif p[i][j] == 0 and (count == 2 or count == 3):
                    q[i][j] = 1

            elif (1 <= i <= 3) and j == 0:
                count = p[i - 1][0] + p[i - 1][j + 1] + p[i][j + 1] + p[i + 1][j + 1] + p[i + 1][j]

                if p[i][j] == 1 and count < 2:
                    q[i][j] = 0
                elif p[i][j] == 1 and count == 2:
                    q[i][j] = 1
                elif p[i][j] == 1 and count > 2:
                    q[i][j] = 0
                elif p[i][j] == 0 and (count == 2 or count == 3):
                    q[i][j] = 1
            elif (1 <= i <= 3) and j == 4:
                count = p[i][j - 1] + p[i - 1][j - 1] + p[i - 1][j] + p[i - 1][j - 1] + p[i + 1][j]
                if p[i][j] == 1 and count < 2:
                    q[i][j] = 0
                elif p[i][j] == 1 and count == 2:
                    q[i][j] = 1
                elif p[i][j] == 1 and count > 2:
                    q[i][j] = 0
                elif p[i][j] == 0 and (count == 2 or count == 3):
                    q[i][j] = 1

    p = q.copy()
