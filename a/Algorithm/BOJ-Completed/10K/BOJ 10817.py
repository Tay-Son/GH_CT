import sys

lst_ = list(map(int,sys.stdin.readline().split()))
lst_.sort()
print(lst_[-2])