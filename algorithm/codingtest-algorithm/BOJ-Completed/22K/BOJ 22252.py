import sys
import heapq as hq

dct_g = dict()
tot_ = 0

for _ in range(int(sys.stdin.readline())):
    lst_input = sys.stdin.readline().split()
    com_ = lst_input[0]
    g_name = lst_input[1]
    if com_ == '1':
        if g_name not in dct_g:
            dct_g[g_name] = []
        for each_ in map(int, lst_input[3:]):
            hq.heappush(dct_g[g_name], -each_)
    else:
        if g_name in dct_g:
            print(g_name)
            for _ in range(int(lst_input[2])):
                if dct_g[g_name]:
                    tot_ -= hq.heappop(dct_g[g_name])
                    print(tot_)
                else:
                    break

print(tot_)
exit()
