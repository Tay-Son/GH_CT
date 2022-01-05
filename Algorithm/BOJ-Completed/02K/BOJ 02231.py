import sys

input_ = int(sys.stdin.readline())


def func(n):
    ret_ = n
    while n > 10:
        ret_ += n % 10
        n //= 10
    ret_ += n
    return ret_


val_ = input_ - 9 * len(str(input_))
answer = 0
for val_ in range(input_ - 9 * len(str(input_)),input_+1):
    if func(val_) == input_:
        answer = val_
        break
print(answer)