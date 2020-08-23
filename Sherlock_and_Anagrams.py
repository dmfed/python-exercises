'''
Вам предоставляется строка . Найдите количество неупорядоченных анаграммных пар подстрок.

Формат входных данных
Первая строка содержит число   количество тестов. Каждый тест состоит из строки, 
записанной в одной строке.

Строка  состоит только из строчных букв английского алфавита.

Формат выходных данных
Выведите ответ для каждого теста в отдельной строке.

Пример входных данных

2
abba
abcd
Пример выходных данных

4
0
'''

def sherlockAndAnagrams(s):
    slices = dict()
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            key = "".join(sorted(s[i:j]))
            slices[key] = slices.get(key, 0) + 1
    print(slices)
    count = sum([(slices[val] * (slices[val] - 1) / 2) for val in slices if slices[val] > 1])
    return int(count)

print("kkkk", sherlockAndAnagrams("kkkk")) # 10
print("abba", sherlockAndAnagrams("abba")) # 4
