lst_ = [0, 1, 2]

input_ = int(input())

if input_ > 2:
    for _ in range(3, input_ + 1):
        lst_.append(lst_[-2] + lst_[-1])
print(lst_[input_] % 10007)