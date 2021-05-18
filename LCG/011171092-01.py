import math
import matplotlib.pyplot as plt

z_1_0, z_1_1 = 5, 7
z_2_0 = 6
z_3_0, z_3_1 = 2, 7

trials = [100, 500, 1000]

for n in trials:
    z1_list = list()
    z1_list.append(z_1_0)
    z1_list.append(z_1_1)
    z2_list = list()
    z2_list.append(z_2_0)
    z3_list = list()
    z3_list.append(z_3_0)
    z3_list.append(z_3_1)
    z_list = list()
    u_list = list()

    for i in range(1, n):
        z1 = (z1_list[i - 1] ** 2 + z1_list[i] ** 3 + 5) % 15
        z1_list.append(z1)
    # print(len(z1_list))
    for i in range(n):
        z2 = (z2_list[i] + 4 * z2_list[i]) % 16
        z2_list.append(z2)
    # print(len(z2_list))

    for i in range(1, n):
        z3 = (3 * z3_list[i] + z3_list[i - 1] ** 3) % 15
        z3_list.append(z3)
    # print(len(z1_list))

    for i in range(1, n + 1):
        z = (z1_list[i] + 5 * (z2_list[i] ** 3) + 3 * z3_list[i]) % 16  # change
        z_list.append(z)
        u_list.append(z / 16)
    # print(len(z_list))
    print(f'For n = {n}, the list of U is ')
    print(u_list)
    n = [str(i) for i in range(n)]
    plt.bar(n, u_list, label='Random Number')
    plt.legend(loc='upper right')
    plt.show()
