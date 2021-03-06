# https://cyc1am3n.github.io/2019/04/26/bfs_dfs_with_python.html
#
from collections import deque

# graph = {1: set([3, 4]),
#               2: set([3, 4, 5]),
#               3: set([1, 5]),
#               4: set([1]),
#               5: set([2, 6]),
#               6: set([3, 5])}
graph = {1: {3, 4},
         2: {3, 4, 5},
         3: {1, 5},
         4: {1},
         5: {2, 6},
         6: {3, 5}
         }

root = 1


def BFS_with_adj_list(graph, root):
    visited = []
    queue = deque([root])

    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            queue += graph[n] - set(visited)
    return visited


print(BFS_with_adj_list(graph, root))
