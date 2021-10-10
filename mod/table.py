from rich.table import Table
import shutil

TABLE_WIDTH = (shutil.get_terminal_size().columns / 3 - 1)


class ListTable:
    def __init__(self, key):
        self.list = ["t1", "t2"]
        self.key = key
        self.key.getValid(self.list)

    def display_table(self) -> Table:
        table = Table(show_header=True, header_style="bold magenta",
                      width=TABLE_WIDTH)
        table.add_column("name", justify="right")
        for p in range(len(self.list)):
            if p == self.key.cursor:
                table.add_row(self.list[p], style="underline red on white")
            else:
                table.add_row(self.list[p])
        return table
