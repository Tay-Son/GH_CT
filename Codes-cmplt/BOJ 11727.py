import sys

input_ = int(sys.stdin.readline())

lst_ = [0, 1, 3]
if input_ > 2:
    for cnt_ in range(3, input_ + 1):
        lst_.append(lst_[-1] + 2 * lst_[-2])
print(lst_[input_] % 10007)