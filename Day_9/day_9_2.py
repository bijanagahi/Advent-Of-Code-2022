from math import sqrt
from copy import copy
from enum import Enum

class Direction(Enum):
    R = (1,0)
    U = (0,1)
    L = (-1,0)
    D = (0,-1)

    def toPoint(self)->"Point":
        return Point.fromTuple(self.value)

class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x: int = x
        self.y: int = y
    
    @classmethod
    def fromTuple(cls, t:tuple)-> "Point":
        return cls(t[0],t[1])
    
    @classmethod
    def pointTo(cls, point: "Point", target: "Point") -> "Point":
        '''Returns a point which, when added to the first argument, gets to the target'''
        return cls(target.x - point.x, target.y - point.y)
    
    def distanceTo(self, target: "Point") -> int:
        return sqrt((target.x -self.x)**2 + (target.y - self.y)**2)
    
    def vectorTo(self, target: "Point") -> "Vector":
        return Vector(self, target)
    
    def add(self, operand:"Point") -> None:
        self.x += operand.x
        self.y += operand.y
    
    def asTuple(self) -> tuple[int, int]:
        return tuple((self.x, self.y))
    
    def __str__(self) -> str:
        return f"[{self.x},{self.y}]"


class Vector:
    def __init__(self, p1: Point, p2: Point) -> None:
        self.p1: Point = copy(p1) # Avoid reference errors here
        self.p2: Point = copy(p2)
    
    def distance(self) -> int:
        pass

def solve(lines: list[str]) -> int:
    instructions: tuple[Direction, int] = [(Direction[pair[0]], int(pair[2:])) for pair in lines]
    seen: set[Point] = set()
    head = Point(0,0)
    tail = Point(0,0)
    print(abs(head.distanceTo(tail)))

    seen.add(tail.asTuple()) # add the tail pos straight away
    direction: Direction
    units: int

    for direction, units in instructions:
        print(f"Starting instruction: {direction}, {units}. Head: {head}| Tail: {tail}")
        # Assume that the head/tail distance is already stable at this point.
        step: int
        for step in range(units):
            # 1) Move the head
            head.add(direction.toPoint())
            print(f"Stepping...step:{step}. Head: {head}| Tail: {tail}")
            # 2) Check the distance and move tail if needed
            #   Threshold is >= 2
            distanceToTail: float = abs(head.distanceTo(tail))
            print(f"Distance from head to tail: {distanceToTail}")
            if distanceToTail >= 2:
                # Too far, need to move the tail.
                correction: Point = calculateCorrectionOffset(tail, head)
                print(f"Correction point {correction}")
                tail.add(correction)
                seen.add(tail.asTuple())
    print(seen)
    return len(seen)

def calculateCorrectionOffset(point: Point, target: Point) -> Point:
    '''Given a point and target, calculate what is needed to get the point to the target.'''
    print("*****")
    offset: Point = Point.pointTo(point, target)
    nudge: int # min amount to change to get tail near the head
    # We know how to get to the target, but we want to only move once in each direction.
    # First check to ensure we're not too far off
    assert offset.x <=2 and offset.y <=2
    print(offset)
    match offset:
        case Point(x=0, y=y):
            print(f"We need to change the Y axis [{y}]")
            offset.y = 1 if y > 0 else -1
        case Point(x=x, y=0):
            print(f"We need to change the X axis [{x}]")
            offset.x = 1 if x > 0 else -1
        case Point(x=1, y=y) | Point(x=-1, y=y):
            print(f"We need to change the Y axis [{y}]")
            offset.y = 1 if y > 0 else -1
        case Point(x=x, y=1) | Point(x=x, y=-1):
            print(f"We need to change the X axis [{x}]")
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