from copy import copy

class OverallStatisticsManager:
    def __init__(self, totalRounds = 0, 
                 guessesCount = {1 : 0, 2 : 0, 3 : 0, 4 : 0, 5 : 0}, 
                 currentStreak = 0, 
                 maxStreak = 0):
        self._totalRounds = totalRounds
        self._guessesCount = guessesCount
        self._currentStreak = currentStreak
        self._maxStreak = maxStreak

    def AddRound(self): self._totalRounds += 1
    def AddGuessNumber(self, guessCount): 
        if guessCount in self._guessesCount: self._guessesCount[guessCount] += 1
        else: self._guessesCount.update({guessCount : 1})

    def AddStreak(self): 
        self._currentStreak += 1
        if self._currentStreak > self._maxStreak: self._maxStreak = self._currentStreak
    def ResetStreak(self): self._currentStreak = 0
    def GetRounds(self): return self._totalRounds
    def GetGuessesCount(self): return copy(self._guessesCount) 
    def GetStreak(self): return self._currentStreak
    def GetMaxStreak(self): return self._maxStreak

    def __str__(self):
        wins = sum(self._guessesCount.values())
        winPercentage = None if self._totalRounds == 0 else round(100 * (wins / self._totalRounds))
        displayString = f"""----------------------------------------
Wordle Statistics
Played: {self._totalRounds}
Wins: {wins}
Losses: {self._totalRounds - wins}
Win Percentage: {winPercentage}
Current Streak: {self._currentStreak}
Max Streak: {self._maxStreak}
"""
        for guessCountMatch in self._guessesCount.items():
            displayString += f"{guessCountMatch[0]} : {guessCountMatch[1]}\n"
        displayString += "----------------------------------------"
        return displayString