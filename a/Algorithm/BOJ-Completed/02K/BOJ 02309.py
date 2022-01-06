from itertools import combinations as cb

lst_dwarves = []
for _ in range(9):
    lst_dwarves.append(int(input()))

for cb_ in cb(lst_dwarves, 7):
    if sum(cb_) == 100:
        for each_ in sorted(cb_):
            print(each_)
        break