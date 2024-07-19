from menuPackage.MenuInterface import MenuInterface
from menuPackage.MenuOption import TestMenuOption, ExitMenuOption

if __name__ == "__main__":
    
    menu = MenuInterface("Clipboard Manager", 
                         "Select an option: ",
                         [TestMenuOption(),
                          ExitMenuOption()]
                        )
    menu.UtiliseMenu()