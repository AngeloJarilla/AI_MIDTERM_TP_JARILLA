import heapq

# Define the grid (0 = free cell, 1 = obstacle)
grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
]

start = (0, 0)  # Starting cell
goal = (4, 4)   # Goal cell

# Heuristic function: Manhattan distance
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# A* search algorithm
def astar_search(grid, start, goal):
    open_set = []
    heapq.heappush(open_set, (0 + heuristic(start, goal), 0, start, [start]))
    visited = set()

    while open_set:
        f, g, current, path = heapq.heappop(open_set)

        if current == goal:
            return path

        if current in visited:
            continue
        visited.add(current)

        neighbors = [
            (current[0] + dx, current[1] + dy)
            for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]
            if 0 <= current[0] + dx < len(grid) and 0 <= current[1] + dy < len(grid[0])
        ]

        for neighbor in neighbors:
            if grid[neighbor[0]][neighbor[1]] == 0:
                heapq.heappush(open_set, (g + 1 + heuristic(neighbor, goal), g + 1, neighbor, path + [neighbor]))

    return None

# Run A* search
path = astar_search(grid, start, goal)

if path:
    print("Path found:")
    for step in path:
        print(step)
else:
    print("No path found.")

