def PrimeNo(n):
    if n < 2:
        return False
    for i in range(2, n // 2 + 1):
            if (n % i == 0):
                return False
    return True

def sumPrimeNo(beg, end):
    sum = 0
    for num in range (beg, end + 1):
          if PrimeNo(num):
               sum += num
    return sum

beg = int(input('Enter the beginning of range :'))
end = int(input('Enter the ending of range :')) 
res = sumPrimeNo(beg, end)
print(f'sum of all prime numbers is :{res}')
        