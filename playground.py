# We can pass n number of arguments using the *args in argument list
def add(*args):
    sum_num = 0
    for arg in args:
        sum_num += arg
    return sum_num


print(add(1, 2, 3, 4, 5))


# We can pass n number of key word arguments using the **kwargs in argument list
def calculate(n, **kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key)
        print(value)
    n += kwargs["add"]
    # .get method will not break rather give None if the item doesn't exist in dict
    n *= kwargs.get("multiply")
    print(n)


calculate(2, add=3, multiply=5)
