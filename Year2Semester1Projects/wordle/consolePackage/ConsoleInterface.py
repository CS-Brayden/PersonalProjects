from colorama import Fore, Style

class ConsoleInterface:
    @staticmethod
    def ReadRequiredValue(prompt, requiredValues, invalidInputMessage = "Invalid Input"):
        while True:
            try:
                readInput = input(prompt).lower()
                if readInput in requiredValues: return readInput
            except: pass
            print(invalidInputMessage)    

    @staticmethod
    def ReadWordleValue(prompt, requiredValues, 
                        invalidInputMessage = "Invalid Input",
                        invalidInputValidityMessage = "Invalid: must be an accepted term",
                        invalidLengthMessage = "Invalid: must have a length of 5"):
        while True:
            try:
                readInput = input(prompt).lower()
                possibleValue = readInput in requiredValues
                validLength = len(readInput) == 5
                if possibleValue and validLength: return readInput.upper()
                if not possibleValue: print(invalidInputValidityMessage)
                if not validLength: print(invalidLengthMessage)
            except: print(invalidInputMessage)
    
    @staticmethod
    def PrintColouredString(givenString, characterColourMatches):
        for characterIndex, character in enumerate(givenString):
            print(Fore.WHITE + characterColourMatches[characterIndex] + character, end="")
        print(Style.RESET_ALL)

    @staticmethod
    def ReadInteger(prompt, minValue = 1, invalidInputMessage = "Invalid Input"):
        while True:
            try:
                readInput = int(input(prompt))
                if readInput >= minValue: return readInput
            except: pass
            print(invalidInputMessage)