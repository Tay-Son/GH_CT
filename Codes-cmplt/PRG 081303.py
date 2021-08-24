def solution(N_, K_, lst_cmd_set):
    lst_u = [cnt_ - 1 for cnt_ in range(N_)]
    lst_u[0] = -1
    lst_d = [cnt_ + 1 for cnt_ in range(N_)]
    lst_d[N_ - 1] = -1

    lst_is = [True for _ in range(N_)]
    stk_del = []
    for cmd_set in lst_cmd_set:
        cat_cmd = cmd_set.split()
        cmd_ = cat_cmd[0]
        if cmd_ == 'U':
            for _ in range(int(cat_cmd[1])):
                K_ = lst_u[K_]

        elif cmd_ == 'D':
            for _ in range(int(cat_cmd[1])):
                K_ = lst_d[K_]

        elif cmd_ == 'C':
            lst_is[K_] = False
            t_u = lst_u[K_]
            t_d = lst_d[K_]
            stk_del.append((K_, t_u, t_d))

            if t_d == -1:
                lst_d[t_u] = -1
                K_ = t_u
            else:
                if t_u == -1:
                    lst_u[t_d] = -1
                else:
                    lst_u[t_d] = t_u
                    lst_d[t_u] = t_d
                K_ = t_d

        else:
            idx_, t_u, t_d = stk_del.pop()
            lst_is[idx_] = True
            if t_u != -1:
                lst_d[t_u] = idx_
            if t_d != -1:
                lst_u[t_d] = idx_
        print(cmd_set, K_, ''.join(['O' if each_ else 'X' for each_ in lst_is]))
        print('u', lst_u)
        print('d', lst_d)
        print()

    return ''.join(['O' if each_ else 'X' for each_ in lst_is])


print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]))
