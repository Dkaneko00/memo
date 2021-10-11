#!/usr/bin/python3

import typer
from rich import print
import mod.display
import mod.layout
import mod.table
import mod.key
import mod.markdown
from rich.console import Console
console = Console()

key = mod.key.Key()
table = mod.table.ListTable(key)
md = mod.markdown.MDDisplay()
layout = mod.layout.DisplayStyle(table, md)
app = typer.Typer()


@app.command("test")
def test():
    print("hoge")


@app.command("layout")
def show_list():
    display = mod.display.Display(layout)
    display.display()
    console.clear()


if __name__ == "__main__":
    app()

