num_com = int(input())
num_edge = int(input())

lst_edge = []
for _ in range(num_edge):
    temp_ = list(map(lambda x: int(x)-1, input().split()))
    lst_edge.append([min(temp_),max(temp_)])

set_visited = set()
def dfs(start):
    set_visited.add(start)
    for edge in lst_edge:
        if edge[0] == start and edge[1] not in set_visited:
            dfs(edge[1])
        elif edge[1] == start and edge[0] not in set_visited:
            dfs(edge[0])


dfs(0)

print(len(set_visited) - 1)
