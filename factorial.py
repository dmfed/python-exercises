import math

def factorial1(n):
    if n == 0:
        return 1
    else:
        return n * factorial1(n-1)
    
def factorial2(n):
    fact = 1
    if n == 0:
        return fact
    else:        
        for i in range(1, n):
            fact *= i + 1            
        return fact 

for i in range(51):
    assert factorial1(i) == math.factorial(i) == factorial2(i)

print('All done')
