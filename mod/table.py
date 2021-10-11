from rich.table import Table
import shutil
import subprocess

TABLE_WIDTH = (shutil.get_terminal_size().columns / 3 - 1)
MEMO_PATH = '~/.memo/'


class ListTable:
    def __init__(self, key):
        self.list: list = self.getList()
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

    def getList(self) -> list:
        try:
            res = subprocess.check_output(
                'ls ' + MEMO_PATH, shell=True).decode("utf-8")
            print(res)
            print(type(res))
            res = self.createList(res)
            return res
        except:
            print("error")
            return

    def createList(self, res: str) -> list:
        res = res.split("\n")
        if not res[-1]:
            return res[:-1]
        else:
            print("false")
            return res
