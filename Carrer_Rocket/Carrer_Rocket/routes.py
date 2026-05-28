"""
Routes and views for the bottle application.
"""

from bottle import route, view, template, request, redirect
from datetime import datetime
import json
import os
import newsform

@route('/')
@route('/home')
def home():
    from bottle import template
    return template('index', year=datetime.now().year)


@route('/contact')
def contact():
    from bottle import template
    return template('contact', title='Contact', message='Your contact page.', year=datetime.now().year)


@route('/about')
def about():
    from bottle import template
    return template('about', title='About', message='Your application description page.', year=datetime.now().year)


@route('/analytics')
def analytics():
    from bottle import template
    with open('data/categories.json', 'r', encoding='cp1251') as f:
        categories_data = json.load(f)
    with open('data/salaries.json', 'r', encoding='cp1251') as f:
        salaries_data = json.load(f)
    return template('analytics', title='Analytic', message='Аналитка рынка.', categories=json.dumps(categories_data, ensure_ascii=False), salaries=json.dumps(salaries_data, ensure_ascii=False), year=2026)

    return dict(
        title = 'Analytic',
        message='Аналитка рынка.',
        categories=json.dumps(categories_data, ensure_ascii=False),
        salaries=json.dumps(salaries_data, ensure_ascii=False),
        year=datetime.now().year
    )

NEWS_FILE = 'news.json'

@route('/news')
def show_news():
    """Отображает страницу со всеми новинками и формой."""
    return template('news',
        title='Актуальные новинки',
        year=datetime.now().year,
        news_list=newsform.get_sorted_news(),
        error='',
        form_data={}
    )

@route('/news', method='POST')
def add_news():
    """Обрабатывает добавление новой новинки."""
    try:
        result = newsform.process_news_form(request, datetime.now().year)
    
        # Если есть ошибки – показываем страницу с ними
        if result is not None and result[0] == 'news':
            return template(result[0], **result[1])
    
        # Если ошибок нет – редиректим
        return redirect('/news')
    except Exception as e:
        print(f"Ошибка в add_news: {e}")
        return template('news',
            title='Актуальные новинки',
            year=datetime.now().year,
            news_list=newsform.get_sorted_news(),
            error='',
            form_data={}
        )
