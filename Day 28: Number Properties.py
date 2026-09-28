import math

for x in range(1, 10):
    properties = {
        "number": x,
        "square": x**2,
        "cube": x**3,
        "factorial": math.factorial(x),
        "even": x % 2 == 0,
    }
    print(properties)
