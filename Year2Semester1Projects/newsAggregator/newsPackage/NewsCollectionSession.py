from copy import deepcopy
class NewsCollectionSession:
    _newsSession = []

    @classmethod
    def StoreNews(cls, givenNews):
        cls._newsSession.append(givenNews)
    
    @classmethod
    def GetNews(cls):
        return deepcopy(cls._newsSession)

    @classmethod
    def RemoveAllNews(cls):
        cls._newsSession = []

    @classmethod
    def UpdateAllNews(cls):
        for news in cls._newsSession:
            news.GetNews()