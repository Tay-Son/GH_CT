import sys

for _ in range(3):
    cnt_ = sys.stdin.readline().split().count('1')
    if cnt_ == 1:
        print('C')
    elif cnt_ == 2:
        print('B')
    elif cnt_ == 3:
        print('A')
    elif cnt_ == 4:
        print('E')
    else:
        print('D')

exit()