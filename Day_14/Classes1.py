import math


class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x: int = x
        self.y: int = y

    def __str__(self) -> str:
        return f"[{self.x},{self.y}]"


class Canvas:
    def __init__(self) -> None:
        self.grid: list[list[str]]
        self.walls: set[tuple[int, int]] = set()

        self.sand_source: Point = Point(500, 0)
        self.min_x: int = 500
        self.max_x: int = 0
        self.min_y: int = 0
        self.max_y: int = 0

        self.prev_point:Point = None
    
    def startPath(self, start:Point) -> None:
        self._checkMinMax(start)
        self.prev_point = start

    def endPath(self) -> None:
        self.prev_point = None

    def addPoint(self, point:Point) -> None:
        assert self.prev_point is not None, "No current path to add to!"
        start = self.prev_point
        end = point
        self._checkMinMax(end)
        wall: list[tuple[int, int]]
        print(f"Start: {start} | End: {end}")
        # Determine the direction of the wall
        if start.x == end.x:
            # use y coords
            x: int = start.x
            wall = [(x, y) for y in range(start.y, end.y+1)]
            print(wall)
        elif start.y == end.y:
            # use y coords
            y: int = start.y
            wall = [(x, y) for x in range(start.x, end.x+1)]
            print(wall)
        self.walls.update(wall)
        self.prev_point = end

    def draw(self) -> None:
        width: int = self.max_x - self.min_x
        height: int = self.max_y - self.min_y
        for y in range(height):
            print()
            for x in range(width):
                print('.', end='')
        print()

    def _checkMinMax(self, *points: Point) -> None:
        for point in points:
            if point.x > self.max_x:
                self.max_x = point.x
            if point.x < self.min_x:
                self.min_x = point.x
            if point.y > self.max_y:
                self.max_y = point.y
            if point.y < self.min_y:
                self.min_y = point.y

    def __str__(self) -> str:
        return f"**Canvas**" \
            f"\nWalls: {self.walls}" \
            f"\nBounding Box: [{self.min_x},{self.max_x},{self.min_y},{self.max_y}]"
