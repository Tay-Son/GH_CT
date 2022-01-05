import sys
num_input = int(sys.stdin.readline())
lst_ = list(map(int,sys.stdin.readline().split()))

print((sum(lst_) * 100) / (len(lst_) * max(lst_)))