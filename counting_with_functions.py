def zero(operation=None):
    value = 0
    return value if not operation else operation(value)

def one(operation=None):
    value = 1
    return value if not operation else operation(value)

def two(operation=None):
    value = 2
    return value if not operation else operation(value)

def three(operation=None):
    value = 3
    return value if not operation else operation(value)

def four(operation=None):
    value = 4
    return value if not operation else operation(value)

def five(operation=None):
    value = 5
    return value if not operation else operation(value)

def six(operation=None):
    value = 6
    return value if not operation else operation(value)

def seven(operation=None):
    value = 7
    return value if not operation else operation(value)

def eight(operation=None):
    value = 8
    return value if not operation else operation(value)

def nine(operation=None):
    value = 9
    return value if not operation else operation(value)

def plus(val):
    def wrapper(args):
        result = args + val
        return result
    return wrapper

def minus(val):
    def wrapper(args):
        result = args - val
        return result
    return wrapper

def times(val):
    def wrapper(args):
        result = args * val
        return result
    return wrapper

def divided_by(val):
    def wrapper(args):
        result = args / val
        return result
    return wrapper

# print(zero(), two())
print(five(times(two())))

    
        