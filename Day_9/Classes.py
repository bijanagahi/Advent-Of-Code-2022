from math import sqrt
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
    
    def add(self, operand:"Point") -> None:
        self.x += operand.x
        self.y += operand.y
    
    def asTuple(self) -> tuple[int, int]:
        return tuple((self.x, self.y))
    
    def __str__(self) -> str:
        return f"[{self.x},{self.y}]"