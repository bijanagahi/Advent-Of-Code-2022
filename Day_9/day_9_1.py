from Classes import Point, Direction

def solve(lines: list[str]) -> int:
    instructions: tuple[Direction, int] = [(Direction[pair[0]], int(pair[2:])) for pair in lines]
    seen: set[Point] = set()
    head = Point(0,0)
    tail = Point(0,0)

    seen.add(tail.asTuple()) # add the tail pos straight away
    direction: Direction
    units: int

    for direction, units in instructions:
        # Assume that the head/tail distance is already stable at this point.
        step: int
        for step in range(units):
            # 1) Move the head
            head.add(direction.toPoint())
            # 2) Check the distance and move tail if needed
            #   Threshold is >= 2
            distanceToTail: float = abs(head.distanceTo(tail))
            if distanceToTail >= 2:
                # Too far, need to move the tail.
                correction: Point = calculateCorrectionOffset(tail, head)
                tail.add(correction)
                seen.add(tail.asTuple())
    return len(seen)

def calculateCorrectionOffset(point: Point, target: Point) -> Point:
    '''Given a point and target, calculate what is needed to get the point to the target.'''
    offset: Point = Point.pointTo(point, target)
    nudge: int # min amount to change to get tail near the head
    # We know how to get to the target, but we want to only move once in each direction.
    # First check to ensure we're not too far off
    assert offset.x <=2 and offset.y <=2
    match offset:
        case Point(x=0, y=y):
            offset.y = 1 if y > 0 else -1
        case Point(x=x, y=0):
            offset.x = 1 if x > 0 else -1
        case Point(x=1, y=y) | Point(x=-1, y=y):
            offset.y = 1 if y > 0 else -1
        case Point(x=x, y=1) | Point(x=x, y=-1):
            offset.x = 1 if x > 0 else -1
        case _:
            print("Something is wrong")
            raise ValueError
    return offset



if __name__ == '__main__':
    lines: list[str] = [line.strip() for line in open("input.txt", "r").readlines()]
    print(solve(lines))

'''

H = (3,3)
T = (2,1)
Vector = (1,2)
 - need to add 1,1 to the tail

what about
H = (2,1)
T = (4,2) -> (3,1)
Vector = (-2,-1)
- need to add -1,-1 to the tail

4  . . . . . .
3  . . . . . . 
2  . . . . T . 
1  . . H . . . 
0  . . . . . .
   0 1 2 3 4 5


'''