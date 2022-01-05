import sys

input_ = int(sys.stdin.readline())
for cnt_ in range(1, input_):
    print(' ' * (input_ - cnt_) + '*' * (2 * cnt_ - 1))
for cnt_ in range(input_, 0, -1):
    print(' ' * (input_ - cnt_) + '*' * (2 * cnt_ - 1))
