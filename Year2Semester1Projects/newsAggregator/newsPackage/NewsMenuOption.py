from menuPackage.MenuOption import AbstractMenuOption
from .NewsCollectionSession import NewsCollectionSession
from .News import GuardianNews, BBCNews, SevenNews

class GetNewsMenuOption(AbstractMenuOption):
    def __init__(self):
        super().__init__("1", "Get current news", False)
    def UtiliseOption(self):
        NewsCollectionSession.RemoveAllNews()
        NewsCollectionSession.StoreNews(GuardianNews())
        NewsCollectionSession.StoreNews(BBCNews())
        NewsCollectionSession.StoreNews(SevenNews())
        NewsCollectionSession.UpdateAllNews()
        print("The new has been retrieved!")
        input("To test:")
        for news in NewsCollectionSession.GetNews():
            print(news.newsURL)
            print(news.headlineURLs)
            print("--------------------------------")
