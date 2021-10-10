import getch


class Key:
    def __init__(self):
        self.name = "hoge"
        self.input = ""
        self.isLoop = True
        self.cursor = 0
        self.valid_length = 0
        self.keyDown = [106, 14]
        self.keyUp = [107, 16]

    def getKey(self):
        self.input = ord(getch.getch())
        if self.input == 113:
            self.isLoop = False
        if self.input in self.keyDown:
            if not self.validation():
                self.cursor += 1
        if self.input in self.keyUp:
            if not self.validation():
                self.cursor -= 1

    def getValid(self, list):
        self.valid_length = len(list)

    def validation(self):
        if self.input in self.keyUp:
            if self.cursor - 1 < 0:
                print("test")
                self.cursor = self.valid_length - 1
                return True
        if self.input in self.keyDown:
            if self.cursor == self.valid_length - 1:
                print("test2")
                self.cursor = 0
                return True
        return False
