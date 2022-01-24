def solution(n, a, b):
    cnt_ = 0
    a -= 1
    b -= 1
    while a != b:
        a //= 2
        b //= 2
        cnt_ += 1
    return cnt_