N = int(input("Enter the number "))

if 1<=N<=9:
    for i in range(1, N): print((10**i) // 9 * i) #10**i // 9 создает последовательность чисел

