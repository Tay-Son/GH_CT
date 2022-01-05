import sys

lst_ = []
for _ in range(1,10):
    lst_.append(int(sys.stdin.readline()))
print(max(lst_))
print(lst_.index(max(lst_))+1)