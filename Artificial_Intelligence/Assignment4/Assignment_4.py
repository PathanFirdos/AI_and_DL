import heapq

# --- A* Algorithm Implementation ---
def a_star(start, goal, grid):
    rows, cols = len(grid), len(grid[0])

    # Manhattan distance heuristic
    def h(cell):
        return abs(cell[0] - goal[0]) + abs(cell[1] - goal[1])

    # Movements (4 directions: up, down, left, right)
    directions = [(0,1),(1,0),(0,-1),(-1,0)]

    # Open set as a priority queue
    open_set = []
    heapq.heappush(open_set, (h(start), 0, start))  # (f, g, node)

    came_from = {}
    g_score = {start: 0}

    while open_set:
        f, g, current = heapq.heappop(open_set)

        if current == goal:
            # reconstruct path
            path = [current]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            return path[::-1]  # reverse path

        for dx, dy in directions:
            neighbor = (current[0] + dx, current[1] + dy)
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and grid[neighbor[0]][neighbor[1]] == 0:
                tentative_g = g_score[current] + 1
                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    g_score[neighbor] = tentative_g
                    f_score = tentative_g + h(neighbor)
                    heapq.heappush(open_set, (f_score, tentative_g, neighbor))
                    came_from[neighbor] = current

    return None  # no path found


# --- Example Usage ---
if __name__ == "__main__":
    # 0 = free cell, 1 = obstacle
    grid = [
        [0, 0, 0, 0, 0],
        [1, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0]
    ]

    start = (0, 0)  # top-left
    goal = (4, 4)   # bottom-right

    path = a_star(start, goal, grid)
    print("Shortest Path using A*:", path)
