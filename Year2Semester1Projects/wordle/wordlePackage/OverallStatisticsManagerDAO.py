from sqlite3 import connect, Error
from .OverallStatisticsManager import OverallStatisticsManager

CONSTANT_DATABASE_FILE = 'WordleStatistics.db'

class OverallStatisticsManagerDAO:
    @staticmethod
    def _Connect(databaseFile):
        connection = connect(databaseFile)
        cursor = connection.cursor()
        try:
            cursor.execute("""
                        CREATE TABLE IF NOT EXISTS OverallStatistics ( 
                                                            ID INTEGER NOT NULL,
                                                            TotalRounds INTEGER NOT NULL,
                                                            CurrentStreak INTEGER NOT NULL,
                                                            MaxStreak INTEGER NOT NULL,
                                                            GuessCountID INTEGER NOT NULL,
                                                            PRIMARY KEY(ID));
                        """)
            cursor.execute("""
                        CREATE TABLE IF NOT EXISTS GuessesCounts ( 
                                                            GuessCountID INTEGER NOT NULL,
                                                            GuessValue INTEGER NOT NULL,
                                                            CountValue INTEGER NOT NULL,
                                                            PRIMARY KEY(GuessCountID, GuessValue),
                                                            FOREIGN KEY (GuessCountID) 
                                                            REFERENCES OverallStatistics(GuessCountID));
                        """)
        except Exception: 
            cursor.close()
            connection.close()
            cursor, connection = None, None
        return cursor, connection
    
    @staticmethod
    def SelectStatistics(databaseFile = CONSTANT_DATABASE_FILE):
        cursor, connection = OverallStatisticsManagerDAO._Connect(databaseFile)
        if connection == None: raise Error("Process stopped, cannot connect with database")
        try:    
            statisticsRows = cursor.execute(f"""SELECT TotalRounds, CurrentStreak, MaxStreak, GuessCountID
                                            FROM OverallStatistics;""").fetchone()
            if statisticsRows == None: return OverallStatisticsManager()
            countId = statisticsRows[3]
            countRows = cursor.execute(f"""SELECT GuessValue, CountValue
                                       FROM GuessesCounts
                                       WHERE GuessCountId == ?;""", (countId,)).fetchall()
            guessesCount = {guess : count for (guess, count) in countRows}
            totalRounds, currentStreak, maxStreak = statisticsRows[:3]
            return OverallStatisticsManager(totalRounds, guessesCount, currentStreak, maxStreak)
        except Exception as e:
            raise Error("Process stopped, cannot connect with database")
        finally:
            cursor.close()
            connection.close()
    
    def InsertStatistics(overallStatistics, databaseFile = CONSTANT_DATABASE_FILE):
        cursor, connection = OverallStatisticsManagerDAO._Connect(databaseFile)
        if connection == None: raise Error("Process stopped, cannot connect with database")
        try:       
            cursor.execute("""
                            INSERT OR REPLACE INTO OverallStatistics (ID, TotalRounds, CurrentStreak, MaxStreak, GuessCountID)
                            VALUES (1, ?, ?, ?, 1);
                            """, (overallStatistics.GetRounds(), overallStatistics.GetStreak(), overallStatistics.GetMaxStreak()))
            for guess, count in overallStatistics.GetGuessesCount().items():
                cursor.execute("""
                                INSERT OR REPLACE INTO GuessesCounts (GuessCountID, GuessValue, CountValue)
                                VALUES (1, ?, ?);
                                """, (guess, count))
            connection.commit()
        except: 
            raise Error("Process stopped, cannot connect with database")
        finally:
            cursor.close()
            connection.close()