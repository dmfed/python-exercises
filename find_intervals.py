'''
Задача состоит в поиске непрерывно возрастающих подпоследовательностей
в данном массиве (следующее значение = предыдущему +1).
Если в подпоследовательности более 2 элементов нужно разделить их символом "-".
Подпоследовательности разделить запятыми.
inp = [-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]
# returns "-6,-3-1,3-5,7-11,14,15,17-20"
'''

inp = [-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]

def find_intervals(values):
    start = 0
    end = 0
    result = ""
    for i in range(1, len(values)):
        if values[i] != values[i-1] + 1:
            result += str(values[end]) + ","
            start = i
        if i == start + 1:
            result += str(values[start]) + ","
        if i == start + 2:
            result = result[:-1] + "-"
        end = i
    result += str(values[end])
    print(result)
    return result

print(find_intervals(inp))
