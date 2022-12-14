class Node:
    def __init__(self, id: tuple[int, int], value: str) -> None:
        assert(len(value) == 1)
        self.id: tuple[int, int] = id
        self.value: str = value
        self.height: int = ord(value.lower())
        self.distance = 0
    
    def __str__(self) -> str:
        return f"Node [{self.id}]: {self.value}|{self.height}"