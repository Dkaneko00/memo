#!/usr/bin/python3

import typer
import getch
from rich.live import Live
from rich.table import Table
from rich.console import Console
from rich.layout import Layout
from rich import print
import shutil

console = Console()
console.clear()
console.width
app = typer.Typer()
i = 0
c = 0
layout_master = Layout()


@app.command("test")
def test():
    typer.echo("test")


l = ["t1", "t2"]


@app.command("hoge")
def hoge():
    global c
    global i
    with Live(test2(), auto_refresh=False) as live:
        while(True):
            c = ord(getch.getch())
            if c == 113:
                console.clear()
                break
            if c == 106:
                i += 1
            if c == 107:
                i -= 1
            live.update(test2(), refresh=True)


@app.command("layout")
def layout():
    global c
    global i
    with Live(lay(), auto_refresh=False) as live:
        while(True):
            c = ord(getch.getch())
            if c == 113:
                console.clear()
                break
            if c == 106:
                i += 1
            if c == 107:
                i -= 1
            live.update(lay(), refresh=True)


def lay() -> Layout:
    layout_master.split_row(
        Layout(name="left"),
        Layout(name="right")
    )
    layout_master["right"].ratio = 2
    layout_master["left"].update(test2())
    print(layout_master)
    return layout_master


def test2() -> Table:
    table = Table(show_header=True, header_style="bold magenta", width=shutil.get_terminal_size().columns/3 - 1)
    table.add_column("name", justify="right")
    for p in range(len(l)):
        if p == i:
            table.add_row(l[p], style="underline red on white")
        else:
            table.add_row(l[p])
    return table


if __name__ == "__main__":
    app()
