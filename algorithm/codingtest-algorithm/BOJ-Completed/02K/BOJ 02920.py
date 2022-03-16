lst_input = list(map(int,input().split()))

val_ = 0
for idx_ in range(7):
    if lst_input[idx_] > lst_input[idx_+1]:
        val_ -= 1
    elif lst_input[idx_] < lst_input[idx_+1]:
        val_ += 1
if val_ == 7:
    print('ascending')
elif val_ == -7:
    print('descending')
else:
    print('mixed')