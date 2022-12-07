class File(object):
    def __init__(self, name, size) -> None:
        self.name = name
        self.size = size
    
    def getName(self):
        return self.name

    def getSize(self):
        return self.size

class Dir(object):
    def __init__(self, name, parent) -> None:
        self.name = name
        self.parent = parent
        self.files = []
        self.dirs = dict() # mapping from name to Dir object
    
    def addFile(self, file):
        self.files.append(file)

    def addDir(self, dirName):
        if dirName not in self.dirs:
            self.dirs.append(dir)
    
    # returns a list of filenames and directories within this directory
    def getLs(self):
        return ([file.getName() for file in self.files],list(self.dirs.keys()))

    def getParent(self):
        return self.parent

    def getName(self):
        return self.name

    def getSize(self):
        return sum([file.size() for file in self.files]) + sum([dir.size() for dir in self.dirs])

class FS(object):
    def __init__(self, root) -> None:
        self.dirs = dict() # holds a flatmap of all the directories for easy referencing
        self.current_dir = root # starts as "/"
    
    def pwd(self):
        return self.current_dir
    
    def cd(self, dirname):

    


def solve(lines):
    pass

if __name__ == '__main__':
  lines = [line.strip() for line in open("input.txt","r").readlines()]
  print(solve(lines))