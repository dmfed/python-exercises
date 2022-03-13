def diamond(width: int):
    w = 1
    offset = width//2 
    print('*' * width)
    while w < (width - 2):
        print('*' * offset, end='')
        print(' ' * w, end='')
        print('*' * offset)
        w += 2
        offset -= 1
    while w > 0:
        print('*' * offset, end='')
        print(' ' * w, end='')
        print('*' * offset)
        w -= 2
        offset += 1
    print('*' * width)



if __name__ == '__main__':
    diamond(15)
