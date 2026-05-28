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
@view('index')
def home():
    """Renders the home page."""
    return dict(
        year=datetime.now().year
    )

@route('/contact')
@view('contact')
def contact():
    """Renders the contact page."""
    return dict(
        title='Contact',
        message='Your contact page.',
        year=datetime.now().year
    )

@route('/about')
@view('about')
def about():
    """Renders the about page."""
    return dict(
        title='About',
        message='Your application description page.',
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