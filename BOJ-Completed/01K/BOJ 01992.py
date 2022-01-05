import sys

sys.setrecursionlimit(99999)

N = int(sys.stdin.readline())
grd_ = []
for _ in range(N):
    grd_.append(list(sys.stdin.readline()))

def func(x, y, n):
    if n == 1:
        return grd_[y][x]
    else:
        lst_ = []
        temp_ = n // 2
        lst_.append(func(x, y, temp_))
        lst_.append(func(x + temp_, y, temp_))
        lst_.append(func(x, y + temp_, temp_))
        lst_.append(func(x + temp_, y + temp_, temp_))
        if lst_.count('1') == 4:
            return ('1')
        elif lst_.count('0') == 4:
            return ('0')
        else:
            return ('(' + ''.join(lst_) + ')')


print(func(0, 0, N))