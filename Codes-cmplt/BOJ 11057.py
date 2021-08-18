import sys

input_ = int(sys.stdin.readline())

lst_ = [1] * 10
if input_ > 1:
    for _ in range(1, input_):
        lst_temp = []
        sum_ = 0
        for idx_ in range(10):
            sum_ += lst_[idx_]
            lst_temp.append(sum_)
        lst_ = lst_temp

print(sum(lst_) % 10007)