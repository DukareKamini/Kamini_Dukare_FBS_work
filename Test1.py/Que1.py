l = int(input('Enter the Length :'))
b = int(input('Enter the Breadth :'))
r = int(input('Enter the Radius :'))

Area = l * b + (1/2 * 22/7 * (r ** r))

print(f'Area of figure is : {Area}')

Perimeter = 2 * (l + b) + (22/7 * r + (2 * r))

print(f'Perimeter of figure is : {Perimeter}')