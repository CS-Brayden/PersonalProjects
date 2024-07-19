from menuPackage.MenuOption import AbstractMenuOption
from menuPackage.ConsoleInterface import ConsoleInterface
from .CustomClipboard import CustomClipboard
from .ClipboardCollectionSession import ClipboardCollectionSession
from .ClipboardDatabase import ClipboardDatabase

class CreateClipboardMenuOption(AbstractMenuOption):
    def __init__(self):
        super().__init__("n", "Create new shortcut")
    def UtiliseOption(self):
        while True:
            copyInput = ConsoleInterface.ReadLimitedHotkey(
                "Please enter a copy hotkey (x to cancel): ",
                ClipboardCollectionSession.GetShortcuts(),
                "A shortcut cannot be used in multiple clipboards")
            if copyInput == "x": return
            pasteInput = ConsoleInterface.ReadLimitedHotkey(
                "Please enter a paste hotkey (x to cancel): ",
                ClipboardCollectionSession.GetShortcuts() + [copyInput],
                "A shortcut cannot be used in multiple clipboards or equal the copy hotkey")
            if pasteInput == "x": return            
            try:
                customClipboard = CustomClipboard(copyInput, pasteInput)
                ClipboardCollectionSession.StoreClipboard(customClipboard)
                print(f"Created ({customClipboard})")
                break
            except ValueError as invalidOption:
                print(invalidOption)

class DisplayClipboardsMenuOption(AbstractMenuOption):
    def __init__(self):
        super().__init__("v", "View all shortcuts")
    def UtiliseOption(self):
        if ClipboardCollectionSession.IsEmpty():
            print("No custom shortcuts created")
            return
        for clipboard in ClipboardCollectionSession.GetClipboards():
            print(clipboard)

class SearchForClipboardMenuOption(AbstractMenuOption):
    def __init__(self):
        super().__init__("f", "Find a clipboard")
    def UtiliseOption(self):
        while True:
            if ClipboardCollectionSession.IsEmpty():
                print("There are no hotkeys to search")
                return
            hotkeyInput = ConsoleInterface.ReadRequiredHotkey(
                "Please enter a related hotkey (x to cancel): ",
                ClipboardCollectionSession.GetShortcuts() + ["x"])
            if hotkeyInput == "x": return
            try:
                print(ClipboardCollectionSession.GetClipboard(hotkeyInput))
                break
            except ValueError as invalidArgument:
                print(invalidArgument)

class RemoveClipboardMenuOption(AbstractMenuOption):
    def __init__(self):
        super().__init__("r", "Remove a custom shortcut")
    def UtiliseOption(self):
        if ClipboardCollectionSession.IsEmpty():
            print("There are no hotkeys to remove")
            return
        while True:
            try:
                removeInput = ConsoleInterface.ReadRequiredHotkey(
                    "Remove all (a) or remove a hotkey (r) (x to cancel): ",
                    ["a", "r", "x"])
                if removeInput == "x": return
                if removeInput == "a":
                    ClipboardCollectionSession.RemoveAllClipboards()
                    print("Removed all shortcuts")
                    return
                if removeInput == "r":
                    hotkeyInput = ConsoleInterface.ReadRequiredHotkey(
                        "Please enter a clipboard's copy or paste hotkey (press x to cancel): ",
                        ClipboardCollectionSession.GetShortcuts() + ["x"])
                    if hotkeyInput == "x": return
                    clipboard = ClipboardCollectionSession.GetClipboard(hotkeyInput)
                    ClipboardCollectionSession.RemoveClipboard(clipboard)
                    print(f"Removed ({clipboard})")
                    break
                raise ValueError("Invalid option")
            except ValueError as invalidArgument:
                print(invalidArgument)

class ToggleClipboardsMenuOption(AbstractMenuOption):
    def __init__(self):
        super().__init__("t", "Toggle created shortcuts")
    def UtiliseOption(self):
        if ClipboardCollectionSession.IsEmpty():
            print("There are no hotkeys to toggle")
            return
        
        while True:
            try:
                toggleInput = ConsoleInterface.ReadRequiredHotkey(
                    "Activate all (a), deactivate all (d), activate a hotkey (n) , or deactivate"
                    + " a hotkey (v) (x to cancel): ",
                    ["a", "d", "n", "v", "x"])
                if toggleInput == "x": return
                if toggleInput == "a":
                    ClipboardCollectionSession.ActivateAllClipboards()
                    print("Activated all shortcuts")
                    return
                if toggleInput == "d":
                    ClipboardCollectionSession.DeactivateAllClipboards()
                    print("Deactivated all shortcuts")
                    return
                hotkeyInput = ConsoleInterface.ReadRequiredHotkey(
                    "Please enter a clipboard's copy or paste hotkey (x to cancel): ",
                    ClipboardCollectionSession.GetShortcuts() + ["x"])
                if hotkeyInput == "x": return
                clipboard = ClipboardCollectionSession.GetClipboard(hotkeyInput)
                if toggleInput == "n":
                    clipboard.Activate()
                    print(f"Activated {clipboard}")
                    break
                elif toggleInput == "v":
                    clipboard.Deactivate()
                    print(f"Deactivated {clipboard}")
                    break
                else: raise ValueError("Invalid option")
            except ValueError as invalidArgument:
                print(invalidArgument)

class EditClipboardMenuOption(AbstractMenuOption):
    def __init__(self):
        super().__init__("e", "Edit a custom shortcut")
    def UtiliseOption(self):
        if ClipboardCollectionSession.IsEmpty():
            print("There are no hotkeys to edit")
            return
        while True:
            try:
                originalHotkeyInput = ConsoleInterface.ReadRequiredHotkey(
                    "Please enter the original hotkey (x to cancel): ", 
                    ClipboardCollectionSession.GetShortcuts() + ["x"])
                if originalHotkeyInput == "x": return
                newHotkeyInput = ConsoleInterface.ReadLimitedHotkey(
                    "Please enter the new hotkey (x to cancel): ",
                    ClipboardCollectionSession.GetShortcuts(),
                    "The new hotkey cannot be used in multiple clipboards or equal itself") 
                if newHotkeyInput == "x": return       
                clipboard = ClipboardCollectionSession.GetClipboard(originalHotkeyInput)
                originalClipboard = str(clipboard)
                clipboard.UpdateShortcut(originalHotkeyInput, newHotkeyInput)
                print(f"Updated from ({originalClipboard}) to ({clipboard})")
                break
            except ValueError as invalidArgument:
                print(invalidArgument)

class SaveClipboardMenuOption(AbstractMenuOption):
    def __init__(self):
        super().__init__("s", "Save Clipboards to database")
    def UtiliseOption(self):
        print("Only the current hotkeys are saved, any previous hotkeys will be removed")
        confirmInput = ConsoleInterface.ReadHotkey("Press any button to confirm (x to cancel): ")
        if confirmInput == "x": return
        clipboards = ClipboardCollectionSession.GetClipboards()
        try:
            ClipboardDatabase.StoreClipboardCollection(clipboards)
            print("The current clipboards have been saved")
        except Exception as databaseException:
            print(databaseException)

class LoadClipboardMenuOption(AbstractMenuOption):
    def __init__(self):
        super().__init__("l", "Load Clipboards from database")
    def UtiliseOption(self):
        print("Only the saved hotkeys will be loaded, any other current shortcuts are removed")
        print("The current shortcuts will be removed if there is no save")
        confirmInput = ConsoleInterface.ReadHotkey("Press any button to confirm (x to cancel): ")
        if confirmInput == "x": return
        backup = ClipboardCollectionSession.GetClipboards()
        ClipboardCollectionSession.RemoveAllClipboards()
        try:
            clipboards = ClipboardDatabase.LoadClipboardCollection()
            ClipboardCollectionSession.SetClipboardCollection(clipboards)
            print("The saved clipboards have been loaded")
        except Exception as databaseException:
            print(databaseException)
            ClipboardCollectionSession.SetClipboardCollection(backup)