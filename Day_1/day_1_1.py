def solve():
	running_total = 0
	highest = 0
	elf = 1
	for line in [_.rstrip() for _ in open("input.txt",'r').readlines()]:
		if line == '':
			if running_total > highest:
				highest = running_total
				# print(f"New high total: {highest}")
			running_total = 0
			elf += 1
		else:
			running_total += int(line)
	print(highest)


if __name__ == '__main__':
	solve()