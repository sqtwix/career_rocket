import json
import os
from datetime import datetime
from models.article_model import ArticleModel
from services.validation_service import ValidationError, ValidationService

class ArticleService:
    
    DATA_FILE = "data/articles.json"
    
    @staticmethod
    def get_all_articles() -> list[ArticleModel]:
        articles = []
        if not os.path.exists(ArticleService.DATA_FILE):
            return articles
        
        with open(ArticleService.DATA_FILE, 'r', encoding='utf-8') as f:
            content = f.read()
            if not content:
                return articles
            loaded = json.loads(content)
            for article in loaded.get('articles', []):
                articles.append(
                    ArticleModel(
                        article['header'],
                        article['description'],
                        article['author'],
                        article['postDate'],
                        article['text']
                    )
                )
        return articles
    
    @staticmethod
    def get_all_articles_by_date(postDate: str) -> list[ArticleModel]:
        articles = []
        try:
            datetime.strptime(postDate, '%Y-%m-%d')
        except ValueError:
            raise ValueError(f"Неверный формат даты: {postDate}")
        
        with open(ArticleService.DATA_FILE, 'r', encoding='utf-8') as f:
            loaded = json.loads(f.read())
            for article in loaded.get('articles', []):
                if article['postDate'] == postDate:
                    articles.append(
                        ArticleModel(
                            article['header'],
                            article['description'],
                            article['author'],
                            article['postDate'],
                            article['text']
                        )
                    )
        return articles
    
    @staticmethod
    def get_all_articles_by_interval(startDate: str, endDate: str) -> list[ArticleModel]:
        articles = []
        try:
            start = datetime.strptime(startDate, '%Y-%m-%d').date()
            end = datetime.strptime(endDate, '%Y-%m-%d').date()
        except ValueError as e:
            raise ValueError(f"Неверный формат даты: {e}")
        
        with open(ArticleService.DATA_FILE, 'r', encoding='utf-8') as f:
            loaded = json.loads(f.read())
            for article in loaded.get('articles', []):
                article_date = datetime.strptime(article['postDate'], '%Y-%m-%d').date()
                if start <= article_date <= end:
                    articles.append(
                        ArticleModel(
                            article['header'],
                            article['description'],
                            article['author'],
                            article['postDate'],
                            article['text']
                        )
                    )
        return articles
    
    @staticmethod
    def add_new_article(form_data: dict):
        errors = ValidationService.validate_article_form(form_data)
        
        if errors:
            raise ValidationError(errors)
        
        existing = []
        if os.path.exists(ArticleService.DATA_FILE):
            with open(ArticleService.DATA_FILE, 'r', encoding='utf-8') as f:
                content = f.read()
                if content:
                    loaded = json.loads(content)
                    existing = loaded.get('articles', [])
                    for article in existing:
                        if article['header'] == form_data['header']:
                            raise Exception
        
        new_article = {
            'header': form_data['header'],
            'description': form_data['description'],
            'author': form_data['author'],
            'postDate': form_data['postDate'],
            'text': form_data['text']
        }
        
        existing.append(new_article)
        
        with open(ArticleService.DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump({"articles": existing}, f, ensure_ascii=False, indent=4)
        
        return new_article