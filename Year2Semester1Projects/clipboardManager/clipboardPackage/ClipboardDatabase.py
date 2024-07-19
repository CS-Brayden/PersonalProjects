from sqlite3 import connect, Error
from .CustomClipboard import CustomClipboard

class ClipboardDatabase:
    @staticmethod
    def _CreateDatabase(databaseFile):
        connection = connect(databaseFile)
        cursor = connection.cursor()
        try:
            cursor.execute("""
                        CREATE TABLE IF NOT EXISTS ClipboardCollection ( 
                                                            CopyShortcut VARCHAR(50) NOT NULL,
                                                            PasteShortcut VARCHAR(50) NOT NULL,
                                                            Active BOOLEAN NOT NULL,
                                                            PRIMARY KEY(CopyShortcut, PasteShortcut));
                        """)
        except Exception: 
            cursor.close()
            connection.close()
            cursor, connection = None, None
        return cursor, connection
    @staticmethod
    def StoreClipboardCollection(clipboards, databaseFile = 'clipboard.db'):
        
        cursor, connection = ClipboardDatabase._CreateDatabase(databaseFile)
        if connection == None: raise Error("Process stopped, cannot connect with database")
        try:
            shortcuts = []
            for clipboard in clipboards:
                cursor.execute("""
                            INSERT OR REPLACE INTO ClipboardCollection (CopyShortcut, PasteShortcut, Active)
                            VALUES (?, ?, ?);
                            """, (clipboard.copyShortcut, clipboard.pasteShortcut, clipboard.active))
                shortcuts += [clipboard.copyShortcut, clipboard.pasteShortcut]
            shortcutPlaceholder = ", ".join(["?"] * len(shortcuts))     
            cursor.execute(f"""
                        DELETE FROM ClipboardCollection
                        WHERE CopyShortcut NOT IN ({shortcutPlaceholder})
                        OR PasteShortcut NOT IN ({shortcutPlaceholder});
                        """, shortcuts * 2)
            connection.commit()
        except: 
            raise Error("Process stopped, cannot connect with database")
        finally:
            cursor.close()
            connection.close()
    @staticmethod
    def LoadClipboardCollection(databaseFile = 'clipboard.db'):
        cursor, connection = ClipboardDatabase._CreateDatabase(databaseFile)
        if connection == None: raise Error("Process stopped, cannot connect with database")
        try:
            rows = cursor.execute("SELECT * FROM ClipboardCollection").fetchall()
            return [CustomClipboard(row[0], row[1], row[2]) for row in rows]
        except: raise Error("Process stopped, cannot connect with database")
        finally:
            cursor.close()
            connection.close()