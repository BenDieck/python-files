from functools import reduce

def mult_recursive(list, index=0):
    return 1 if index >= len(list) else list[index] * mult_recursive(list, index + 1)

def mult_lambda(list):
    return reduce(lambda x, y: x*y, list)

def mult_loop(list):
    prod = 1
    for item in list:
        prod *= item
    return prod

list = [1,2,3,4,5,6,]

prod = mult_recursive(list)
prod2 = mult_lambda(list)
prod3 = mult_loop(list)

print(f"prod = {prod}")
print(f"prod2 = {prod2}")
print(f"prod3 = {prod3}")
