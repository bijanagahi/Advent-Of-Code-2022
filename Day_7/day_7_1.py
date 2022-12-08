from typing import Union

class File:
    def __init__(self, name: str, size: int) -> None:
        self.name: str = name
        self.size: int = size

    def getName(self) -> str:
        return self.name

    def getSize(self) -> int:
        return self.size


class Dir:
    def __init__(self, name: str, parent: Union[None, "Dir"]) -> None:
        self.name: str = name
        self.size: int = 0
        self.parent: Dir = parent
        self.files: list[File] = []
        self.dirs: dict[str, Dir] = dict()  # mapping from name to Dir object

    def addFile(self, file: File) -> None:
        self.files.append(file)
        self.updateSize(file.getSize())

    def addDir(self, dir: "Dir") -> None:
        self.dirs[dir.getName()] = dir
    
    def updateSize(self, size: int) -> None:
        print(f"Hi, I'm directory {self.getName()} and I'm adding {size} to my size ({self.size})")
        self.size += size
        if self.parent is not None:
            self.parent.updateSize(size)

    # returns a list of filenames and directories within this directory
    def getFiles(self) -> list[str]:
        return [file.getName() for file in self.files]

    def getDirs(self) -> dict[str, "Dir"]:
        return self.dirs

    def getParent(self) -> "Dir":
        return self.parent

    def getName(self) -> str:
        return self.name

    def getSize(self) -> int:
        return self.size

class FS:
    def __init__(self, root: Dir) -> None:
        self.current_dir: Dir = root  # starts as "/"
        self.root: Dir = root 

    def pwd(self) -> Dir:
        print(f"PWD: {self.current_dir.getName()}")
        return self.current_dir

    def ls(self) -> None:
        print(f"Files: {self.current_dir.getFiles()}")
        print(f"Directories: {self.current_dir.getDirs().keys()}")

    def cd(self, dirname: str) -> None:
        if dirname == "..":
            self.current_dir = self.current_dir.getParent()
            print(f"CD-ing up, new dir: {self.current_dir.getName()}")
            return
        dirname:str = self.current_dir.getName() + dirname + '/'
        if dirname in self.current_dir.getDirs():
            print(f"CD from {self.current_dir.getName()} into {dirname}")
            self.current_dir = self.current_dir.getDirs()[dirname]
        else:
            raise ValueError(f"Couldn't find directory name {dirname} within list of {self.current_dir.getDirs()}")

    def addFile(self, name: str, size: int) -> None:
        print(f"Adding file {name} | size {size}")
        if name not in self.current_dir.getFiles():
            self.current_dir.addFile(File(name, size))

    def addDir(self, name: str) -> None:
        print(f"Adding dir with name: {name}. Current path: {self.current_dir.getName()}")
        if name not in self.current_dir.getDirs():
            self.current_dir.addDir(Dir(self.current_dir.getName() + name + '/', self.current_dir))
    
    def getRootSize(self) -> int:
        return self.root.getSize()
    
    def traverse(self) -> int:
        q:list[Dir] = []
        seen: set[str] = set()
        low_ballers: list[int] = []

        q.append(self.root)
        while q:
            currentDir: Dir = q.pop()
            for name, dir in currentDir.getDirs().items():
                if name in seen:
                    continue
                seen.add(name)
                if dir.getSize() <= 100000:
                    low_ballers.append(dir.getSize())
                q.append(dir)
        return sum(low_ballers)



def solve(lines: list[str]) -> int:
    root: Dir = Dir('/', None)
    fs: FS = FS(root)
    fs.pwd()
    for line in lines[1:]:
        match (line[0:3]):
            case ("$ c"):
                fs.cd(line[5:])
            case ("$ l"):
                pass # don't care about ls
            case ("dir"):
                fs.addDir(line[4:])
            # Final case is a file
            case (_):
                size, name = line.split(" ")
                fs.addFile(name, int(size))
    return fs.traverse()

        


if __name__ == '__main__':
    lines: list[str] = [line.strip() for line in open("input.txt", "r").readlines()]
    print(solve(lines))
