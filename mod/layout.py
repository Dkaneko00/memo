from rich.layout import Layout


class DisplayStyle():
    def __init__(self, table, md):
        self.table = table
        self.md = md
        self.layout = Layout()

    def display_layout(self, key) -> Layout:
        self.layout.split_row(
            Layout(name="left"),
            Layout(name="right")
        )
        self.layout["right"].ratio = 2
        self.layout["left"].update(self.table.display_table())
        self.layout["right"].update(self.md.getMD())
        return self.layout
