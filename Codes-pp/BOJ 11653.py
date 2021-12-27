import sys

N_ = int(sys.stdin.readline())
div_ = 2
while N_ > 1:
    while not N_ % div_:
        print(div_)
        N_ //= div_
    div_ += 1
exit()

import sys

N_ = int(sys.stdin.readline())
lst_is_prime = [True for _ in range(N_ + 1)]
lst_is_prime[0], lst_is_prime[1] = False, False

for cand_prime in range(2, N_ + 1):
    if lst_is_prime[cand_prime]:
        temp_ = cand_prime + cand_prime
        while temp_ <= N_:
            lst_is_prime[temp_] = False
            temp_ += cand_prime
        while not N_ % cand_prime:
            print(cand_prime)
            N_ //= cand_prime
    if N_ == 1:
        break

exit()
