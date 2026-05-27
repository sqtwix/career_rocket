# services/news_service.py
import json
import os
from datetime import datetime
from models.news_model import NewsModel
from services.validation_service import ValidationService, ValidationError


class NewsService:
    
    DATA_FILE = "data/news.json"
    
    @staticmethod
    def get_all_news() -> list[NewsModel]:
        news_models = []
        if not os.path.exists(NewsService.DATA_FILE):
            return news_models
        
        with open(NewsService.DATA_FILE, 'r', encoding='utf-8') as f:
            content = f.read()
            if not content:
                return news_models
            loaded_context = json.loads(content)
            for news in loaded_context.get('news', []):
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
    def get_all_news_by_date(postDate: str) -> list[NewsModel]:
        news_models = []
        with open(NewsService.DATA_FILE, 'r', encoding='utf-8') as f:
            loaded_context = json.loads(f.read())
            for news in loaded_context.get('news', []):
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
    def get_all_news_by_interval(startDate: str, endDate: str) -> list[NewsModel]:
        news_models = []
        start = datetime.strptime(startDate, '%Y-%m-%d').date()
        end = datetime.strptime(endDate, '%Y-%m-%d').date()
        
        with open(NewsService.DATA_FILE, 'r', encoding='utf-8') as f:
            loaded_context = json.loads(f.read())
            for news in loaded_context.get('news', []):
                news_date = datetime.strptime(news['postDate'], '%Y-%m-%d').date()
                if start <= news_date <= end:
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
    def add_new_news(form_data: dict):
        errors = ValidationService.validate_news_form(form_data)
        
        if errors:
            raise ValidationError(errors)
        
        existing_news = []
        if os.path.exists(NewsService.DATA_FILE):
            with open(NewsService.DATA_FILE, 'r', encoding='utf-8') as f:
                content = f.read()
                if content:
                    loaded = json.loads(content)
                    existing_news = loaded.get('news', [])
        
        new_news = {
            'header': form_data['header'],
            'description': form_data['description'],
            'author': form_data['author'],
            'postDate': form_data['postDate'],
            'text': form_data['text']
        }
        
        existing_news.append(new_news)
        
        with open(NewsService.DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump({"news": existing_news}, f, ensure_ascii=False, indent=4)