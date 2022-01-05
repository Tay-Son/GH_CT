import sys

min_ = 99
sum_ = 0
for _ in range(7):
   input_ =  int(sys.stdin.readline())
   if input_ % 2:
       min_ = min(min_,input_)
       sum_ += input_

if sum_:
    print(sum_)
    print(min_)
else:
    print(-1)