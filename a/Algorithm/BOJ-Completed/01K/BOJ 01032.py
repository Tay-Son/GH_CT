import sys

N = int(sys.stdin.readline())
str_ = sys.stdin.readline().split()[0]
for _ in range(1, N):
    input_ = sys.stdin.readline().split()[0]
    str_temp = ''
    for idx_ in range(len(str_)):
        if str_[idx_] != '?' and str_[idx_] != input_[idx_]:
            str_temp += '?'
        else:
            str_temp += str_[idx_]
    str_ = str_temp
print(str_)