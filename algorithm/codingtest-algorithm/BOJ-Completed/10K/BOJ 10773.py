import sys

K = int(sys.stdin.readline())
lst_ = []
for _ in range(K):
    input_ = int(sys.stdin.readline())
    if not input_:
        lst_.pop()
    else:
        lst_.append(input_)
print(sum(lst_))