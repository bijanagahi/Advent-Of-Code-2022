from Classes1 import Point, Canvas

def solve(lines: list[str]) -> int:
    path: list[tuple[int, int]] = []
    paths: list[list[tuple[int, int]]] = []
    all_coordinates: list[tuple[int, int]] = []
    bouding_box: tuple[int, int, int, int] = None
    canvas:Canvas = Canvas()
    for line in lines:
        coordinates = [coordinate.split(',') for coordinate in line.split(' -> ')]
        start_point:Point = Point(int(coordinates[0][0]),int(coordinates[0][1]))
        canvas.startPath(start_point)
        for x, y in coordinates[1:]:
            point:Point = Point(int(x), int(y))
            canvas.addPoint(point)
        canvas.endPath()
    print(canvas)


def getBoundingBox(all_coordinates: list[tuple[int, int]]) -> tuple[int, int, int, int]:
    min_x: int = min([t[0] for t in all_coordinates])
    max_x: int = max([t[0] for t in all_coordinates])
    max_y: int = max([t[1] for t in all_coordinates])
    min_y: int = min([t[1] for t in all_coordinates])
    return (min_x, max_x, min_y, max_y)

def draw(bounding_box:tuple[int, int, int, int]):
    width: int = bounding_box[1] -bounding_box[0]
    height: int = bounding_box[3] - bounding_box[2]
    for y in range(height):
        print()
        for x in range(width):
            print('.',end='')
    print()

if __name__ == '__main__':
    lines: list[str] = [line.strip()
                        for line in open("test.txt", "r").readlines()]
    print(solve(lines))
