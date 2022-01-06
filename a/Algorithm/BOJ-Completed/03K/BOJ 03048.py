import sys

N1_, N2_ = map(int, sys.stdin.readline().split())
str_1 = sys.stdin.readline().strip()
str_2 = sys.stdin.readline().strip()
offset_ = int(sys.stdin.readline())
lst_ = [[str_1[N1_ - idx_ - 1], idx_ * 2] for idx_ in range(0, N1_)] + \
       [[str_2[idx_ - N1_], (idx_ - offset_) * 2 - 1] for idx_ in range(N1_, N1_ + N2_)]

lst_.sort(key=lambda x: x[1])

print(''.join(map(lambda x: str(x[0]), lst_)))

exit()