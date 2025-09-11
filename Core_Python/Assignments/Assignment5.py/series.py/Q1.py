n = int(input('Enter the Value of n :'))
sum = 0
fact = 1

for i in range(1, n + 1):
    fact = fact * i
    sum = sum + fact

print(f'The sum of the series 1!+2!+3!+...+,{n}! is : {sum}')
