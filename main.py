#!/usr/bin/python3

import typer
from rich import print
import mod.display
import mod.layout
import mod.table
import mod.key

key = mod.key.Key()
table = mod.table.ListTable(key)
layout = mod.layout.DisplayStyle(table)
app = typer.Typer()


@app.command("test")
def test():
    print("hoge")


@app.command("layout")
def show_list():
    display = mod.display.Display(layout)
    display.display()


if __name__ == "__main__":
    app()
