from requests import get
from random import choice
from copy import copy
from colorama import Back

#Reference: https://gist.github.com/scholtes/94f3c0303ba6a7768b47583aff36654d/
CONSTANT_COLLECTION_URL = "https://gist.githubusercontent.com/scholtes/94f3c0303ba6a7768b47583aff36654d/raw/d9cddf5e16140df9e14f19c2de76a0ef36fd2748/wordle-La.txt"
       
class Wordle: 
    def __init__(self):
        self._GeneratePossibleValues()
        self.setWord = choice(self.wordleCollection)
        
    def _GeneratePossibleValues(self):
        collectionUrl = CONSTANT_COLLECTION_URL
        self.wordleCollection = get(collectionUrl).text.splitlines()

    def GetWordleCollection(self): return copy(self.wordleCollection)

    def GetSetWord(self): return self.setWord.upper()

    def IsCorrectGuess(self, givenGuess): return givenGuess.lower() == self.setWord

    def GetCharacterColourMatches(self, givenGuess):
        characterColourMatches = []
        for guessCharacter, character in zip(givenGuess.lower(), self.setWord):
            if guessCharacter == character: characterColourMatches.append(Back.GREEN)
            elif guessCharacter in self.setWord: characterColourMatches.append(Back.YELLOW)
            else: characterColourMatches.append(Back.LIGHTBLACK_EX)
        return characterColourMatches 
    
    def GetUnrelatedCharacters(self, givenGuess): 
        return {character for character in givenGuess.lower() if character not in self.setWord}