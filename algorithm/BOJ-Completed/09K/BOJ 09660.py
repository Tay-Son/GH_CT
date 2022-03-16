import sys

N = int(sys.stdin.readline())

lst_ = [False, True, False, True, True, True, True]

if lst_[N % 7] == True:
    print('SK')
else:
    print('CY')