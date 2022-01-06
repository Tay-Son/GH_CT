import sys

a_, b_ = map(int, sys.stdin.readline().split())
while a_ and b_:
    if a_ < b_:
        if not b_ % a_:
            print('factor')
        else:
            print('neither')
    else:
        if not a_ % b_:
            print('multiple')
        else:
            print('neither')
    a_, b_ = map(int, sys.stdin.readline().split())

exit()
