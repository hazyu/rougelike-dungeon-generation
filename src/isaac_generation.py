class Room:
    def __init__(
            self,
            left: bool = False,
            right: bool = False,
            up: bool = False,
            down: bool = False
        ) -> None:
            self.left = left
            self.right = right
            self.up = up
            self.down = down

class IsaacGeneration:
    def __init__(self) -> None:
        self.game_map = [["#" for _ in range(0, 9)] for _ in range(0, 8)]

        x = 4
        y = 4

        self.game_map[y][x] = "1" 
        self.render()

    def render(self):
        for row in self.game_map:
            print(" ".join(row))