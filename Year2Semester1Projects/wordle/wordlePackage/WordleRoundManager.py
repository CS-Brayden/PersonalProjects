from consolePackage.ConsoleInterface import ConsoleInterface
from .Wordle import Wordle

class WordleRoundManager:
    def __init__(self, totalGuessNumber = 5):
        self.totalGuessNumber = totalGuessNumber
        self.guesses = []
        self.guessCount = 0
        self.wordleValue = Wordle()
        self.isCorrect = False

    def StartRound(self):
        unrelatedCharacters = set()
        for guessNumber in range(1, self.totalGuessNumber + 1):
            self.guessCount = guessNumber
            if unrelatedCharacters != set(): print(f"Known unreleated character: {unrelatedCharacters}")
            guessValue = ConsoleInterface.ReadWordleValue(f"{guessNumber}) Enter a guess: ", 
                                                          self.wordleValue.GetWordleCollection()
                                                         )
            ConsoleInterface.PrintColouredString(guessValue, self.wordleValue.GetCharacterColourMatches(guessValue))
            self.guesses.append(guessValue)
            if self.wordleValue.IsCorrectGuess(guessValue): 
                self.isCorrect = True
                break
            unrelatedCharacters |= self.wordleValue.GetUnrelatedCharacters(guessValue)

    def DisplayResults(self):
        print("----------------------------------------")
        print(f"Out of {self.totalGuessNumber} {'guesses' if self.totalGuessNumber != 1 else 'guess'}:")
        if self.isCorrect: 
            print(f"Correct, the value is {self.wordleValue.GetSetWord()}")
            print(f"This was guessed in {self.guessCount} {'guesses' if self.guessCount != 1 else 'guess'}")
        else: print(f"Incorrect, the value is {self.wordleValue.GetSetWord()}")
        print("Guesses: ")
        for guessIndex, guess in enumerate(self.guesses):
            print(f"{guessIndex + 1}) ", end = "")
            ConsoleInterface.PrintColouredString(guess, self.wordleValue.GetCharacterColourMatches(guess))
        print("----------------------------------------")

    def UpdateOverallResults(self, givenOverllStatistics):
        givenOverllStatistics.AddRound()
        if self.isCorrect:
            givenOverllStatistics.AddGuessNumber(self.guessCount)
            givenOverllStatistics.AddStreak()
        else: givenOverllStatistics.ResetStreak()