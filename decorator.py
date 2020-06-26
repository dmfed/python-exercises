def verbose(func, *args):
    def wrapper(*args):
        print(f"Running function {func.__name__} with arguments {args}")
        print(func(*args))
        print("All done")
    return wrapper


@verbose
def check_equal(a, b):
    assert type(a) is type(b), "Trying to compare defferent types"
    return a == b


check_equal(1, 1)

print(check_equal.__name__)  # says "wrapper"
