num_input = int(input())
for _ in range(num_input):
    val_ = 0
    is_ = True
    for each_ in input():
        if each_ == '(':
            val_ += 1
        else:
            val_ -= 1
            if val_ < 0:
                is_ = False
                break
    if is_ and val_ == 0:
        print('YES')
    else:
        print('NO')