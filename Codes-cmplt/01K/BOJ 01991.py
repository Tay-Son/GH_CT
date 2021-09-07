import sys

N = int(sys.stdin.readline())
dct_ = dict()
for _ in range(N):
    p_, ch_l, ch_r = sys.stdin.readline().split()
    dct_[p_] = (ch_l, ch_r)


def inorder(p_):
    if p_ != '.':
        ch_l, ch_r = dct_[p_]
        inorder(ch_l)
        print(p_, end='')
        inorder(ch_r)


def postorder(p_):
    if p_ != '.':
        ch_l, ch_r = dct_[p_]
        postorder(ch_l)
        postorder(ch_r)
        print(p_, end='')


def preorder(p_):
    if p_ != '.':
        ch_l, ch_r = dct_[p_]
        print(p_, end='')
        preorder(ch_l)
        preorder(ch_r)

preorder('A')
print()
inorder('A')
print()
postorder('A')
print()