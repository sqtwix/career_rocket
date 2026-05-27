# controllers/news_controller.py
from bottle import request, template, redirect
from services.news_service import NewsService
from services.validation_service import ValidationError


class NewsController:
    
    @staticmethod
    def index():
        start_date = request.query.get('start_date', '')
        end_date = request.query.get('end_date', '')
        
        try:
            if start_date and end_date:
                news_list = NewsService.get_all_news_by_interval(start_date, end_date)
            else:
                news_list = NewsService.get_all_news()
        except ValueError as e:
            news_list = NewsService.get_all_news()
        
        news_list.sort(key=lambda x: x.postDate, reverse=True)
        
        return template(
            'news_template',
            news_list=news_list,
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
            NewsService.add_new_news(form_data)
            redirect('/news')
        except ValidationError as e:
            news_list = NewsService.get_all_news()
            news_list.sort(key=lambda x: x.postDate, reverse=True)
            return template(
                'news_template',
                news_list=news_list,
                errors=e.errors,
                form_data=form_data,
                start_date='',
                end_date=''
            )
    
    @staticmethod
    def filter_by_date():
        start_date = request.forms.get('start_date', '').strip()
        end_date = request.forms.get('end_date', '').strip()
        redirect(f'/news?start_date={start_date}&end_date={end_date}')