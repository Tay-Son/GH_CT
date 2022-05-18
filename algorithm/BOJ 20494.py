import sys

tot_ = 0
for _ in range(int(sys.stdin.readline())):
    str_ = sys.stdin.readline().rstrip()
    tot_ += len(str_)
print(tot_)

exit()
