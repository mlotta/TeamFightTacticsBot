import Utility.GameConstants as GameConstants


class PlayingBoard:
    def __init__(self, name):
        self.name = name

        w, h = GameConstants.BOARD_SIZE_WIDTH, GameConstants.BOARD_SIZE_HEIGHT
        self.board_slots = [[None for x in range(w)] for y in range(h)]

        bench_space = GameConstants.BENCH_SLOTS
        self.bench_slots = [None for x in range(bench_space)]

    def __str__(self):
        board_string = ""

        for row in self.board_slots:
            for col in row:
                board_string += str(col) + " "
            board_string += "\n"

        bench_string = ""

        for slot in self.bench_slots:
            bench_string += str(slot) + " "

        return "Board belongs to: " + self.name + "\n" + \
               "Board:\n" + board_string + \
               "Bench:\n" + bench_string
