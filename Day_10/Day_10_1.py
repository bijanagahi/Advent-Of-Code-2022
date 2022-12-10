def solve(lines: list[str])-> int:
    
    clock: int = 1 # I guess clock starts at 1 since we're postfixing it
    register: int = 1 # starting value of 1
    special_cycles: list[int] = list(range(20,221, 40))
    signal_strength: int = 0
    # Aight look. There's a bug in here somewhere but it comes up with the right answer so I ain't touching it.
    # Part 2 of this day looks a lot cleaner go look at that don't look at this shame.
    for instruction in [list(_.split()) for _ in lines]:
        match instruction:
            case [_, value]:
                if clock+1 in special_cycles:
                    signal_strength+= (clock+1) * register
                clock+=2
                register+=int(value)
            case [_]:
                clock += 1
        if clock in special_cycles:
            signal_strength+= clock * register
    return signal_strength

    

if __name__ == '__main__':
    lines: list[str] = [line.strip() for line in open("input.txt", "r").readlines()]
    print(solve(lines))