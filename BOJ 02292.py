input_ = int(input())

if input_ == 1:
    print(1)
else:
    cnt_ = 1
    sum_ = 0
    val_ = (input_ + 4)//6
    while sum_ < val_:
        sum_ += cnt_
        cnt_ += 1
    print(cnt_)