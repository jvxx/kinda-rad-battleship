from typing import Iterator, List


class Board(object):

    def __init__(self, rows: int, cols: int, blank_char: str) -> None:
        self.rows = rows
        self.cols = cols
        self.blank_char = blank_char
        self.contents = [[[blank_char for col in range(cols)] for row in range(rows)] for thickness in range(2)]

    def __str__(self) -> str:
        space_length = ' ' * max([len(str(self.rows)), len(str(self.cols))])

        make_empty_grid = space_length * 2 + space_length.join((str(i) for i in range(self.cols))) + '\n'

        for row_index, row in enumerate(self):
            make_empty_grid += str(row_index) + space_length + space_length.join(row) + '\n'

        return make_empty_grid

    def __iter__(self) -> Iterator[List[str]]:
        return iter(self.contents)

    def __getitem__(self, index: int) -> List[str]:
        return self.contents[index]

    def is_in_bounds(self, row: int, col: int) -> bool:
        return (0 <= row < self.rows and
                0 <= col < self.cols)
