lst_ = [int(i) for i in input().split()]
print((lst_[0] + lst_[1])%lst_[2])
print(((lst_[0] % lst_[2]) + (lst_[1] % lst_[2]))%lst_[2] )
print((lst_[0] * lst_[1])%lst_[2])
print(((lst_[0] % lst_[2]) * (lst_[1] % lst_[2])) % lst_[2] )