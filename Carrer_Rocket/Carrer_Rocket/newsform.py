import json
import os
from datetime import datetime
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

def get_sorted_news():
    """Возвращает отсортированный список новинок (новые сверху)."""
    news_list = load_news()
    news_list.sort(key=lambda x: x.get('date', ''), reverse=True)
    return news_list

def validate_news_data(title,category, description, date):
    """Проверяет корректность данных новинки."""
    errors = []

    title = title.strip() if title else ''
    category = category.strip() if category else ''
    description = description.strip() if description else ''
    date = date.strip() if date else ''

    if not title:
        errors.append('Название обязательно')
    if not category:
        errors.append('Категория обязательна')
    if not description:
        errors.append('Описание обязательно')
    if not date:
        errors.append('Дата обязательна')

    return errors, title,category, description, date

def add_news_item(title, category, description, date):
    """Добавляет новую новинку в файл."""
    try:
        news_list = load_news()

        new_item = {
            'title': title,
            'category': category,
            'description': description,
            'date': date
        }
        news_list.append(new_item)
        news_list.sort(key=lambda x: x.get('date', ''), reverse=True)
        save_news(news_list)
        return news_list
    except Exception as e:
        print(f"Ошибка при сохранении: {e}")
        return None

def get_page_data():
    """Возвращает данные для отображения страницы (список, ошибка, form_data)."""
    return {
        'news_list': get_sorted_news(),
        'error': '',
        'form_data': {}
    }

def process_news_form(request, current_year):
    title = request.forms.get('title', '')
    category = request.forms.get('category', '')
    description = request.forms.get('description', '')
    date = request.forms.get('date', '')

    errors, title,category, description, date = validate_news_data(title, category, description, date)

    if errors:
        return ('news', {
            'title': 'Актуальные новинки',
            'year': current_year,
            'news_list': get_sorted_news(),
            'error': '<br>'.join(errors),
            'form_data': {
                'title': title,
                'category': category,
                'description': description,
                'date': date
            }
        })
    
    result = add_news_item(title, category, description, date)
    
    # Если сохранение не удалось (вернуло None) — показываем ошибку
    if result is None:
        return ('news', {
            'title': 'Актуальные новинки',
            'year': current_year,
            'news_list': get_sorted_news(),
            'error': 'Ошибка при сохранении данных. Проверьте файл news.json',
            'form_data': {
                'title': title,
                'category': category,
                'description': description,
                'date': date
            }
        })
    
    return None 