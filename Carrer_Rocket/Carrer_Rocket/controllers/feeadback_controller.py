import json
import os
import re
from datetime import datetime
from bottle import route, view, template, request, redirect, response

FEEDBACK_FILE = 'data/feedback.json'

def load_feedback():
    """Загружает данные из JSON-файла"""
    if not os.path.exists(FEEDBACK_FILE):
        return {}
    with open(FEEDBACK_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_feedback(data):
    """Сохраняет данные в JSON."""
    with open(FEEDBACK_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

#  Валидация
def is_valid_by_regular(email):
    email_pattern = r'^[a-zA-Z0-9][a-zA-Z0-9._%+-]{0,62}@[a-zA-Z0-9][a-zA-Z0-9-]{1,62}\.[a-zA-Z]{2,}$'
    return bool(re.match(email_pattern, email))

def is_valid_domain(email):
    domain_zone = email.split('.')[-1].lower()
    allowed_domains = ['ru', 'com', 'net', 'org', 'edu', 'gov', 'mil', 'info',
                       'biz', 'site', 'tech', 'io', 'uk', 'de', 'fr', 'jp', 'cn']
    return domain_zone in allowed_domains

def getErrorList(author, title, text, email):
    errors = []
    if not author or len(author) < 2:
        errors.append('Имя автора должно содержать не менее 2 символов')
    if not title or len(title) < 3:
        errors.append('Заголовок отзыва должен содержать не менее 3 символов')
    elif len(title) > 100:
        errors.append('Заголовок не должен превышать 100 символов')
    if not text or len(text) < 5:
        errors.append('Текст отзыва должен содержать не менее 5 символов')
    if text.replace(' ', '').isdigit():
        errors.append("Текст не может состоять только из цифр.")
    if not is_valid_by_regular(email):
        errors.append("Почта не соответствует паттерну! (Пример: bob123@mail.com).")
    elif not is_valid_domain(email):
        errors.append("Невалидный домен. Он должен быть из списка: ru, com, net, org, edu, gov, mil, info, biz, site, tech, io, uk, de, fr, jp, cn")
    return errors

#  Основные операции с отзывами
def get_all_reviews_sorted():
    """Возвращает плоский список всех отзывов, сортированный по дате (новые сверху)."""
    data = load_feedback()
    all_reviews = []
    for email, reviews in data.items():
        for rev in reviews:
            rev_copy = rev.copy()
            rev_copy['email'] = email      
            all_reviews.append(rev_copy)
    all_reviews.sort(key=lambda x: x['date'], reverse=True)
    return all_reviews

def add_review(email, author, title, text):
    """Добавляет отзыв для указанного email (сохраняя имя в отзыве)."""
    data = load_feedback()
    if email not in data:
        data[email] = []
    new_review = {
        'author': author,
        'title': title,
        'text': text,
        'date': datetime.now().isoformat()
    }
    data[email].append(new_review)
    save_feedback(data)

#  Маршруты 
@route('/feedback', method='GET')
@view('feedback')
def feedback_get():
    response.content_type = 'text/html; charset=utf-8'
    reviews = get_all_reviews_sorted()
    return {
        'reviews': reviews,
        'author': '',
        'title': '',
        'text': '',
        'email': '',
        'errors': [],
        'year': datetime.now().year
    }

@route('/feedback', method='POST')
def feedback_post():
    author = request.forms.getunicode('author', '').strip()
    title = request.forms.getunicode('title', '').strip()
    text = request.forms.getunicode('text', '').strip()
    email = request.forms.getunicode('email', '').strip()

    errors = getErrorList(author, title, text, email)
    if errors:
        reviews = get_all_reviews_sorted()
        return template('feedback',
                        reviews=reviews,
                        author=author,
                        title=title,
                        text=text,
                        email=email,
                        errors=errors,
                        year=datetime.now().year)

    add_review(email, author, title, text)
    return redirect('/feedback')