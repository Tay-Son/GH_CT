num_tc = int(input())
for _ in range(num_tc):
    val_k = int(input())
    val_n = int(input())
    lst_ = [i for i in range(1, val_n + 1)]
    if val_k > 0:
        for _ in range(1, val_k + 1):
            lst_temp = []
            for idx_ in range(val_n):
                lst_temp.append(sum(lst_[:idx_ + 1]))
            lst_ = lst_temp
    print(lst_[-1])