from copy import copy

class Sprite:
    def __init__(self, xPos:int) -> None:
        self.xPos:int = xPos
    
    def getPixel(self, cycle:int) -> str:
        return "#" if cycle in [self.xPos-1, self.xPos, self.xPos+1] else "."
    
    def setXPos(self, newXPos: int) -> None:
        self.xPos = newXPos

class CRT:

    _WIDTH: int = 40 # Class variable

    def __init__(self) -> None:
        self.rows: list[list[str]] = []
        self.current_row: list[str] = []
        self.pos: int = 0

    def addPixel(self, pixel: str) -> None:
        self.current_row.append(pixel)
        self.pos += 1
        if self.pos >= self._WIDTH:
            self.rows.append(copy(self.current_row)) # This gave me so much trouble because of python's reference handling.
            self.current_row.clear()
            self.pos = 0
    
    def getCurrentPos(self)->int:
        return self.pos
    
    def __str__(self) -> str:
        return '\n'.join([''.join(row) for row in self.rows])

def solve(lines: list[str])-> int:
    register: int = 1 # starting value of 1
    sprite: Sprite = Sprite(register)
    crt = CRT()

    for instruction in [list(_.split()) for _ in lines]:
        match instruction:
            case [_, value]:
                # Add instruction takes two cycles.
                # Draw one pixel, then increment pos (internally).
                crt.addPixel(sprite.getPixel(crt.getCurrentPos()))
                # Draw again, since the registers haven't been updated.
                crt.addPixel(sprite.getPixel(crt.getCurrentPos()))
                # now update the register (and the sprite)
                register+=int(value)
                sprite.setXPos(register)
            case [_]:
                # Noop instruction takes one cycle.
                # Draw a pixel then increment the pos (internally)
                crt.addPixel(sprite.getPixel(crt.getCurrentPos()))
    print(crt)
    return ''

if __name__ == '__main__':
    lines: list[str] = [line.strip() for line in open("input.txt", "r").readlines()]
    print(solve(lines))