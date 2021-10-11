from rich.markdown import Markdown
from rich.text import Text

class MDDisplay:
    def __init__(self):
        self.md = "# Hoge\n- aaa"

    def getMD(self) -> Markdown:
        return Markdown(self.md)
