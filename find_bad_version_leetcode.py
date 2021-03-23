def find_good(start, end):
        iterations = 0
        while start != end and iterations < 10:
            guess = (start + end) // 2
            print(start, end, guess)
            if isBadVersion(guess):
                end = guess
            else:
                start = guess + 1
            iterations += 1
        return start

def isBadVersion(n):
    bad = 4
    return n >= bad

print(find_good(1, 10))
