import sys

lst_ = []
for _ in range(int(sys.stdin.readline())):
    lst_.append(int(sys.stdin.readline()))

stk_ = [(lst_[0], 1)]
cnt_ = 0
for each_ in lst_[1:]:
    while stk_ and each_ > stk_[-1][0]:
        stk_.pop()
        cnt_ += 1

    if stk_:
        if each_ == stk_[-1][0]:
            cnt_ += stk_[-1][1]
            stk_.append((each_, stk_[-1][1] + 1))
        else:
            cnt_ += 1
            stk_.append((each_, 2))

    else:
        stk_.append((each_, 1))

print(cnt_)

exit()
