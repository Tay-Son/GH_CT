import sys

str_input = sys.stdin.readline().strip()
is_valid = True
set_ = set()
start_a, start_b = ord(str_input[0]), int(str_input[1])
curr_a, curr_b = start_a, start_b
set_.add((curr_a, curr_b))
for _ in range(35):
    str_input = sys.stdin.readline().strip()
    temp_a, temp_b = ord(str_input[0]), int(str_input[1])
    diff_a, diff_b = abs(curr_a - temp_a), abs(curr_b - temp_b)

    if (temp_a, temp_b) in set_ or diff_a + diff_b != 3 or diff_a == 0 or diff_b == 0:
        is_valid = False
        break
    curr_a, curr_b = temp_a, temp_b
    set_.add((curr_a, curr_b))

diff_a, diff_b = abs(curr_a - start_a), abs(curr_b - start_b)

if is_valid and diff_a + diff_b == 3 and diff_a != 0 and diff_b != 0:
    print('Valid')
else:
    print('Invalid')

exit()