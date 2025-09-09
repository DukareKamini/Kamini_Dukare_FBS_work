n = int(input('Enter a number :'))

for i in range(n):
    for j in range(1, n - i):
        print('', end = ' ')

    num = 1
    for j in range(i + 1):
        print(num, end = ' ')
        num = num * (i - j) // (j + 1)

    print()

