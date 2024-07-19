import copy
class ClipboardCollectionSession:
    _collectionInstance = []

    @classmethod
    def StoreClipboard(cls, givenClipboard):
        cls._collectionInstance.append(givenClipboard) 

    @classmethod
    def GetClipboards(cls):
        return copy.deepcopy(cls._collectionInstance)
        return list.copy(cls._collectionInstance)
    
    @classmethod
    def GetClipboard(cls, hotkey):
        for clipboard in cls._collectionInstance:
            if hotkey in (clipboard.copyShortcut, clipboard.pasteShortcut): 
                return clipboard
        raise ValueError("No clipboards were found with the given hotkey")

    @classmethod
    def RemoveClipboard(cls, givenClipboard):
        if givenClipboard not in cls._collectionInstance:
            raise ValueError("The given clipboard is not stored")
        givenClipboard.Deactivate()
        cls._collectionInstance.remove(givenClipboard)

    @classmethod
    def RemoveAllClipboards(cls):
        for clipboard in cls._collectionInstance:
            cls.RemoveClipboard(clipboard)

    @classmethod
    def GetShortcuts(cls):
        allShortcuts = []
        for clipboard in cls._collectionInstance:
            allShortcuts += [clipboard.copyShortcut, clipboard.pasteShortcut]
        return allShortcuts

    @classmethod
    def IsEmpty(cls):
        return cls._collectionInstance == []

    @classmethod
    def ActivateAllClipboards(cls):
        for clipboard in cls._collectionInstance:
            clipboard.Activate()

    @classmethod
    def DeactivateAllClipboards(cls):
        for clipboard in cls._collectionInstance:
            clipboard.Deactivate()

    @classmethod
    def SetClipboardCollection(cls, givenCollection):
        cls._collectionInstance = givenCollection