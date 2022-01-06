import sys

N_ = int(sys.stdin.readline())
M_ = int(sys.stdin.readline())
str_ = sys.stdin.readline().rstrip()

lst_aux = ['O', 'I']
curr_target = 1
cnt_ = 0
lst_ = []
for chr_ in str_:
    if chr_ == lst_aux[curr_target]:
        cnt_ += 1
        curr_target ^= 1
    else:
        if cnt_ >= 3:
            lst_.append((cnt_ - 1) // 2)
        if curr_target == 0:
            cnt_ = 1
        else:
            curr_target = 1
            cnt_ = 0
if cnt_ >= 3:
    lst_.append((cnt_ - 1) // 2)

tot_ = 0
for each_ in lst_:
    tot_ += max(0, each_ + 1 - N_)
print(tot_)

exit()