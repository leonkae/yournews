# from turtle import title
import urllib.request,json
from app import app
from instance.config import NEWS_API_KEY
from app.config import config
from .models.article import Article
from .models.source import Source


api_key = NEWS_API_KEY
base_url = config.NEWS_BASE_URL
source_base_url = config.SOURCE_BASE_URL 

def get_articles(category):
    get_url = base_url.format(category,api_key)
    print (get_url)
    # get_url = 'https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=444f55e941ed44459db54db9932d8905'
    # print ("url hala",get_url)
    with urllib.request.urlopen(get_url) as url:
        get_data = url.read()
        get_article_response = json.loads(get_data)
        
        article_result = None
        
        if get_article_response['articles']:
            article_result_list = get_article_response['articles']
            # print (article_result_list)
            article_result = process_results(article_result_list)
            # print (article_result)
            return article_result    
            
def process_results(article_result_list):
    article_result = []
    for item in article_result_list:
        author = item.get('author')
        title = item.get('title')
        description = item.get('description')
        url = item.get('url')
        urlToImage = item.get('urlToImage')
        content = item.get('content')
        
        # if urlToImage:
        article_object = Article(author,title,description,url,urlToImage,content)
        article_result.append(article_object)
    return article_result


def get_source():
    get_url = source_base_url.format(api_key)
    print (get_url)
    
    with urllib.request.urlopen(get_url) as url:
        get_data = url.read()
        get_sources_response = json.loads(get_data)
        
        source_result = None
        
        if get_sources_response['sources']:
            source_result_list = get_sources_response['sources']
            source_result = process_results(source_result_list)
            return source_result
        
def process_result(source_result_list):
    source_result = []
    for item in source_result_list:
        name = item.get('name')
        url = item.get('url')
        
        source_object = Source(name,url) 
        source_result.append(source_object)
    return source_result            
            
        
        

        
        
        
        # https://newsapi.org/v2/?category=business&apiKey=444f55e941ed44459db54db9932d8905
        
        # https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=444f55e941ed44459db54db9932d8905
        
        
        
    #   self.author = author
    #     self.title = title
    #     self.description = description
    #     self.url = url
    #     self.urlToImage = urlToImage
    #     self.content = content