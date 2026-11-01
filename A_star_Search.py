import heapq

class Node:
    def __init__(self, state, parent, g, h):
        self.state = state
        self.parent = parent
        self.g = g
        self.h = h
        self.f = g + h

    def __lt__(self, other):
        return self.f < other.f


def a_star_search(start, goal, heuristic, neighbors):
    open_list = []
    heapq.heappush(
        open_list, Node(start, None, 0, heuristic(start, goal))
    )

    best_g = {start: 0}
    closed_list = set()

    while open_list:
        current = heapq.heappop(open_list)

        if current.g != best_g.get(current.state):
            continue

        if current.state == goal:
            path = []
            while current:
                path.append(current.state)
                current = current.parent
            return path[::-1]

        closed_list.add(current.state)

        for neighbor, cost in neighbors(current.state):
            new_g = best_g[current.state] + cost

            if new_g < best_g.get(neighbor, float("inf")):
                best_g[neighbor] = new_g
                h = heuristic(neighbor, goal)
                heapq.heappush(
                    open_list,
                    Node(neighbor, current, new_g, h)
                )
                closed_list.discard(neighbor)

    return None


def heuristic(state, goal):
    return abs(state[0] - goal[0]) + abs(state[1] - goal[1])


def neighbors(state):
    x, y = state
    moves = [
        (x + 1, y),
        (x - 1, y),
        (x, y + 1),
        (x, y - 1)
    ]

    return [
        (p, 1) for p in moves
        if 0 <= p[0] <= 3 and 0 <= p[1] <= 3
    ]


start = (0, 0)
goal = (3, 3)

path = a_star_search(start, goal, heuristic, neighbors)
print("Path from start to goal:", path)
