# Kelvin Araújo Ferreira - 2019037653

import heapq

def heuristic(node, heuristic_dict):
    return heuristic_dict.get(node, float('inf'))

def a_star(graph, start, end, heuristic_dict):
    priority_queue = [(0, start)]
    visited = set()
    g = {start: 0}
    parent = {start: None}

    while priority_queue:
        _, current_node = heapq.heappop(priority_queue)
        if current_node == end:
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = parent[current_node]
            path.reverse()
            return path, g[end]

        visited.add(current_node)

        for neighbor, cost in graph[current_node].items():
            if neighbor in visited:
                continue

            tentative_g_score = g[current_node] + cost
            if tentative_g_score < g.get(neighbor, float('inf')):
                parent[neighbor] = current_node
                g[neighbor] = tentative_g_score
                f = tentative_g_score + heuristic(neighbor, heuristic_dict)
                heapq.heappush(priority_queue, (f, neighbor))

    return None, None

def main():
    with open('Romenia.txt', 'r') as f:
        romania_map = eval(f.read())
    
    with open('Heuristica.txt', 'r') as f:
        heuristic_dict = eval(f.read())

    start = 'Arad'
    end = 'Bucharest'

    path, cost = a_star(romania_map, start, end, heuristic_dict)

    if path is not None:
        print(f'Path found: {path}')
        print(f'Total cost: {cost}')
    else:
        print('Path not found')


if __name__ == '__main__':
    main()