num_input = int(input())

cnt_ = 1
sum_ = 1

while sum_ < num_input:
    cnt_ += 1
    sum_ += cnt_

temp_ = num_input - (sum_ - cnt_)
val_a = temp_
val_b = (cnt_ + 1) - temp_

if cnt_ % 2:
    print(val_b, end='/')
    print(val_a)

else:
    print(val_a, end='/')
    print(val_b)