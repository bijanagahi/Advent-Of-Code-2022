from copy import copy

def solve(lines: list[str]):
    pair:list[any]
    pairs: list[tuple[list[any], list[any]]]
    running_sum: int = 0
    for idx,i in enumerate(range(0,len(lines), 3)):
        left: list[any] = eval(lines[i]) # Oh boy here I go committing code atrocities again!
        right: list[any] = eval(lines[i+1]) # I sure hope you sanitized your input, I sure didn't!
        print()
        if compare(left, right):
            print(idx+1)
            running_sum += idx +1
    return running_sum
        

def compare(leftList:list[any]|int, rightList:list[any]|int)->bool:
    '''Compares two values, returns true if they're in the correct order and false if not'''
    print(f"Compare {leftList} vs {rightList}")
    if leftList == [] and rightList == []:
        return None
    elif leftList == []:
        return True
    elif rightList == []:
        return False
    left = leftList.pop(0)
    right = rightList.pop(0)
    print(f"  Comparing {left} vs {right}")
    # If both values are integers, the lower integer should come first.
    if isinstance(left, int) and isinstance(right, int):
        # print(f"Comparing {left} vs {right}")
        if left < right:
            return True
        if left > right:
            return False
        return compare(leftList, rightList)
    if isinstance(left, int) and isinstance(right, list):
        print(f"Mixed input, turning {left} into {[left]} | {left} vs {right}")
        left = [left]
        return compare(left, right)
    if isinstance(left, list) and isinstance(right, int):
        print(f"Mixed input, turning {right} into {[right]} | {left} vs {right}")
        right = [right]
        return compare(left, right)
    
    # Okay so now we have two lists.
    print(f"Got two lists: {left} vs {right}")
    # Is the left side empty?
    if left == []:
        return True
    # What about the right side?
    if right == []:
        return False
    # They've both got items in them still. Keep it rolling.
    result: bool|None = compare(left, right)
    # print(f"result is {result}.")
    # print(f"after result: {left} vs {right}")
    if result is not None:
        return result
    else:
        return compare(leftList, rightList)

    






if __name__ == '__main__':
    lines: list[str] = [line.strip()
                        for line in open("input.txt", "r").readlines()]
    print(solve(lines))

    # Bad guesses:
    # 4768 too low
