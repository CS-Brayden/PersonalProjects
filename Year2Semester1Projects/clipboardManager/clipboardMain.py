#Perform documentation and test cases
from os import chdir, path
from menuPackage.MenuInterface import MenuInterface
from menuPackage.MenuOption import ExitMenuOption
from clipboardPackage.ClipboardMenuOption import (
    CreateClipboardMenuOption, DisplayClipboardsMenuOption, 
    RemoveClipboardMenuOption, ToggleClipboardsMenuOption, SearchForClipboardMenuOption,
    EditClipboardMenuOption, SaveClipboardMenuOption, LoadClipboardMenuOption
)

if __name__ == "__main__": 
    chdir(path.dirname(path.abspath(__file__)))
    menu = MenuInterface("Clipboard Manager", 
                         "Select an option: ",
                         [CreateClipboardMenuOption(),
                          EditClipboardMenuOption(),
                          RemoveClipboardMenuOption(),
                          ToggleClipboardsMenuOption(),
                          DisplayClipboardsMenuOption(),
                          SearchForClipboardMenuOption(),   
                          SaveClipboardMenuOption(),
                          LoadClipboardMenuOption(),                       
                          ExitMenuOption()                        
                          ]
                        )
    menu.UtiliseMenu()

