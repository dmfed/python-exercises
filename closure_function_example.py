def myclosure():
    val = 0
    def add(x):
        nonlocal val ## this is the whole point
        val += x
        return val
    return add

pos = myclosure()

print(pos(1), pos(1)) 


