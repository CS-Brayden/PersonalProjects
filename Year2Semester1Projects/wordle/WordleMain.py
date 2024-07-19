#Perform exception handling/validation, documentation, and testing
from wordlePackage.WordleRoundManager import WordleRoundManager
from consolePackage.ConsoleInterface import ConsoleInterface
from wordlePackage.OverallStatisticsManagerDAO import OverallStatisticsManagerDAO

if __name__ == "__main__":
    overllStatistics = OverallStatisticsManagerDAO.SelectStatistics()
    while True:
        print(overllStatistics)
        readInput = ConsoleInterface.ReadRequiredValue("Do you want to start a round (Y/N): ", 
                                                       ['y', 'n'])
        if readInput == "n": 
            print("Quitting!")
            break
        else: print("Starting!")
        setGuesses = ConsoleInterface.ReadInteger("Please enter the number of guesses: ")
        wordleRoundManager = WordleRoundManager(setGuesses)
        wordleRoundManager.StartRound()
        wordleRoundManager.DisplayResults()
        wordleRoundManager.UpdateOverallResults(overllStatistics)
        OverallStatisticsManagerDAO.InsertStatistics(overllStatistics)