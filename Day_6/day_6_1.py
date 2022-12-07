def solve(line):
    window = 4
    for start in range(len(line)):
        if len(set(line[start:start+window])) > 3:
            return start+window

if __name__ == '__main__':
  line = [line.strip() for line in open("input.txt","r").readlines()][0]
  print(solve(line))