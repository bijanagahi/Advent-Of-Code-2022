import re

'''
Here's the approach on this Dynamic Programming problem:
- Initialize two maps to keep track of valve flow rates and adjacent nodes (don't need a full graph here)
- Initialize the memoization array with each valve as a column, and each minute as a row.
- For each minute (row):
    - For each valve (column):
        - Check adjacent valves (including itself) in previous row:
            - If none are accessable, mark this valve as inaccessable and move on
            - If others were accessible but this one wasn't previously, mark as 0 and move on
            - this valve = max {
                            all other valves that don't include this valve + (this valve's flow rate * time remaining) |
                            this valve's previous value
                            }
'''

def solve(lines: list[str]):
    # We need two maps:
    flow_rates:dict[str, int] = dict() # associates each value with its flow rate
    adjacent_nodes:dict[str, list[str]] = dict() # get adjacent values for the given valve
    flow_rates, adjacent_nodes = parse_input(lines)
    # We'll also need a "2D array" to keep track of things. In reality, this is a list of dictionaries.
    #   Each row represents a time step. The dictionary is indexed by valve and contains
    #   a tuple of the best value (-1 for impossible), and a list of nodes turned on already
    default:tuple[int, list[str]] = (-1, [])
    grid:list[dict[str,tuple[int, list[str]]]] = []
    # init the first row (t=0)
    row:dict[str,tuple[int, list[str]]] = dict([(v,default) for v in flow_rates.keys()])
    row['AA'] = (0,[]) # we always start at AA
    grid.append(row) # honestly we may not need this...

    # Let's do this.
    t:int = 1 # time step
    total_time:int = 30 # mins
    while t < 5:
        print(f"*******TIME STEP: {t}**********")
        valve:str
        prev_row:dict[str,tuple[int, list[str]]] = grid[t-1]
        cur_row:dict[str, tuple[int, list[str]]] = dict()
        
        for valve in flow_rates.keys():
            print()
            # First check if we can access this node
            if max([prev_row[v][0] for v in adjacent_nodes[valve]+[valve]]) == -1:
                print(f"Can't reach valve {valve}. Marking as -1")
                cur_row[valve] = (-1, [])
                continue # none of the adjacent nodes are accessible, so neither is this one.
            
            # Now that we know it is accessible, we want to see if it's the first time we're here
            #    and if so, we just mark it as 0 and move on
            if prev_row[valve][0] == -1:
                print(f"Can reach valve {valve} but it's the first time")
                cur_row[valve] = (0, [])
                continue
            
            '''
            Now onto the tricky bit. Our current state is such that we know we can turn this valve on right now.
            But we don't know if that's the best move or not. Here are the steps:
            - Calculate the future value of turning this value on right now.
            - Add that value to the value(s) in the previous row for all valves that don't contain this valve in their list and are adjacent
            - To that list, add the previous value of this valve.
            - Get the max. Update this valve to be that
            '''
            flow:int = flow_rates[valve] * (total_time-t) # total flow if we opened right now
            print(f"Looking at {valve}. If opened, the total flow will be: {flow}")
            valid_adjecent_nodes:list[str] = list(filter(lambda x:prev_row[x][0]>=0,adjacent_nodes[valve]))
            valid_adjecent_nodes.append(valve)
            print("Valid adjacent nodes:", valid_adjecent_nodes)
            all_options:list[tuple[int, list[str]]] = [prev_row[v] for v in valid_adjecent_nodes]
            print("All options:",all_options)
            updated_options:list[tuple[int, list[str]]] = [option if valve in option[1] else (option[0]+flow,(option[1]+[valve])) for option in all_options]
            # now we just take the max of this and make it the value here.
            print("Updated options:",updated_options)
            chosen_option:tuple[int, list[str]] = max(updated_options, key=lambda x:x[0])
            cur_row[valve]=chosen_option

        print(f"*******END TIME STEP: {t}**********")
        grid.append(cur_row)
        t+=1
    # Let's check the results
    # for row in grid:
    #     print("Row:")
    #     print(row)
    print_grid(grid)








def parse_input(lines: list[str]) -> tuple[dict[str, int],dict[str, list[str]]]:
    '''Take the raw input line and return the flow rate and adjacent nodes dicts'''
    pattern = r'Valve (\w{2}) has flow rate=(\d*); tunnels? leads? to valves? (.*)$'
    flow_rate:dict[str, int] = dict()
    adjacent_nodes:dict[str, list[str]] = dict()
    line:str
    for line in lines:
        result:(re.Match[str]|None) = re.search(pattern,line)
        if result:
            assert len(result.groups()) == 3
            flow_rate[result.group(1)] = int(result.group(2))
            adjacent_nodes[result.group(1)] = result.group(3).split(', ')
    return flow_rate, adjacent_nodes

def print_grid(grid:list[dict[str,tuple[int, list[str]]]])->None:
    row:dict[str,tuple[int, list[str]]]
    i:int
    print('       |   ', end='')
    print('   '.join(x for x in grid[0].keys()))
    for i,row in enumerate(grid):
        print(f"Time {i} | ",end='')
        key:str
        value:tuple[int, list[str]]
        builder:str = ''
        for key,value in row.items():
            v:str = str(value[0]).zfill(4)
            builder+=v+' '
        print(builder)



if __name__ == '__main__':
    lines: list[str] = [line.strip()
                        for line in open("test.txt", "r").readlines()]
    print(solve(lines))
