from pyray import *
from isaac_generation import IsaacGeneration

def main():
    init_window(1280, 720, "Rougelike Dungeon Generation")

    generation = IsaacGeneration()

    while not window_should_close():
        begin_drawing()
        clear_background(WHITE)

        end_drawing()

    close_window()


if __name__ == "__main__":
    main()
