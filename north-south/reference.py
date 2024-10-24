
from generator import generate_graph , print_edges
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

def main():

    edges = generate_graph(8, random_shuffle=True)

    print_edges(edges)

    print( '-' * 10)

    solution = solve(edges)


    n = len(solution[0])
    m = len(solution[1])

    print(n, m)
    print(*sorted(solution[0]), sep=' ')
    print(*sorted(solution[1]), sep=' ')


if __name__ == "__main__":
    main()
