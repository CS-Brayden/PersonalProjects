from .ConsoleInterface import ConsoleInterface

class MenuInterface:
    def __init__(self, mainPrompt, optionPrompt, menuOptions):
        self.mainPrompt = mainPrompt
        self.optionPrompt = optionPrompt
        self.options = dict()
        for option in menuOptions:
            self.options.update({option.optionSymbol : option})
        
    def UtiliseMenu(self):
        while True:
            self._DisplayPrompts()
            selectedOption = self._SelectOption()
            selectedOption.UtiliseOption()
            if selectedOption.shouldCloseOption: break
            ConsoleInterface.ReadHotkey("Press any button to continue: ")

    def _DisplayPrompts(self):
        print("--------------------------")
        print(self.mainPrompt)
        for symbol, option in self.options.items():
            print(f"{symbol}) {option.optionName}")
        print("--------------------------")

    def _SelectOption(self, invalidOption = "Invalid option"):
        while True:
            selectedValue = ConsoleInterface.ReadRequiredHotkey(self.optionPrompt, self.options.keys(), invalidOption)
            try:
                if selectedValue not in self.options: raise ValueError(invalidOption)
                return self.options[selectedValue]
            except ValueError as argumentException:
                print(argumentException)