from Classes import Node


def solve(lines: list[list[str]]) -> int:
    grid: list[list[Node]] = []
    start: Node = None
    end: Node = None
    for i in range(len(lines)):
        row: list[Node] = []
        for j in range(len(lines[i])):
            node: Node = Node((i, j), lines[i][j])
            match lines[i][j]:
                case 'S':
                    node.height = ord('a') # it's hacky okay
                    start = node
                case 'E':
                    node.height = ord('z')
                    end = node
            row.append(node)
        grid.append(row)
    assert (start is not None) and (end is not None), "Couldn't find the start or end!"
    # Okay we have the grid, but we need to keep track of our distance as we BFS.
    # This can be achieved by incrementing the num steps each time we pop from the queue
    visited: set[Node] = set()
    queue: list[tuple[Node,int]] = []
    current_distance: int = 0
    node: Node # keep track of current node
    queue.append((start,current_distance))
    visited.add(start)

    while queue:
        node, current_distance = queue.pop(0)
        # Are we at the end?
        if node.value == 'E':
            print(f"Done! Took {current_distance} steps")
            return current_distance
        for neighbor_node in getNeighbors(grid, *node.id):
            if neighbor_node in visited:
                continue

            visited.add(neighbor_node)
            queue.append((neighbor_node, current_distance+1))
    raise ValueError("wut.")



def getNeighbors(grid: list[list[Node]], i, j) -> list[Node]:
    '''Returns a list of neighbor nodes that are higher in elevation'''
    neighbor_coordinates: list[tuple[int, int]] = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    neighbor: tuple[int, int]
    neighbors: list[Node] = []
    node:Node
    current_node:Node = grid[i][j]
    for neighbor in neighbor_coordinates:
        new_i, new_j = (neighbor[0]+i, neighbor[1]+j)
        if new_i >= 0 and new_i < len(grid) and new_j >= 0 and new_j < len(grid[i]):
            # It's a valid coordiante, but is it a valid node (elevation check)
            node = grid[new_i][new_j]
            if node.height <= current_node.height+1:
                neighbors.append(node)
    return neighbors


if __name__ == '__main__':
    lines: list[list[str]] = [
        list(_) for _ in [line.strip() for line in open("input.txt", "r").readlines()]]
    print(solve(lines))
