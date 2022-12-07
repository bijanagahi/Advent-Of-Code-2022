def solve(line):
    window = 14
    for start in range(len(line)):
        if len(set(line[start:start+window])) > 13:
            return start+window

if __name__ == '__main__':
  line = [line.strip() for line in open("input.txt","r").readlines()][0]
  print(solve(line))