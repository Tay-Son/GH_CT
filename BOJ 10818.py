input()
str_input = input()
lst_input = [int(i) for i in str_input.split()]

print(min(lst_input), end=' ')
print(max(lst_input))