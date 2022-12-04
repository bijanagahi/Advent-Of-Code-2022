from enum import Enum

class Hand(Enum):
    ROCK = "A"
    PAPER = "B"
    SCISSORS = "C"

    def score(self):
        return ord(self.value)-64 # shift down to 1,2,3

class Response(Enum):
    ROCK = "X"
    PAPER = "Y"
    SCISSORS = "Z"

    def score(self):
        return ord(self.value)-87 # shift down to 1,2,3
    
class Result(Enum):
    LOSS = 0
    DRAW = 1
    WIN = 2
    
    def score(self):
        return self.value * 3 # This is extra work, but keeps syntax consistent.

def solve(lines):
    score = 0
    for line in lines:
        opponent, player = (Hand(line.split()[0]), Response(line.split()[1]))
        result = getResult(opponent, player)
        score += player.score() + result.score()
    print(score)
        
def getResult(opponent, player):
    if opponent.name  == player.name:
        return Result.DRAW
    match (opponent, player):
        case (Hand.ROCK, _):
            match player:
                case Response.PAPER:
                    return Result.WIN
        case (Hand.PAPER, _):
            match player:
                case Response.SCISSORS:
                    return Result.WIN
        case (Hand.SCISSORS, _):
            match player:
                case Response.ROCK:
                    return Result.WIN
        case _:
            raise ValueError()
    return Result.LOSS

if __name__ == '__main__':
  lines = [line.strip() for line in open("input.txt","r").readlines()]
  solve(lines)