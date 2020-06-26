digits = {'0': 0,
          '1': 1,
          '2': 2,
          '3': 3,
          '4': 4,
          '5': 5,
          '6': 6,
          '7': 7,
          '8': 8,
          '9': 9}

def to_int(val):
    multiplier = len(val) - 1
    number = 0
    for i in val:
        number += digits[i] * (10 ** multiplier)
        multiplier -= 1
    return number

def addition(a, b):
    x = to_int(a)
    y = to_int(b)
    return x + y

a = "123"
print(a, type(a))
b = to_int(a)
print(b, type(b))

print(addition("12", "30"))
