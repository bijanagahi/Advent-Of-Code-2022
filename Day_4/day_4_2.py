def getSet(a):
    return set( range(int(a.split("-")[0]), int(a.split("-")[1])+1) )

def solve(lines):
    overlaps = 0
    for line in lines:
        a,b = line.split(",")
        set_a = getSet(a)
        set_b = getSet(b)
        if len(set_a.intersection(set_b)):
            overlaps += 1
        
    return overlaps

if __name__ == '__main__':
  lines = [line.strip() for line in open("input.txt","r").readlines()]
  print(solve(lines))