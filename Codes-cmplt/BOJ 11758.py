import sys

lst_p2 = []
for _ in range(3):
    lst_p2.append(list(map(int, sys.stdin.readline().split())))

val_a = lst_p2[0][0] * lst_p2[1][1] + lst_p2[1][0] * lst_p2[2][1] + lst_p2[2][0] * lst_p2[0][1]
val_b = lst_p2[1][0] * lst_p2[0][1] + lst_p2[2][0] * lst_p2[1][1] + lst_p2[0][0] * lst_p2[2][1]
temp_ = val_a - val_b

if temp_ > 0:
    print(1)
elif temp_ == 0:
    print(0)
else:
    print(-1)