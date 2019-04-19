import sys, os, ipdb

def get_xy(pos, size):
    x = int(pos % size)
    y = int(pos / size)
    return x, y

def snail_it(l):
    pos = 0
    size = len(l[0])
    buff = []
    #for i in range(size**2):
    x, y = get_xy(pos, size)
    while len(buff) != size**2:
        while x + 1 < size and l[y][x+1] != '':
            buff.append(l[y][x])
            l[y][x] = ''
            pos +=1
            x, y = get_xy(pos, size)
            if x + 1 < size and l[y][x+1] == '':
                break

        while y + 1 < size and l[y+1][x] != '':
            buff.append(l[y][x])
            l[y][x] = ''
            pos += size
            x, y = get_xy(pos, size)
            if y + 1 < size and l[y + 1][x] == '':
                break

        while x - 1 >= 0 and l[y][x - 1] != '':
            buff.append(l[y][x])
            l[y][x] = ''
            pos -= 1
            x, y = get_xy(pos, size)
            if x - 1 >=0 and l[y][x-1] == '':
                break

        while y - 1 >= 0:
            buff.append(l[y][x])
            l[y][x] = ''
            pos -= size
            x, y = get_xy(pos, size)
            if y - 1 >= 0 and l[y - 1][x] == '':
                break

    print(buff)




def main():
    l = [
        [1,   2,  3, 4],
        [12, 13, 14, 5],
        [11,  0, 15, 6],
        [10,  9,  8, 7],
    ]
    l2 = [
        [1,2,3],
        [8,0,4],
        [7,6,5]
    ]
    l3 = [
        [1, 2, 3, 4, 5],
        [16, 17, 18, 19,6],
        [15, 24, 0, 20,7],
        [14, 23, 22, 21,8],
        [13, 12, 11,10,9],
    ]
    l4 = [
        [ 1,  2,  3,  4,  5,  6],
        [20, 21, 22, 23, 24,  7],
        [19, 32, 33, 34, 25,  8],
        [18, 31,  0, 35, 26,  9],
        [17, 30, 29, 28, 27, 10],
        [16, 15, 14, 13, 12, 11],
    ]
    snail_it(l2)
    snail_it(l)
    snail_it(l3)
    snail_it(l4)


if __name__ == '__main__':
    main()
