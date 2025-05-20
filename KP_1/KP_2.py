N = int(input("Enter the number "))

if 1<=N<=10:
    for i in range(1, N + 1): print(int((10 ** i - 1) / 9) ** 2)