from functools import reduce

# functional programming style
squares = map(lambda x: x * x, [1, 2, 3, 4, 5])
should = reduce(lambda x, y: x and y, [True, True, False]) # help(reduce)
evens = filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5])

# pythonic style
squares = [x * x for x in [1, 2, 3, 4, 5]] # list comprehension
should = all([True, True, False]) # return true if all values in the list are True
evens = [x for x in [1,2,3,4,5] if x % 2 == 0]


# creating new functions from existing functions
from functools import partial

def pow(x, power=1):
    return x ** power

square = partial(pow, power=2)
cube = partial(pow, power=3)

square(2) # 4
cube(2) # 8