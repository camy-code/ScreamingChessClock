class Pause:
    def __init__(self) -> None:
        self.pause = False

    def toggle(self):
        self.pause = not self.pause
    
    def getPause(self):
        return self.pause

