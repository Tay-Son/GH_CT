import sys

input_ = int(sys.stdin.readline())
for cnt_ in range(input_,0,-1):
    print(' ' * (input_ - cnt_) + '*' * cnt_)