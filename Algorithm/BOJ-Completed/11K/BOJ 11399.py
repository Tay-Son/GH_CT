input()
lst_ = list(map(int, input().split()))
lst_.sort()
print(sum([sum(lst_[:x + 1]) for x in range(len(lst_))]))
