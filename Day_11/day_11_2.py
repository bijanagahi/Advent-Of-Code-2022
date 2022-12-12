'''
WARNING: This code uses Python's eval() method to dynamically create lamdas which get executed with zero guards.

This means that with a malicious puzzle input, arbitrary RCE is possible. USE AT YOUR OWN RISK and please check the input manually.
'''
from Classes2 import Item, Monkey
from typing import Callable
import random
from math import prod


def solve(lines: list[str]) -> int:
    '''
    Oh boy this'll be a fun one.
    Each "Monkey" in the input is defined with exactly 6 lines.
    We can extract relevant info from each of those lines with some pretty hacky slices.
    The goal here is to have zero human intervention with the input.
    '''
    monkeys: list[Monkey] = []
    monkey: Monkey
    item: Item
    target: int

    # Initialize all the Monkey objects.
    i: int = 0
    while i < len(lines):
        # Grab 6 lines at a time to create the monkey object
        monkey: Monkey = createMonkey(lines[i:i+6])
        monkeys.append(monkey)
        i += 7
    # This is the trick to this problem. You have to multiply all the divisors together to get a max modulo limit.
    # This only works because all the divisors given are prime, so they share no GCD except their product.
    modulo_limit: int = prod([monkey.divisor for monkey in monkeys])
    for monkey in monkeys:
        monkey.setModuloLimit(modulo_limit)

    # Rounds
    for i in range(10000):
        for monkey in monkeys:
            # Get all the items that need to be thrown at other monkeys
            targets: list[tuple[Item, int]] = monkey.inspect()
            for item, target in targets:
                monkeys[target].catch(item)

    monkey_businesses: list[int] = [monkey.items_inspected for monkey in monkeys]
    monkey_businesses.sort(reverse=True)
    print(monkey_businesses)
    return monkey_businesses[0]*monkey_businesses[1]


def createMonkey(lines: list[str]) -> Monkey:
    '''Lord forgive me for what is below.'''
    monkey_id: int
    starting_items: list[Item] = []
    operation_text: str
    divisor: int
    true_throw: int
    false_throw: int
    test_text: str
    for line in lines:
        match line[:4]:
            case "Monk":
                monkey_id = int(line.split(" ")[1][0])
            case "Star":
                starting_items = [Item(random.randint(100, 1000), int(_))
                                  for _ in line[16:].split(", ")]
            case "Oper":
                operation_text = f"lambda old:{line[17:]}"
            case "Test":
                divisor = int(line.split()[-1])
            case "If t":
                true_throw = int(line.split()[-1])
            case "If f":
                false_throw = int(line.split()[-1])
            case _:
                raise IndexError(
                    "Line doesn't match any set pattern. Accidentally included a newline?")
    test_text = f"lambda x: {true_throw} if x else {false_throw}"

    return Monkey(
        monkey_id,
        starting_items,
        operation_text,
        divisor,
        test_text
    )


if __name__ == '__main__':
    lines: list[str] = [line.strip()
                        for line in open("input.txt", "r").readlines()]
    print(solve(lines))
