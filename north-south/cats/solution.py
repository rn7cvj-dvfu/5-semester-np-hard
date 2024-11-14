from collections import defaultdict, deque


def solve(edges):
    def is_bipartite(graph):
        color = {}
        for node in graph:
            if node not in color:
                queue = deque([node])
                color[node] = 0
                while queue:
                    current = queue.popleft()
                    for neighbor in graph[current]:
                        if neighbor not in color:
                            color[neighbor] = 1 - color[current]
                            queue.append(neighbor)
                        elif color[neighbor] == color[current]:
                            return False, {}
        return True, color

    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    is_bipartite_graph, color = is_bipartite(graph)

    if not is_bipartite_graph:
        raise ValueError("The graph is not bipartite")

    left_set = [node for node in color if color[node] == 0]
    right_set = [node for node in color if color[node] == 1]

    return [left_set, right_set]


example_number = int(input())

edges = [
    list(map(int, line.split()))
    for line in open("{}.in".format(str(example_number).rjust(2, "0")))
    .read()
    .splitlines()
]

solution = solve(edges[1:])

first = solution[0] if 1 in solution[0] else solution[1]
second = solution[0] if 1 not in solution[0] else solution[1]
 
 
print(len(first), len(second))
print(*sorted(first), sep=" ")
print(*sorted(second), sep=" ")
