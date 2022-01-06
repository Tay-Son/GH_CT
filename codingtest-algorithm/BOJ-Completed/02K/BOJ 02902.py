import sys

lst_input = sys.stdin.readline().split('-')
print(''.join([each_[0] for each_ in lst_input]))