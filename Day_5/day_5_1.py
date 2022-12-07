import re

INSTRUCTION_PATTERN = r"move (\d+) from (\d+) to (\d+)"

def solve(lines):
    # The 'front' of the stack is the top.
    stacks = [[] for i in range(9)]
    parse_idx = 0
    # https://media.tenor.com/Lf64P48TmqkAAAAC/aunty-donna-broden.gif
    for line in lines:
        parse_idx += 1
        if line[1] == '1':
            parse_idx += 1
            break
        for stack,i in enumerate( range(1,len(line),4)):
            if line[i] == ' ':
                continue
            stacks[stack].append(line[i])
    # parse_idx now points to the first instruction line
    instructions = parse_instructions(lines[parse_idx:])
    for count, src, dst in instructions:
        src -= 1
        dst -= 1
        for _ in range(count):
            stacks[dst].insert(0,stacks[src].pop(0))
    return(''.join([stack[0] for stack in stacks]))

def parse_instructions(lines):
    instructions = []
    for line in lines:
        instructions.append([int(_) for _ in re.findall(INSTRUCTION_PATTERN,line)[0]])
    return instructions


if __name__ == '__main__':
  lines = [line[:-1] for line in open("input.txt","r").readlines()]
  print(solve(lines))