arr = [
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 1, 1, 0, 1],
    [0, 1, 0, 0, 1],
    [0, 0, 0, 0, 0]
]


class Array:
    def __init__(self, arr):
        self.arr = arr

    def _show(self):
        for i in range(len(self.arr)):
            for j in range(len(self.arr)):
                print(self.arr[i][j], end=" ")
            print()
        print()

    def show(self):
        for it in range(21):
            array = []
            for i in range(len(self.arr)):
                array.append([0 for i in range(len(self.arr))])

            print(f"Time-{it}")
            self._show()

            for i in range(len(self.arr)):
                for j in range(len(self.arr)):

                    if (0 != i and i != len(self.arr) - 1) and (j != 0 and j != len(self.arr) - 1):
                        p = i - 1
                        k = j - 1
                        c = 0
                        for l in range(p, p + 3):
                            for m in range(k, k + 3):
                                if self.arr[l][m] == 1 and (l != i or m != j):
                                    c += 1
                        if c < 2 and self.arr[i][j] == 1:
                            array[i][j] = 0
                        elif c > 2 and self.arr[i][j] == 1:
                            array[i][j] = 0
                        elif c == 2 and self.arr[i][j] == 1:
                            array[i][j] = 1
                        if (c == 2 or c == 3) and self.arr[i][j] == 0:
                            array[i][j] = 1

                    elif i == 0 and 1 <= j < len(self.arr) - 1:
                        k = 0
                        c = 0
                        for l in range(0, 2):
                            for m in range(j - 1, j + 2):
                                if self.arr[l][m] == 1 and (l != i or m != j):
                                    c += 1
                        if c < 2 and self.arr[i][j] == 1:
                            array[i][j] = 0
                        elif c > 2 and self.arr[i][j] == 1:
                            array[i][j] = 0
                        elif c == 2 and self.arr[i][j] == 1:
                            array[i][j] = 1
                        if (c == 2 or c == 3) and self.arr[i][j] == 0:
                            array[i][j] = 1

                    elif i == len(self.arr) - 1 and 1 <= j < len(self.arr) - 1:
                        k = 0
                        c = 0
                        for l in range(i - 1, i + 1):
                            for m in range(j - 1, j + 2):
                                if self.arr[l][m] == 1 and (l != i or m != j):
                                    c += 1
                        if c < 2 and self.arr[i][j] == 1:
                            array[i][j] = 0
                        elif c > 2 and self.arr[i][j] == 1:
                            array[i][j] = 0
                        elif c == 2 and self.arr[i][j] == 1:
                            array[i][j] = 1
                        if (c == 2 or c == 3) and self.arr[i][j] == 0:
                            array[i][j] = 1

                    elif j == 0 and 1 <= i < len(self.arr) - 1:
                        k = 0
                        c = 0
                        for l in range(i - 1, i + 2):
                            for m in range(j, j + 2):
                                if self.arr[l][m] == 1 and (l != i or m != j):
                                    c += 1
                        if c < 2 and self.arr[i][j] == 1:
                            array[i][j] = 0
                        elif c > 2 and self.arr[i][j] == 1:
                            array[i][j] = 0
                        elif c == 2 and self.arr[i][j] == 1:
                            array[i][j] = 1
                        if (c == 2 or c == 3) and self.arr[i][j] == 0:
                            array[i][j] = 1

                    elif j == len(self.arr) - 1 and 1 <= i < len(self.arr) - 1:
                        k = 0
                        c = 0
                        for l in range(i - 1, i + 2):
                            for m in range(j - 1, j + 1):
                                if self.arr[l][m] == 1 and (l != i or m != j):
                                    c += 1
                        if c < 2 and self.arr[i][j] == 1:
                            array[i][j] = 0
                        elif c > 2 and self.arr[i][j] == 1:
                            array[i][j] = 0
                        elif c == 2 and self.arr[i][j] == 1:
                            array[i][j] = 1
                        if (c == 2 or c == 3) and self.arr[i][j] == 0:
                            array[i][j] = 1

                    elif i == j and (i == 0 or i == len(self.arr) - 1):

                        if i == 0:
                            c = self.arr[i][j + 1] + self.arr[i + 1][j] + self.arr[i + 1][j + 1]
                            if c < 2 and self.arr[i][j] == 1:
                                array[i][j] = 0
                            elif c > 2 and self.arr[i][j] == 1:
                                array[i][j] = 0
                            elif c == 2 and self.arr[i][j] == 1:
                                array[i][j] = 1
                            if (c == 2 or c == 3) and self.arr[i][j] == 0:
                                array[i][j] = 1

                        elif i == len(self.arr) - 1:
                            c = self.arr[i][j - 1] + self.arr[i - 1][j - 1] + self.arr[i - 1][j]
                            if c < 2 and self.arr[i][j] == 1:
                                array[i][j] = 0
                            elif c > 2 and self.arr[i][j] == 1:
                                array[i][j] = 0
                            elif c == 2 and self.arr[i][j] == 1:
                                array[i][j] = 1
                            if (c == 2 or c == 3) and self.arr[i][j] == 0:
                                array[i][j] = 1

                    elif i == 0 and j == len(self.arr) - 1:
                        c = self.arr[i][j - 1] + self.arr[i + 1][j - 1] + self.arr[i + 1][j]
                        if c < 2 and self.arr[i][j] == 1:
                            array[i][j] = 0
                        elif c > 2 and self.arr[i][j] == 1:
                            array[i][j] = 0
                        elif c == 2 and self.arr[i][j] == 1:
                            array[i][j] = 1
                        if (c == 2 or c == 3) and self.arr[i][j] == 0:
                            array[i][j] = 1

                    elif i == len(self.arr) - 1 and j == 0:
                        c = self.arr[i - 1][j] + self.arr[i - 1][j + 1] + self.arr[i][j + 1]
                        if c < 2 and self.arr[i][j] == 1:
                            array[i][j] = 0
                        elif c > 2 and self.arr[i][j] == 1:
                            array[i][j] = 0
                        elif c == 2 and self.arr[i][j] == 1:
                            array[i][j] = 1
                        if (c == 2 or c == 3) and self.arr[i][j] == 0:
                            array[i][j] = 1

            self.arr = array.copy()


arr = Array(arr)
arr.show()
