def myclosure():
    val = 0
    def add(x):
        nonlocal val ## this is the whole point
        val += x
        return val
    return add

cl = myclosure()

print(cl(1), cl(1), cl(1)) 


