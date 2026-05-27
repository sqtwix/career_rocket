from bottle import route, static_file  
import json
from datetime import datetime
import controllers.articles_controller


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


@route('/offer_store')
def offer_store():
    from bottle import template
    hh_link = "https://hh.ru/search/vacancy?area=113&professional_role=96&professional_role=104&professional_role=125&professional_role=126&text=IT"
    return template('offer_store', title='Offer_store', message='Магазин предложений', year=datetime.now().year, hh_link=hh_link)


@route('/static/<filepath:path>')
def serve_static(filepath):
    return static_file(filepath, root='./static')


@route('/data/<filename>')
def serve_data(filename):
    return static_file(filename, root='./data')