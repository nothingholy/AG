def find_eulerian_tour(graph):
    stack = [];
    tour = []

    stack.append(graph[0][0])

    while len(stack) > 0:
        v = stack[len(stack) - 1]

        degree = get_degree(v, graph)

        if degree == 0:
            stack.pop()
            tour.append(v)
        else:
            index, edge = get_edge_and_index(v, graph)
            graph.pop(index)
            stack.append(edge[1] if v == edge[0] else edge[0])
    return tour


def get_degree(v, graph):
    degree = 0
    for (x, y) in graph:
        if v == x or v == y:
            degree += 1

    return degree


def get_edge_and_index(v, graph):
    edge = ();
    index = -1

    for i in range(len(graph)):
        if (v == graph[i][0] or v == graph[i][1]):
            edge, index = graph[i], i
            break

    return index, edge


graph = [(1, 2), (2, 3), (2, 13), (2, 5),
(12, 13), (11, 12), (10, 11), (9, 11),
(4, 6), (6, 9), (6, 7), (7, 8), (8, 9),(1, 13), (3, 12), (3, 4), (2, 4), (1, 13), (11, 13), (2, 5), (10, 13), (4, 5),(8, 13), (5, 7), (5, 6), (9, 10),(8,10)]

print((find_eulerian_tour(graph)))
