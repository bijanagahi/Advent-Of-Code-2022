lines = [line.strip() for line in open("input.txt", "r").readlines()]
print( sum([ord(_)-96 if _.islower() else ord(_)-38 for _ in [list(set(lines[i]).intersection(set(lines[i+1]),set(lines[i+2])))[0] for i in range(0,len(lines),3)]]) )
