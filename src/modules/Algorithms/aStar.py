import math


def astar(args):
    # Define parameters
    start = args[0]
    goal = args[1]
    grid = args[2]
    # Define the size of the grid
    rows = len(grid)
    cols = len(grid[0])

    # Define movement directions: up, down, left, right
    directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]

    # Manhattan distance
    def heuristic(node):
        return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

    open_set = [start]
    closed_set = []

    g_cost = [[math.inf] * cols for _ in range(rows)]
    g_cost[start[0]][start[1]] = 0

    parents = {}

    while open_set:
        # Find the node in the open set with the lowest f cost
        current = min(open_set, key=lambda x: g_cost[x[0]][x[1]] + heuristic(x))

        if current == goal:
            # Reconstruct the path
            path = []
            while tuple(current) in parents:
                path.append(current)
                current = parents[tuple(current)]
            path.append(start)

            # Reverse the order of coordinates to [x, y]
            path = [[coord[1], coord[0]] for coord in path]

            # Reverses path
            return path[::-1]

        open_set.remove(current)
        closed_set.append(current)

        # Explore neighbours
        for dx, dy in directions:
            neighbour = [current[0] + dx, current[1] + dy]

            # Check if neighbour is within bounds of the grid
            if 0 <= neighbour[0] < rows and 0 <= neighbour[1] < cols:
                # Check if neighbour is an obstacle or already visited
                if grid[neighbour[0]][neighbour[1]] == 1 or neighbour in closed_set:
                    continue

                tentative_g = g_cost[current[0]][current[1]] + 1

                # If neighbour not in open set or new path is shorter
                if neighbour not in open_set or tentative_g < g_cost[neighbour[0]][neighbour[1]]:
                    # Update parent and g cost
                    parents[tuple(neighbour)] = current
                    g_cost[neighbour[0]][neighbour[1]] = tentative_g

                    open_set.append(neighbour)

    return None
