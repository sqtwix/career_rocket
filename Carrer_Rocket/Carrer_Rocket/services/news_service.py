import json

from datetime import date
from models.news_model import NewsModel

class NewsService():
    @staticmethod
    def get_all_news() -> list[NewsModel]:
        news_models = []
        with open("data/news.json", 'r', encoding='utf-8') as f:
            content = f.read()
            loaded_context = json.loads(content)
            for news in loaded_context['news']:
                news_models.append(
                    NewsModel(
                        news['header'],
                        news['description'],
                        news['author'],
                        news['postDate'],
                        news['text']
                    )
                )
        return news_models
    
    @staticmethod
    def get_all_news_by_date(postDate : date) -> list[NewsModel]:
        news_models = []
        with open("data/news.json", 'r', encoding='utf-8') as f:
            loaded_context = json.loads(f.read())
            for news in loaded_context['news']:
                if news['postDate'] == postDate:
                    news_models.append(
                    NewsModel(
                        news['header'],
                        news['description'],
                        news['author'],
                        news['postDate'],
                        news['text']
                    )
                )
        return news_models
    
    @staticmethod
    def get_all_news_by_interval(startDate : date, endDate : date) -> list[NewsModel]:
        news_models = []
        with open("data/news.json", 'r', encoding='utf-8') as f:
            loaded_context = json.loads(f.read())
            for news in loaded_context['news']:
                if news['postDate'] >= startDate and news['postDate'] <= endDate:
                    news_models.append(
                    NewsModel(
                        news['header'],
                        news['description'],
                        news['author'],
                        news['postDate'],
                        news['text']
                    )
                )
        return news_models