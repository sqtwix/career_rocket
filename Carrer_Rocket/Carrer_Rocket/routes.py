"""
Routes and views for the bottle application.
"""

from bottle import route, view, template, request, redirect
from datetime import datetime
import json
import os

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

def load_news():
    """Загружает список новинок из JSON файла."""
    if not os.path.exists(NEWS_FILE):
        return []
    with open(NEWS_FILE, 'r', encoding='utf-8') as f:
        try:
            return json.load(f)
        except:
            return []

def save_news(news_list):
    """Сохраняет список новинок в JSON файл."""
    with open(NEWS_FILE, 'w', encoding='utf-8') as f:
        json.dump(news_list, f, ensure_ascii=False, indent=2)

@route('/news')
def show_news():
    """Отображает страницу со всеми новинками и формой добавления."""
    news_list = load_news()

    news_list.sort(key=lambda x: x.get('date', ''), reverse=True)
    return template('news', 
        year=datetime.now().year,
        news_list=news_list
    )

@route('/news', method='POST')
def add_news():
    """Обрабатывает добавление новой новинки из формы."""
    title = request.forms.get('title', '').strip()
    category = request.forms.get('category', '').strip()
    date = request.forms.get('date', '').strip()
    description = request.forms.get('description', '').strip()

    if not title or not category or not date or not description:
        return redirect('/news')

    news_list = load_news()
    new_item = {
        'title': title,
        'category': category,
        'date': date,
        'description': description,
    }
    news_list.append(new_item)
    save_news(news_list)
    return redirect('/news')