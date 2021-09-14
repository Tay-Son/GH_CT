import sys

num_tc = int(sys.stdin.readline())
for _ in range(num_tc):
    val_a, val_b = map(int, sys.stdin.readline().split())
    lst_ = [val_a % 10]
    curr_ = (lst_[0] * lst_[0]) % 10
    while curr_ != lst_[0]:
        lst_.append(curr_)
        curr_ *= lst_[0]
        curr_ %= 10

    answer_ = lst_[(val_b-1) % len(lst_)]
    if answer_ == 0:
        print(10)
    else:
        print(answer_)