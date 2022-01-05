input_ = int(input())
for cnt_ in range(1, input_ + 1):
    print(' ' * (input_ - cnt_) + '*' * (2 * cnt_ - 1))
