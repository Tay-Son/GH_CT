import sys

for _ in range(int(sys.stdin.readline())):
    N_ = int(sys.stdin.readline())
    if not (N_ % 9) or (N_ % 3 == 2):
        print('TAK')
    else:
        print('NIE')

exit()
