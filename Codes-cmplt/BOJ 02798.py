from itertools import combinations as cb

N, M = map(int, input().split())
lst_ = list(map(int, input().split()))

max_answer = 0
for cb_ in cb(lst_, 3):
    sum_ = sum(cb_)
    if sum_ <= M:
        max_answer = max(sum_, max_answer)
print(max_answer)