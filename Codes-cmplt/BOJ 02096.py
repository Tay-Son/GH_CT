import sys

N_ = int(sys.stdin.readline())

t_a, t_b, t_c = map(int, sys.stdin.readline().split())
lst_dp_a = [t_a, t_b, t_c]
lst_dp_b = [t_a, t_b, t_c]

for _ in range(1, N_):
    t_a, t_b, t_c = map(int, sys.stdin.readline().split())
    lst_dp_a = [
        max(lst_dp_a[0], lst_dp_a[1]) + t_a,
        max(lst_dp_a) + t_b,
        max(lst_dp_a[1], lst_dp_a[2]) + t_c]
    lst_dp_b = [
        min(lst_dp_b[0], lst_dp_b[1]) + t_a,
        min(lst_dp_b) + t_b,
        min(lst_dp_b[1], lst_dp_b[2]) + t_c]

print(max(lst_dp_a), min(lst_dp_b))

exit()
