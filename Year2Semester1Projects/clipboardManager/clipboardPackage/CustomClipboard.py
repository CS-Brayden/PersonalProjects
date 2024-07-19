from .ClipboardCollectionSession import ClipboardCollectionSession
from menuPackage.ConsoleInterface import ConsoleInterface 
from keyboard import add_hotkey, remove_hotkey, release, press_and_release
from pyperclip import copy, paste
from time import sleep

class CustomClipboard:
    def __init__(self, copyShortcut, pasteShortcut, active = True):
        existingShortcuts = ClipboardCollectionSession.GetShortcuts()
        if (copyShortcut in existingShortcuts or pasteShortcut in existingShortcuts or 
            copyShortcut == pasteShortcut): raise ValueError("Shortcuts must be new and unique")
        self.copyShortcut = copyShortcut
        self.pasteShortcut = pasteShortcut
        self.copied = ""
        self.active = False
        if active: self.Activate()

    def CopyTo(self):
        if ConsoleInterface.InConsole(): return
        inClipboard = paste()
        release(self.copyShortcut)
        sleep(0.1)
        press_and_release("ctrl+c")
        sleep(0.1)
        if paste() != inClipboard: self.copied = paste()
        copy(inClipboard)

    def PasteFrom(self):
        if ConsoleInterface.InConsole(): return
        inClipboard = paste()
        copy(self.copied)
        release(self.pasteShortcut)
        sleep(0.1)
        press_and_release("ctrl+v")
        sleep(0.1)
        copy(inClipboard)

    def Activate(self):
        if not self.active:
            add_hotkey(self.copyShortcut, self.CopyTo)
            add_hotkey(self.pasteShortcut, self.PasteFrom)
            self.active = True

    def Deactivate(self):
        if self.active:
            remove_hotkey(self.copyShortcut)
            remove_hotkey(self.pasteShortcut)
            self.active = False

    def UpdateShortcut(self, originalHotkey, newHotkey):
        existingShortcuts = ClipboardCollectionSession.GetShortcuts()
        if (newHotkey in existingShortcuts or originalHotkey not in existingShortcuts): 
            raise ValueError("New shortcuts must be unique, original shortcut must exist")
        self.Deactivate()
        if originalHotkey == self.copyShortcut:
            self.copyShortcut = newHotkey
        if originalHotkey == self.pasteShortcut:
            self.pasteShortcut = newHotkey
        self.Activate()

    def __str__(self):
        return f"Copy: {self.copyShortcut} Paste: {self.pasteShortcut} Active: {self.active}"