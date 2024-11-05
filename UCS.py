import heapq


class Node:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost
        self.next = None

    def __lt__(self, other):
        return self.cost < other.cost


def UCS(start, goal, graph):
    priority_queue = []
    heapq.heappush(priority_queue, (0, start))

    costs = {start: 0}
    nodes = {start: Node(start, 0)}

    while priority_queue:
        current_cost, current_node = heapq.heappop(priority_queue)

        if current_node == goal:
            return reconstruct_path(nodes[current_node])

        for neighbor, cost in graph[current_node].items():
            new_cost = current_cost + cost
            if neighbor not in costs or new_cost < costs[neighbor]:
                costs[neighbor] = new_cost
                if neighbor not in nodes:
                    nodes[neighbor] = Node(neighbor, new_cost)
                nodes[neighbor].next = nodes[current_node]
                heapq.heappush(priority_queue, (new_cost, neighbor))

    return None


def reconstruct_path(goal_node):
    path = []
    costs = []
    current_node = goal_node
    total_cost = goal_node.cost

    while current_node:
        path.append(current_node.name)
        costs.append(current_node.cost)
        current_node = current_node.next

    return path[::-1], costs[::-1], total_cost


if __name__ == "__main__":

    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'D': 2, 'E': 5},
        'C': {'A': 4, 'D': 1},
        'D': {'B': 2, 'C': 1, 'E': 1},
        'E': {'B': 5, 'D': 1}
    }

    start_node = 'A'
    goal_node = 'E'
    path, costs, total_cost = UCS(start_node, goal_node, graph)

    if path:
        print("Path found:", ' -> '.join(path))
        print("Costs along the path:", costs)
        print("Total cost from {} to {}: {}".format(start_node, goal_node, total_cost))
    else:
        print("No path found.")
