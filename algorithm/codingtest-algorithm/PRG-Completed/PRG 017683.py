def music_parser(music_):
    dct_note = {'C': 'a',
                'C#': 'b',
                'D': 'c',
                'D#': 'd',
                'E': 'e',
                'F': 'f',
                'F#': 'g',
                'G': 'h',
                'G#': 'i',
                'A': 'j',
                'A#': 'k',
                'B': 'l'}
    str_result = ''
    curr_note = music_[0]
    if len(music_) > 1:
        for each_chr in music_[1:]:
            if each_chr == '#':
                curr_note += each_chr
            else:
                if curr_note in dct_note:
                    str_result += dct_note[curr_note]
                curr_note = each_chr
    if curr_note in dct_note:
        str_result += dct_note[curr_note]
    return str_result


def solution(music_, lst_musicinfo):
    str_answer = '(None)'

    str_music = music_parser(music_)
    lst_pi = [0 for _ in range(len(str_music))]

    ptr_b = 0
    for ptr_a in range(1, len(str_music)):
        while 0 < ptr_b and str_music[ptr_a] != str_music[ptr_b]:
            ptr_b = lst_pi[ptr_b - 1]
        if str_music[ptr_a] == str_music[ptr_b]:
            ptr_b += 1
            lst_pi[ptr_a] = ptr_b

    lst_musicinfo_parsed = []
    for musicinfo_ in lst_musicinfo:
        start_, end_, name_, music_contents = musicinfo_.split(',')
        lst_start = start_.split(':')
        lst_end = end_.split(':')
        start_ = int(lst_start[0]) * 60 + int(lst_start[1])
        end_ = int(lst_end[0]) * 60 + int(lst_end[1])
        running_time = end_ - start_
        str_music_contents = music_parser(music_contents)
        lst_musicinfo_parsed.append((running_time, name_, str_music_contents))

    lst_musicinfo_parsed.sort(key=lambda x: -x[0])

    is_ = False
    for running_time, name_, str_music_contents in lst_musicinfo_parsed:
        if is_:
            break
        else:
            rep_, rem_ = divmod(running_time, len(str_music_contents))
            str_full_music_contents = ''
            for _ in range(rep_):
                str_full_music_contents += str_music_contents
            str_full_music_contents += str_music_contents[:rem_]

            idx_p = 0
            for idx_t in range(len(str_full_music_contents)):
                while idx_p > 0 and str_full_music_contents[idx_t] != str_music[idx_p]:
                    idx_p = lst_pi[idx_p - 1]
                if str_full_music_contents[idx_t] == str_music[idx_p]:
                    if idx_p == len(str_music) - 1:
                        is_ = True
                        str_answer = name_
                        break
                    else:
                        idx_p += 1

    return str_answer

print(solution("AAAAA", ["12:00,12:06,HELLO,A", "13:00,13:05,WORLD,ABCDEF"]))
exit()

import sys

str_t = sys.stdin.readline().rstrip()
str_p = sys.stdin.readline().rstrip()

lst_pi = [0 for _ in range(len(str_p))]

ptr_b = 0
for ptr_a in range(1, len(str_p)):
    while ptr_b > 0 and str_p[ptr_a] != str_p[ptr_b]:
        ptr_b = lst_pi[ptr_b - 1]
    if str_p[ptr_a] == str_p[ptr_b]:
        ptr_b += 1
        lst_pi[ptr_a] = ptr_b

lst_ans = []
idx_p = 0
for idx_t in range(len(str_t)):
    while idx_p > 0 and str_t[idx_t] != str_p[idx_p]:
        idx_p = lst_pi[idx_p - 1]
    if str_t[idx_t] == str_p[idx_p]:
        if idx_p == len(str_p) - 1:
            lst_ans.append(idx_t - len(str_p) + 2)
            idx_p = lst_pi[idx_p]
        else:
            idx_p += 1

print(len(lst_ans))
print(' '.join(map(str, lst_ans)))
exit()
