import requests
import json

def show_fact(number, t = 1):
    types = {1: 'trivia', 2: 'math', 3: 'date', 4: 'year'}
    url = f'http://numbersapi.com/{number}/{types[t]}?json'
    fact = requests.get(url)
    data = fact.json()
    if data['found']:
        print(data['text'])
    else:
        print('No interesting facts found...')

while True:
    number = input('Please enter number: ')
    t = input(
'''Enter type of fact or 'q' to quit
(1 - trivia, 2 - math, 3 - date, 4 - year): ''')
    if t == 'q':
        break
    if t != '' and t.isdigit() and 1 <= int(t) <=4:
        show_fact(number, t = int(t))
    else:
        show_fact(number)
    
    
    

