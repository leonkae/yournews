from flask import Config

import os
class Config:
    '''holds base urls'''
    
    NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
    # export NEWS_API_KEY='444f55e941ed44459db54db9932d8905'
    SOURCE_BASE_URL = "https://newsapi.org/v2/top-headlines/sources?apiKey={}"
    NEWS_BASE_URL ='https://newsapi.org/v2/top-headlines?country=us&category={}&apiKey={}'
    
 # https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=444f55e941ed44459db54db9932d8905
class ProdConfig(Config):
    pass

class DevConfig(Config):
    '''holds debugger'''
    DEBUG = True
  
    
    