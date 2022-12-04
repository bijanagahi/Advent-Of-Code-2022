def solve():
  running_total = 0
  totals = []
  elf = 1
  for line in [_.rstrip() for _ in open("input.txt",'r').readlines()]:
    if line == '':
      totals.append(int(running_total))
      running_total = 0
    else:
      running_total += int(line)
  totals.sort()
  print(sum(totals[-3:]))


if __name__ == '__main__':
  solve()