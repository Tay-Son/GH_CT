set_ = set()

def func_d(n):
    ret_ = n+sum(map(int,str(cnt_)))
    set_.add(ret_)
    return ret_

for cnt_ in range(1,10001):
    if cnt_ not in set_:
        print(cnt_)
    while cnt_ < 10000:
        cnt_ = func_d(cnt_)
        if cnt_ in set_:
            break