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
    LOSS = "X"
    DRAW = "Y"
    WIN = "Z"
    
    def score(self):
        return (ord(self.value)-88)*3 # shift down to 0,1,2 and multiply by 3 to get actual score

def solve(lines):
    score = 0
    for line in lines:
        hand, result = (Hand(line.split()[0]), Result(line.split()[1]))
        response = getResponse(hand, result)
        score += result.score() + response.score()
    print(score)
        
def getResponse(hand, result):
    if result == Result.DRAW:
        return Response[hand.name]
    match (hand, result):
        case (Hand.ROCK, Result.WIN):
            return Response.PAPER
        case (Hand.ROCK, Result.LOSS):
            return Response.SCISSORS
        case (Hand.PAPER, Result.WIN):
            return Response.SCISSORS
        case (Hand.PAPER, Result.LOSS):
            return Response.ROCK
        case (Hand.SCISSORS, Result.WIN):
            return Response.ROCK
        case (Hand.SCISSORS, Result.LOSS):
            return Response.PAPER
        case _:
            raise ValueError()

if __name__ == '__main__':
  lines = [line.strip() for line in open("input.txt","r").readlines()]
  solve(lines)