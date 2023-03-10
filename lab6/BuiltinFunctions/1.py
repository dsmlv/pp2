from functools import reduce

numbers = [2, 3, 5, 7, 11, 13]

product = reduce(lambda x, y: x * y, numbers)

print(product)