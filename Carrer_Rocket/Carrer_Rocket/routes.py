"""
Routes and views for the bottle application.
"""

from bottle import route, view, template, static_file  
import json
from datetime import datetime

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
        year=2026
        )

@route('/offer_store')
@view('offer_store')
def offer_store():
    return dict(
            title='Offer_store',
            message='Магазин предложений',
            year = datetime.now().year
            )

# Маршрут для статических файлов (CSS, JS)
@route('/static/<filepath:path>')
def serve_static(filepath):
    return static_file(filepath, root='./static')

# Маршрут для данных (JSON)
@route('/data/<filename>')
def serve_data(filename):
    return static_file(filename, root='./data')
