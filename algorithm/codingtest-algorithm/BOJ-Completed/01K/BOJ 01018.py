import sys

N, M = map(int, sys.stdin.readline().split())
grd_ = []
for _ in range(N):
    grd_.append(list(sys.stdin.readline()))

val_ = ['W', 'B']
lst_answer = []
for offset_N in range(N - 7):
    for offset_M in range(M - 7):
        answer_ = 0
        for idx_N in range(offset_N, offset_N + 8):
            for idx_M in range(offset_M, offset_M + 8):
                cpr_ = val_[(idx_N + idx_M) % 2]
                if grd_[idx_N][idx_M] != cpr_:
                    answer_ += 1
        lst_answer.append(min(answer_, 64 - answer_))

print(min(lst_answer))