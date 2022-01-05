import sys

N, M, B = map(int, sys.stdin.readline().split())

lst_ = []
for _ in range(N):
    lst_ += list(map(int, sys.stdin.readline().split()))

min_ = max(0, min(lst_))
max_ = min(256, (sum(lst_) + B) // (N * M))

lst_answer = []
for cnt_ in range(max_, min_ - 1, -1):
    tot_ = 0
    for each_ in lst_:
        val_ = each_ - cnt_
        if val_ < 0:
            val_ = - val_
        else:
            val_ *= 2
        tot_ += val_
    lst_answer.append([tot_, cnt_])
lst_answer.sort(key=lambda x:x[0])

print(' '.join(map(str, lst_answer[0])))