area = int(input('Enter the Area of one wall :'))
interiorwall_cost = int(input('Enter the cost of interior wall :'))
exteriorwall_cost = int(input('Enter the cost of exterior wall :'))

Total_cost = area + (6 * exteriorwall_cost + 8 * interiorwall_cost)

print(f'cost of painting the building wall is : {Total_cost} ')