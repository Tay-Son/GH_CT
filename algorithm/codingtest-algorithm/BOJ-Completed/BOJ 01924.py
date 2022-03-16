import sys

lst_d = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
lst_m = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

M, D = map(int, sys.stdin.readline().split())
print(lst_d[(sum(lst_m[:M - 1]) + D - 1) % 7])
