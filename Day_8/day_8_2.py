def solve(lines: list[str]) -> int:
    grid: list[list[int]] = []
    for line in lines:
        grid.append([int(_) for _ in line])
    best_tree = 0
    for x in range(1,len(grid)-1):
        for y in range(1,len(grid[0])-1):
            score: int = castRays(grid, x, y)
            if score >= best_tree:
                best_tree = score

    return best_tree

def castRays(grid: list[list[int]], x:int, y:int) -> int:
    '''Cast a ray in each cardinal direction and returns the viewing distances'''
    my_height: int = grid[x][y]
    scenic_score = 1 # not 0 since we're multiplying
    # Cast ray right
    scenic_score *= getViewDistance(my_height, grid[x][y+1:])
    # Cast ray left
    scenic_score *= getViewDistance(my_height, grid[x][:y], True)
    # Cast ray up
    scenic_score *= getViewDistance(my_height,[_[y] for _ in grid[:x]], True)
    # Cast ray down
    scenic_score *= getViewDistance(my_height,[_[y] for _ in grid[x+1:]])
    return scenic_score

def getViewDistance(my_height: int, trees: list[int], should_reverse:bool = False) -> int:
    '''Returns the number of trees this tree can see'''
    if should_reverse: # when viewing left and up this list slice is reversed
        trees.reverse()
    for i,tree in enumerate(trees):
        if my_height <= tree:
            return i+1 # viewing distance will always be at least 1
    return len(trees)

if __name__ == '__main__':
    lines: list[str] = [line.strip() for line in open("input.txt", "r").readlines()]
    print(solve(lines))
