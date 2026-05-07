"""
Routes and views for the bottle application.
"""

from bottle import route, view, template, static_file, request, redirect, response
import json
import os
from datetime import datetime

# consts
FEEDBACK_FILE = 'data/feedback.json'

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

@route('/analytics')
@view('analytics')
def analytics():

    # Загрузка данных из json
    with open('data/categories.json', 'r', encoding='cp1251') as f:
        categories_data = json.load(f)

    with open('data/salaries.json', 'r', encoding='cp1251') as f:
        salaries_data = json.load(f)

    return dict(
        title = 'Analytic',
        message='Аналитка рынка.',
        categories=json.dumps(categories_data, ensure_ascii=False),
        salaries=json.dumps(salaries_data, ensure_ascii=False),
        year=datetime.now().year
        )

@route('/offer_store')
@view('offer_store')
def offer_store():
    hh_link = "https://hh.ru/search/vacancy?area=113&professional_role=96&professional_role=104&professional_role=124&professional_role=125&professional_role=126&text=IT"
    
    return dict(
        title='Offer_store',
        message='Магазин предложений',
        year=datetime.now().year,
        hh_link=hh_link
    )

@route('/static/<filepath:path>')
def serve_static(filepath):
    return static_file(filepath, root='./static')

@route('/data/<filename>')
def serve_data(filename):
    return static_file(filename, root='./data')


# Доп функции для страницы отзывов
def load_feedback():
    """Загружает отзывы из JSON-файла"""
    if os.path.exists(FEEDBACK_FILE):
        with open(FEEDBACK_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def save_feedback(data):
    """Сохраняет отзывы в JSON-файл"""
    with open(FEEDBACK_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

@route('/feedback', method='GET')
@view('feedback')
def feedback_get():
    """Показывает страницу отзывов"""
    response.content_type = 'text/html; charset=utf-8'
    reviews = load_feedback()

    # Сортировка: сначала новые (по дате убывания)
    reviews.sort(key=lambda x: x['date'], reverse=True)
    return {
        'reviews': reviews,
        'author': '',
        'text': '',
        'error': None,
        'year': datetime.now().year
    }

@route('/feedback', method='POST')
def feedback_post():
    author = request.forms.getunicode('author', '').strip()
    text = request.forms.getunicode('text', '').strip()
    
    errors = []
    if not author or len(author) < 2:
        errors.append('Имя автора должно содержать не менее 2 символов')
    if not text or len(text) < 5:
        errors.append('Текст отзыва должен содержать не менее 5 символов')
    
    if errors:
        reviews = load_feedback()
        reviews.sort(key=lambda x: x['date'], reverse=True)
        # Рендерим шаблон явно, а не возвращаем словарь
        return template('feedback', 
                        reviews=reviews,
                        author=author,
                        text=text,
                        error='; '.join(errors),
                        year=datetime.now().year)
    
    # Всё валидно – сохраняем
    new_review = {
        'author': author,
        'text': text,
        'date': datetime.now().isoformat()
    }
    reviews = load_feedback()
    reviews.append(new_review)
    save_feedback(reviews)
    
    # Редирект для очистки формы
    return redirect('/feedback')