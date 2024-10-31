import random

random.seed(3141592651296)


def generate_graph(
    n: int,
    extra_edges: int = 0,
    m: int = None,
    random_shuffle: bool = False,
) -> list[tuple[int, int]]:
    """
    Генерирует двудольный грф

    Параметры:\\
    n (int): Общее количество вершин. \\
    extra_edges (int): Кол-во дополнительных случайных ребер в графе.\\
    m (int): Общее количество ребер в графе, если задано то в графе будет ровно m ребер. Не гарантируется что граф будет двудольным . \\
    random_shuffle (bool) : перемешать у части ребер порядок вершин.\\

    Возвращает:\\
    list[tuple[int, int]]: Список ребер графа.
    """
    n1 = random.randint(1, n // 2)  # Размер первого королевства
    n2 = n - n1  # Размер второго королевства

    cities = list(range(1, n + 1))
    random.shuffle(cities)

    kingdom1 = cities[:n1]
    kingdom2 = cities[n1:]

    edges = set()

    for i in range(min(n1, n2)):
        edges.add((kingdom1[i], kingdom2[i]))

        if i != min(n1, n2) - 1:
            edges.add((kingdom1[i + 1], kingdom2[i]))

        if m is not None and len(edges) == m:
            break

    for i in range(min(n1, n2), max(n1, n2)):

        if n1 > n2:
            edges.add((kingdom1[i], random.choice(kingdom2)))
        else:
            edges.add((random.choice(kingdom1), kingdom2[i]))

        if m is not None and len(edges) == m:
            break

    extra_edges = extra_edges if m is None else m - len(edges) + extra_edges

    if random_shuffle:
        list_edges = list(edges)
        for i in range(len(list_edges)):
            if random.choice([True, False]):
                list_edges[i] = (list_edges[i][1], list_edges[i][0])

        edges = set(list_edges)

    return list(edges)


def print_edges(edges: list[tuple[int, int]]):

    print(f"{len(edges)}")

    for edge in edges:
        print(f"{edge[0]} {edge[1]}")


def main():

    n = 3
    k = 2 # должно быть случайным от 1 до n
    
    edges = generate_graph(n)

    print(f"{n} {len(edges)} {k}")

    for edge in edges:
        print(f"{edge[0]} {edge[1]}")


if __name__ == "__main__":
    main()
