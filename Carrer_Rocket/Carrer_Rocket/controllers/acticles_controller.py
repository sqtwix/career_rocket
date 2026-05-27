from bottle import request, template, redirect
from services.article_service import ArticleService
from services.validation_service import ValidationError

class ArticlesController:
    
    @staticmethod
    def index():
        start_date = request.query.get('start_date', '')
        end_date = request.query.get('end_date', '')
        
        try:
            if start_date and end_date:
                articles = ArticleService.get_all_articles_by_interval(start_date, end_date)
            else:
                articles = ArticleService.get_all_articles()
        except ValueError:
            articles = ArticleService.get_all_articles()
        
        articles.sort(key=lambda x: x.postDate, reverse=True)
        
        return template(
            'articles',
            articles=articles,
            errors={},
            form_data={},
            start_date=start_date,
            end_date=end_date
        )
    
    @staticmethod
    def add():
        form_data = {
            'header': request.forms.get('header', '').strip(),
            'description': request.forms.get('description', '').strip(),
            'author': request.forms.get('author', '').strip(),
            'postDate': request.forms.get('postDate', '').strip(),
            'text': request.forms.get('text', '').strip()
        }
        
        try:
            ArticleService.add_new_article(form_data)
            redirect('/articles')
        except ValidationError as e:
            articles = ArticleService.get_all_articles()
            articles.sort(key=lambda x: x.postDate, reverse=True)
            return template(
                'articles',
                articles=articles,
                errors=e.errors,
                form_data=form_data,
                start_date='',
                end_date=''
            )
    
    @staticmethod
    def filter_by_date():
        start_date = request.forms.get('start_date', '').strip()
        end_date = request.forms.get('end_date', '').strip()
        redirect(f'/articles?start_date={start_date}&end_date={end_date}')