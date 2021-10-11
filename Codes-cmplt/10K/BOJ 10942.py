import sys

N = int(sys.stdin.readline())
lst_N = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
lst_M = []
lst_cache = [-1 for _ in range(2 * N - 1)]
for _ in range(M):
    S, E = map(lambda x: int(x) - 1, sys.stdin.readline().split())

    if lst_cache[S + E] == -1:
        sp_l = (S + E) // 2
        if (S + E) % 2:
            sp_r = sp_l + 1
        else:
            sp_r = sp_l

        offset_ = 0
        for _ in range(min(N - sp_r, sp_l + 1)):
            if lst_N[sp_l - offset_] == lst_N[sp_r + offset_]:
                offset_ += 1
            else:
                break

        if (S + E) % 2:
            lst_cache[S + E] = 2 * offset_
        else:
            lst_cache[S + E] = 2 * (offset_ - 1) + 1
    if E - S > lst_cache[S + E]:
        print(0)
    else:
        print(1)

exit()