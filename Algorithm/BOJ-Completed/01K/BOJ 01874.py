import sys

n = int(sys.stdin.readline())

stk_ = []
curr_ = 1
lst_answer = []
is_ = True
for _ in range(n):
    input_ = int(sys.stdin.readline())
    while curr_ < input_ + 1:
        stk_.append(curr_)
        curr_ += 1
        lst_answer.append('+')
    temp_ = stk_.pop()
    if temp_ == input_:
        lst_answer.append('-')
    else:
        is_ =False
        break

if is_:
    for each_ in lst_answer:
        print(each_)
else:
    print('NO')