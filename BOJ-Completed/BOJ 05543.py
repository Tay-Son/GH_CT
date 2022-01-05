lst_bg = []
lst_bv = []

for _ in range(3):
    lst_bg.append(int(input()))
for _ in range(2):
    lst_bv.append(int(input()))
print(min(lst_bg)+min(lst_bv)-50)
