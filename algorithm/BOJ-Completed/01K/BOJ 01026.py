input()
lst_a = list(map(int, input().split()))
lst_b = list(map(int, input().split()))

lst_a.sort()
lst_b.sort(reverse=True)

print(sum([lst_a[i] * lst_b[i] for i in range(len(lst_a))]))
