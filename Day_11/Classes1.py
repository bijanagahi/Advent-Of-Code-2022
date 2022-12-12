from typing import Callable
from copy import copy
import inspect


class Item:
    def __init__(self, value: int) -> None:
        self.value: int = value

    def __str__(self) -> str:
        return str(self.value)


class Monkey:
    def __init__(self,
                 id: int,
                 starting_items: list[Item],
                 operation_text: str,
                 divisor: int,
                 test_text: str) -> None:
        # This monkey's ID (for debugging)
        self.id: int = id
        # Items this monkey starts with
        self.items: list[Item] = starting_items
        # Function to modify the worry level after inspection
        self.operation_text: str = operation_text
        self.operation: Callable[[int], int] = eval(operation_text)
        # Test divisor which will influence where the item gets thrown
        self.divisor: int = divisor
        # Function to determine where the item gets thrown next.
        self.test_text = test_text
        self.test: Callable[[bool], int] = eval(test_text)

        self.items_inspected: int = 0  # How many items this monkey has inspected so far

    def catch(self, item: Item) -> None:
        self.items.append(item)

    def inspect(self) -> list[tuple[Item, int]]:
        '''Inspect all items in this monkeys queue and return a list of where to toss each item'''
        targets: list[tuple[Item, int]] = [
            self._inspect_one(item) for item in self.items]
        # clear this monkey's items
        self.items.clear()
        return targets

    def _inspect_one(self, item: Item) -> tuple[Item, int]:
        '''Inspect the oldest item in the queue and return the modified item and the id of the monkey to toss to.'''
        self.items_inspected+=1
        new_worry_level: int = self.operation(item.value) // 3
        # Update the item's value
        item.value = new_worry_level
        # Test the item and return the monkey to throw to
        target_monkey: int = self.test(not (item.value % self.divisor))
        return (item, target_monkey)

    def __str__(self) -> str:
        return f"Monkey {self.id}:" \
            f"\n  Starting items: {[str(item) for item in self.items]}" \
            f"\n  Operation: new = {self.operation_text[7:]}" \
            f"\n  Test: divisible by {self.divisor}" \
            f"\n    If true: throw to monkey {self.test(True)}"\
            f"\n    If false: throw to monkey {self.test(False)}"\
            f"\n ** Inspected {self.items_inspected} times"
