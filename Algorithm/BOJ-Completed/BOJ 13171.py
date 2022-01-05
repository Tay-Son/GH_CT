import sys

DIV_ = 1000000007
A_ = int(sys.stdin.readline())
X_ = int(sys.stdin.readline())

ans_ = 1
while X_:
    X_, is_ = divmod(X_, 2)
    if is_:
        ans_ *= A_
        ans_ %= DIV_
    A_ *= A_
    A_ %= DIV_

print(ans_)

exit()
