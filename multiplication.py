#!/usr/bin/env python3
import random, time, sys

NUMS = list(range(1,10))
TIME = 0
COUNT = 0
WRONG = 0

try:
    while True:
        if len(sys.argv) > 1:
            x = int(sys.argv[1])
        else:
            x = random.choice(NUMS)
        y = random.choice(NUMS)
        start = time.time()
        ans = int(input(f"{x} * {y} = "))
        end = time.time()
        if ans != x * y:
            print(f"НЕПРАВИЛЬНО. {x} * {y} = {x*y}")
            time.sleep(1)
            continue
        print("ВЕРНО!")
        COUNT += 1
        TIME += end - start
        time.sleep(1) 
except:
    print(f'''\n
Ты верно решил {COUNT} примеров и ошибся {WRONG} раз. 
На один пример ты тратил в среднем {int(TIME/COUNT)} секунд.''') 

     
