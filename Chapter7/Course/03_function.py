"""
def test_func(compute):
    result = compute(1, 2)
    print(result)


def compute(x, y):
    return x + y


test_func(compute)
"""

def test_func(compute):
    result = compute(1, 2)
    print(result)


def compute_add(x, y):
    return x + y

def compute_minus(x, y):
    return x - y

def compute_multiply(x, y):
    return x * y


test_func(compute_add)
test_func(compute_minus)
test_func(compute_multiply)



