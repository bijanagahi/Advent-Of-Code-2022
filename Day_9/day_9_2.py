from Classes import Point, Direction

def solve(lines: list[str]) -> int:
    instructions: tuple[Direction, int] = [(Direction[pair[0]], int(pair[2:])) for pair in lines]
    seen: set[Point] = set()
    rope: list[Point] = [Point(0,0) for _ in range(10)]
    head = rope[0] 
    tail = rope[-1] # last element

    seen.add(tail.asTuple()) # add the tail pos straight away
    direction: Direction
    units: int

    for direction, units in instructions:
        # Assume that the head/tail(s) distance is already stable at this point.
        step: int
        for step in range(units):
            # 1) Move the head
            head.add(direction.toPoint())
            # 2) Check the distance and move tails if needed
            # iterate over all the tails, compare them to the previous item after moving them.
            for i in range(1,len(rope)):
                knot = rope[i]
                knot_in_front: Point = rope[i-1]
                distance_to_knot: float = abs(knot_in_front.distanceTo(knot))
                if distance_to_knot >= 2: # threshold to move knot
                    # Too far, need to move the tail.
                    correction: Point = calculateCorrectionOffset(knot, knot_in_front)
                    knot.add(correction)
            seen.add(tail.asTuple())
    return len(seen)

def calculateCorrectionOffset(point: Point, target: Point) -> Point:
    '''Given a point and target, calculate what is needed to get the point to the target.'''
    offset: Point = Point.pointTo(point, target)
    if abs(offset.x) == 2 and abs(offset.y) ==2: # long diagonal, easy case though.
        return Point(offset.x//2, offset.y//2)
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
            print(f"Something is wrong, calcualted offset is {offset}, point: {point}, target: {target}. Distance: {point.distanceTo(target)}")
            raise ValueError
    return offset



if __name__ == '__main__':
    lines: list[str] = [line.strip() for line in open("input.txt", "r").readlines()]
    print(solve(lines))
