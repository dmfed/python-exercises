#!/usr/bin/env python3

def fib_generator():
	a, b = 0, 1
	while True:
		yield a
		a, b = b, a+b

allfibs = fib_generator()

for _ in range(30):
	print(next(allfibs))
