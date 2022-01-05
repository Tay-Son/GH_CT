import sys

lst_ = [0b1111011,
        0b0010010,
        0b0111101,
        0b0110111,
        0b1010110,
        0b1100111,
        0b1101111,
        0b0110010,
        0b1111111,
        0b1110111]

mat_ = [[0 for _ in range(10)] for _ in range(10)]
for idx_s in range(10):
    for idx_e in range(10):
        mat_[idx_s][idx_e] = str(bin(lst_[idx_s] ^ lst_[idx_e]))[2:].count('1')

for each_ in mat_:
    print(each_)

N_, K_, P_, X_ = map(int, sys.stdin.readline().split())
lst_X = list(map(int, list('0' * (K_ - len(str(X_))) + str(X_))))
cnt_ = 0

for C_ in range(1, N_ + 1):
    if C_ != X_:
        is_ = True
        tot_ = 0
        lst_C = list(map(int, list('0' * (K_ - len(str(C_))) + str(C_))))
        for idx_ in range(K_):
            tot_ += mat_[lst_X[idx_]][lst_C[idx_]]
            if tot_ > P_:
                is_ = False
                break
        if is_:
            cnt_ += 1
print(cnt_)

exit()
