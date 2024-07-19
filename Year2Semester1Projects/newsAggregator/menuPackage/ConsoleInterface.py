from keyboard import read_hotkey
from pygetwindow import getActiveWindowTitle
from time import sleep

class ConsoleInterface:
    @staticmethod
    def ReadValue(prompt, invalidInputMessage = "Invalid Input"):
        while True:
            try: return input(prompt)
            except: print(invalidInputMessage)

    @staticmethod
    def ReadRequiredValue(prompt, requiredValues, invalidInputMessage = "Invalid Input"):
        while True:
            try:
                readInput = input(prompt)
                if readInput in requiredValues: return readInput
            except: pass
            print(invalidInputMessage)

    @staticmethod
    def ReadLimitedValue(prompt, blockedValues, invalidInputMessage = "Invalid Input"):
        while True:
            try:
                readInput = input(prompt)
                if readInput not in blockedValues: return readInput
            except: pass
            print(invalidInputMessage)