import heapq


def greedy_best_first_search(graph, start, goal, heuristics):
    open_list = []
    heapq.heappush(open_list, (heuristics[start], start))
    came_from = {start: None}
    visited = set()

    while open_list:

        _, current = heapq.heappop(open_list)

        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = came_from[current]
            return path[::-1]

        visited.add(current)

        for neighbor, _ in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                came_from[neighbor] = current
                heapq.heappush(open_list, (heuristics[neighbor], neighbor))

    return None


if __name__ == "__main__":

    graph = {
        'A': [('B', 1), ('C', 1)],
        'B': [('A', 1), ('D', 1), ('E', 1)],
        'C': [('A', 1), ('F', 1)],
        'D': [('B', 1)],
        'E': [('B', 1), ('F', 1), ('G', 1)],
        'F': [('C', 1), ('E', 1)],
        'G': [('E', 1)]
    }

    heuristics = {
        'A': 5,
        'B': 4,
        'C': 6,
        'D': 5,
        'E': 2,
        'F': 3,
        'G': 0  # Goal node 'G'
    }

    start = 'A'
    goal = 'G'
    path = greedy_best_first_search(graph, start, goal, heuristics)

    if path:
        print("Path found:", path)
    else:
        print("No path found.")
