from abc import ABC, abstractmethod

class AbstractMenuOption(ABC):
    def __init__(self, optionSymbol, optionName, shouldCloseOption = False):
        self.optionSymbol = optionSymbol
        self.optionName = optionName
        self.shouldCloseOption = shouldCloseOption
    @abstractmethod
    def UtiliseOption(self): pass

class TestMenuOption(AbstractMenuOption):   
    def __init__(self):
        super().__init__("t", "Test")

    def UtiliseOption(self):
        print("Test Message")

class ExitMenuOption(AbstractMenuOption):
    def __init__(self):
        super().__init__("x", "Exit", True)
    def UtiliseOption(self):
        print("Closing System!")