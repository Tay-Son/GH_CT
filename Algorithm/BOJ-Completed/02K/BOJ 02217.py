import sys

num_input = int(sys.stdin.readline())
lst_rope = []
for _ in range(num_input):
    lst_rope.append(int(sys.stdin.readline()))

lst_rope.sort(reverse=True)

max_answer = 0
cnt_ = 0
for rope in lst_rope:
    cnt_ += 1
    max_answer = max(max_answer, cnt_ * rope)
print(max_answer)