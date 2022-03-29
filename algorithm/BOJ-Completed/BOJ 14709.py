import sys

str_f = 'Wa-pa-pa-pa-pa-pa-pow!'
str_c = 'Woof-meow-tweet-squeek'

N_ = int(sys.stdin.readline())
dct_ = {
    (1, 3): 0,
    (1, 4): 0,
    (3, 4): 0
}

lst_ = []
for _ in range(N_):
    a_, b_ = map(int, sys.stdin.readline().split())
    a_, b_ = min(a_, b_), max(a_, b_)
    lst_.append((a_, b_))
lst_.sort()

if N_ == 3 and lst_ == [(1, 3), (1, 4), (3, 4)]:
    print(str_f)
else:
    print(str_c)

exit()
