import sys
r = 31
M = 1234567891

len_str = int(sys.stdin.readline())
str_input = sys.stdin.readline()

answer_ = 0
for idx_ in range(len_str):
    temp_ = (ord(str_input[idx_]) - ord('a') + 1) * (r ** idx_) % M
    answer_ += temp_
print(answer_ % M)