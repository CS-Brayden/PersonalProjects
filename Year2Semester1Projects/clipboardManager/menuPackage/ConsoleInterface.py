from keyboard import read_hotkey
from pygetwindow import getActiveWindowTitle
from time import sleep

class ConsoleInterface:
    @staticmethod
    def ReadRequiredValue(prompt, requiredValues, invalidInputMessage = "Invalid Input"):
        while True:
            try:
                readInput = input(prompt)
                if readInput in requiredValues: return readInput
            except: pass
            print(invalidInputMessage)

    def InConsole(): 
        consoleWindows = ["clipboardManager - Visual Studio Code",
                                          "C:\windows\py.exe"]
        return any(windowTitle in getActiveWindowTitle() for windowTitle in consoleWindows)

    @staticmethod
    def ReadHotkey(prompt, invalidInputMessage = "Invalid Input"):
        readInput = ""
        while True:
            try:
                if ConsoleInterface.InConsole(): print(prompt, end = "", flush = True)
                sleep(0.5)
                readInput =  read_hotkey(False)
                if ConsoleInterface.InConsole(): break
            except(KeyboardInterrupt): 
                readInput = "ctrl+c"
                if ConsoleInterface.InConsole(): break                
            except:
                if ConsoleInterface.InConsole(): print(invalidInputMessage)
        print(readInput)              
        return readInput
    
    @staticmethod
    def ReadLimitedHotkey(prompt, blockedValues, invalidInputMessage = "Invalid Input"):
        while True:
            try:
                readInput = ConsoleInterface.ReadHotkey(prompt, invalidInputMessage)
                if readInput not in blockedValues:
                    return readInput
            except:
                pass
            print(invalidInputMessage)

    @staticmethod
    def ReadRequiredHotkey(prompt, requiredValues, invalidInputMessage = "Invalid Input"):
        while True:
            try:
                readInput = ConsoleInterface.ReadHotkey(prompt, invalidInputMessage)
                if readInput in requiredValues:
                    return readInput
            except:
                pass
            print(invalidInputMessage)