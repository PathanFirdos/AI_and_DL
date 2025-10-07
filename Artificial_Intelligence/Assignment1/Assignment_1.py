from collections import deque


GOAL_STATE = "123456780"

MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def get_neighbors(state):
    neighbors = [] 
    zero_idx = state.index("0")
    x, y = divmod(zero_idx, 3)
    for dx, dy in MOVES:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_idx = nx * 3 + ny
            new_state = list(state)
            new_state[zero_idx], new_state[new_idx] = new_state[new_idx], new_state[zero_idx]
            neighbors.append("".join(new_state))
    return neighbors

def reconstruct_path(parents, state):
    path = []
    while state is not None:
        path.append(state)
        state = parents[state]
    return path[::-1]

def bfs(start):
    queue = deque([start])
    visited = set([start])
    parents = {start: None}
    
    while queue:
        current = queue.popleft()
        if current == GOAL_STATE:
            return reconstruct_path(parents, current)
        for neighbor in get_neighbors(current):
            if neighbor not in visited:
                visited.add(neighbor)
                parents[neighbor] = current
                queue.append(neighbor)
    return None

def dfs(start, depth_limit=30):
    stack = [(start, 0)]
    visited = set()
    parents = {start: None}
    
    while stack:
        current, depth = stack.pop()
        if current == GOAL_STATE:
            return reconstruct_path(parents, current)
        if current not in visited and depth <= depth_limit:
            visited.add(current)
            for neighbor in reversed(get_neighbors(current)):  # reversed for consistent DFS order
                if neighbor not in visited:
                    parents[neighbor] = current
                    stack.append((neighbor, depth + 1))
    return None

def print_solution(path):
    for idx, state in enumerate(path):
        print(f"Step {idx}:")
        print(state[0:3])
        print(state[3:6])
        print(state[6:9])
        print()

def main():
    start_state = input("Enter start state as 9 digits (use 0 for blank): ").strip()
    method = input("Choose method (bfs / dfs): ").strip().lower()

    if method == "bfs":
        solution = bfs(start_state)
    elif method == "dfs":
        depth_limit = int(input("Enter depth limit for DFS (e.g., 20): "))
        solution = dfs(start_state, depth_limit=depth_limit)
    else:
        print("Invalid method.")
        return

    if solution:
        print(f"\nSolution found in {len(solution) - 1} steps:\n")
        print_solution(solution)
    else:
        print("No solution found (or depth limit too low for DFS).")


if __name__ == "__main__":
    main()
