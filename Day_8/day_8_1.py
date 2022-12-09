def solve(lines: list[str]) -> int:
    grid: list[list[int]] = []
    for line in lines:
        grid.append([int(_) for _ in line])
    seen: int = len(grid[0])*2 + (len(grid)-2)*2
    for x in range(1,len(grid)-1):
        for y in range(1,len(grid[0])-1):
            if castRays(grid, x, y):
                seen+=1
    return seen

def castRays(grid: list[list[int]], x:int, y:int) -> bool:
    '''Cast a ray in each cardinal direction and return true if an edge is reached'''
    my_height: int = grid[x][y]
    # Cast ray right
    if my_height > max(grid[x][y+1:]):
        return True
    # Cast ray left
    if my_height > max(grid[x][:y]):
        return True
    # Cast ray up
    if my_height > max([_[y] for _ in grid[:x]]):
        return True
    # Cast ray down
    if my_height >  max([_[y] for _ in grid[x+1:]]):
        return True
    return False

if __name__ == '__main__':
    lines: list[str] = [line.strip() for line in open("input.txt", "r").readlines()]
    print(solve(lines))
