num_input = int(input())
for _ in range(num_input):
    x1, y1, x2, y2 = map(int, input().split())
    num_c = int(input())
    cnt_answer = 0
    for _ in range(num_c):
        x3, y3, r = map(int, input().split())
        if ((x3 - x1) ** 2 + (y3 - y1) ** 2 <= r ** 2) != ((x3 - x2) ** 2 + (y3 - y2) ** 2 <= r ** 2):
            cnt_answer += 1

    print(cnt_answer)