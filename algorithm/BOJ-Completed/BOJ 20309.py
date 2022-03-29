import sys

N_ = int(sys.stdin.readline())
lst_ = list(map(int, sys.stdin.readline().split()))

for each_ in lst_[::2]:
    if not each_ % 2:
        print('NO')
        break
else:
    for each_ in lst_[1::2]:
        if each_ % 2:
            print('NO')
            break
    else:
        print('YES')

exit()
