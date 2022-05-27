import sys

N_ = int(sys.stdin.readline())
lst_ = list(map(int, sys.stdin.readline().split()))
X_ = int(sys.stdin.readline())
lst_.sort()

print(lst_)

tot_ = 0
ptr_r = N_ - 1

for ptr_l in range(N_):
    if ptr_l == ptr_r:
        break
    else:
        while lst_[ptr_l] + lst_[ptr_r] > X_ and ptr_l < ptr_r - 1:
            ptr_r -= 1
        if lst_[ptr_l] + lst_[ptr_r] == X_:
            print(lst_[ptr_l], lst_[ptr_r])
            tot_ += 1
print(tot_)

exit()
