from collections import deque

Graph = dict()
visited = []

def DFS(start):
    stack = []
    stack.append(start)
    while (len(stack) != 0):
        temp = stack.pop()
        if temp in visited:
            continue
        visited.append(temp)
        for i in Graph[temp]:
            stack.append(i)


def BFS(start):
    queue = []
    queue.append(start)
    while(len(queue) != 0):
        temp = queue.pop(0)
        if temp in visited:
            continue
        visited.append(temp)
        while(len(Graph[temp]) != 0):
            queue.append(Graph[temp].pop())



Flag = True
graph_type = ''
start_vertrex = ''
search_type = ''
init = False

while (Flag):
    try:
        str = input()
        str_spl = str.split()

        if (init == False):
            if (len(str_spl) == 3):
                graph_type = str_spl[0]
                start_vertrex = str_spl[1]
                search_type = str_spl[2]
                init = True
        else:
            if (str_spl[0] not in Graph):
                Graph[str_spl[0]] = [str_spl[1]]
            else:
                Graph[str_spl[0]].append(str_spl[1])
            if (graph_type == 'u'):
                if (str_spl[1] not in Graph):
                    Graph[str_spl[1]] = [str_spl[0]]
                else:
                    Graph[str_spl[1]].append(str_spl[0])
            else:
                if str_spl[1] not in Graph:
                    Graph[str_spl[1]] = []
    except Exception:
        Flag = False

if (init):
    for i in Graph:
        Graph[i].sort(reverse=True)
    if (search_type == 'd'):
        DFS(start_vertrex)
    elif (search_type == 'b'):
        BFS(start_vertrex)

    for v in visited:
        print(v)
