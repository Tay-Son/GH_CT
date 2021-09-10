str_A = input()
str_B = input()

lst_B = [int(i) for i in str_B]
for each_B in reversed(lst_B):
    print(int(str_A)*each_B)
print(int(str_A)*int(str_B))
