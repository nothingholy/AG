from queue import Queue

Graph = dict()
visited = dict()

output = []

def DFS(start):
    stack = []
    stack.append(start)

    while len(stack):
        v = stack.pop()

        if visited.get(v, None):
            continue

        visited[v] = 1
        output.append(v)

        for neighbour in Graph[v]:
            if not visited.get(neighbour, None):
                stack.append(neighbour)

def BFS(start):
    queue = Queue()
    queue.put(start)

    while not queue.empty():
        v = queue.get()

        if visited.get(v, None):
            continue

        visited[v] = 1
        output.append(v)

        for neighbour in Graph[v]:
            if not visited.get(neighbour, None):
                queue.put(neighbour)


Flag = True
init = False

while Flag:
    try:
        str = input()
        str_spl = str.split()

        if len(str_spl) == 3 and not init:
            graph_type = str_spl[0]
            start_vertex = str_spl[1]
            search_type = str_spl[2]
            init = True

        elif len(str_spl) == 2 and init:
            if str_spl[0] in Graph:
                if not str_spl[1] in Graph[str_spl[0]]:
                    Graph[str_spl[0]].append(str_spl[1])
            else:
                Graph[str_spl[0]] = [str_spl[1]]

            if graph_type == 'u':
                if str_spl[1] in Graph:
                    if not str_spl[0] in Graph[str_spl[1]]:
                        Graph[str_spl[1]].append(str_spl[0])
                else:
                    Graph[str_spl[1]] = [str_spl[0]]
            else:
                if str_spl[1] not in Graph:
                    Graph[str_spl[1]] = []
    except Exception:
        Flag = False

if init:
    if search_type == 'b':
        for i in Graph.values():
            i.sort()
        BFS(start_vertex)

    if search_type == 'd':
        for i in Graph.values():
            i.sort(reverse=True)
        DFS(start_vertex)

    for v in output:
        print(v)