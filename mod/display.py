from rich.live import Live


class Display:
    def __init__(self, layout):
        self.layout = layout

    def display(self):
        with Live(self.layout.display_layout(self.layout.table.key), auto_refresh=False) as live:
            while(self.layout.table.key.isLoop):
                self.layout.table.key.getKey()
                live.update(self.layout.display_layout(
                    self.layout.table.key), refresh=True)
