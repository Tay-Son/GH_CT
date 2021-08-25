import sys

N_, K_ = map(int, sys.stdin.readline().split())

lst_ = list(range(1, N_ + 1))

ptr_ = N_-1
ptr_target = 0
while K_ > 0:
    if ptr_-ptr_target <= K_:
        lst_.insert(ptr_target, lst_.pop(ptr_))
        K_ -= ptr_-ptr_target
        ptr_target += 1
    else:
        ptr_ -= 1

print(' '.join(map(str, lst_)))
exit()