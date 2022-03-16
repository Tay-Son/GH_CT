import sys

sys.stdin.readline()
set_ = set(map(int, sys.stdin.readline().split()))
sys.stdin.readline()
lst_ = list(map(int, sys.stdin.readline().split()))
answer = 0
for each_ in lst_:
    if each_ in set_:
        print(1)
    else:
        print(0)
