import sys

n = int(sys.stdin.readline())
divider_ = 1000000007


def mat22_mult(mat22_a, mat22_b):
    mat22_output = [[0 for _ in range(2)] for _ in range(2)]

    mat22_output[0][0] = (mat22_a[0][0] * mat22_b[0][0] + mat22_a[0][1] * mat22_b[1][0]) % divider_
    mat22_output[0][1] = (mat22_a[0][0] * mat22_b[0][1] + mat22_a[0][1] * mat22_b[1][1]) % divider_
    mat22_output[1][0] = (mat22_a[1][0] * mat22_b[0][0] + mat22_a[1][1] * mat22_b[1][0]) % divider_
    mat22_output[1][1] = (mat22_a[1][0] * mat22_b[0][1] + mat22_a[1][1] * mat22_b[1][1]) % divider_

    return mat22_output


mat22_answer = [[1,0],[0,1]]
mat22_input = [[1, 1], [1, 0]]

while n > 0:
    div_, mod_ = divmod(n, 2)
    if mod_:
        mat22_answer = mat22_mult(mat22_answer,mat22_input)
    mat22_input = mat22_mult(mat22_input, mat22_input)
    n = div_

print(mat22_answer[1][0])