import sys

input_ = int(sys.stdin.readline())
cnt_ = 0
val_ = 665
while cnt_ < input_:
    val_ += 1
    if '666' in str(val_):
        cnt_ += 1
print(val_)