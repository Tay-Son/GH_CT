import sys

lst_ = [('M', 1000), ('D', 500), ('C', 100), ('L', 50), ('X', 10), ('V', 5), ('I', 1)]


def AtoR_(str_):
    num_ = int(str_)
    str_out = ''
    for chr_, val_ in lst_:
        for _ in range(3):
            if num_ >= val_:
                str_out += chr_
                num_ -= val_
            else:
                break

    pass


def RtoA_(str_):
    pass
