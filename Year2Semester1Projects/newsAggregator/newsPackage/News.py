from abc import ABC, abstractmethod
import requests
from bs4 import BeautifulSoup

class AbstractNews(ABC):
    def __init__(self, newsURL):
        self.newsURL = newsURL
        self.headlineURLs = []

    def _GetNewsPage(self):
        response = requests.get(self.newsURL)
        return BeautifulSoup(response.content, "html.parser")

    @abstractmethod
    def _GetNewsHeadlines(self, headlinePage): pass

    def GetNews(self):
        headlinePage = self._GetNewsPage()
        self.headlineURLs = self._GetNewsHeadlines(headlinePage)

class GuardianNews(AbstractNews):
    def __init__(self):
        super().__init__("https://www.theguardian.com/au")

    def _GetNewsHeadlines(self, headlinePage):
        #10 headlines available - theGuardian
        foundHeadlines = headlinePage.find(id = "container-headlines")
        newsTags = foundHeadlines.find_all("a", class_ = "dcr-lv2v9o")
        test = [tag.get('href') for tag in newsTags]
        print("should be 10:", len(test))
        return test
    
class BBCNews(AbstractNews):
    def __init__(self):
        super().__init__("https://www.bbc.com/news")

    def _GetNewsHeadlines(self, headlinePage):
        #8 headlines available - BBC
        foundHeadlines = headlinePage.find("div", {"data-testid" : "undefined-grid-8"})
        newsTags = foundHeadlines.find_all("a", {"data-testid" : "internal-link"})
        test = [tag.get('href') for tag in set(newsTags)]
        print("should be 8:", len(test))
        return test
    
class SevenNews(AbstractNews):
    def __init__(self):
        super().__init__("https://7news.com.au/")

    def _GetNewsHeadlines(self, headlinePage):
        #5 headlines available - 7News
        classAttribute = "css-1ja5ba7-StyledHeroCollectionWrapper e1yd20ns2"
        foundHeadlines = headlinePage.find("div", class_ = classAttribute)
        newsTags = foundHeadlines.find_all("a", {"itemtype" : None})
        test = list({tag.get('href') for tag in newsTags})
        print("should be 5:", len(test))
        return test