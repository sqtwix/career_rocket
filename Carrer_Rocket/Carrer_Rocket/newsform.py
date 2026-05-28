from ast import parse
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
        json.dump(news_list, f, ensure_ascii=False, indent=4)

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

    is_date_valid, date_result = validate_date(date)

    if not title:
        errors.append('Название обязательно')
    if not category:
        errors.append('Категория обязательна')
    if not description:
        errors.append('Описание обязательно')
    if not date:
        errors.append('Дата обязательна')
    if not is_date_valid:
        errors.append(date_result) 
    else:
        date = date_result 

    return errors, title,category, description, date

def validate_date(date_str):
    if not date_str or not date_str.strip():
        return False, "Дата не может быть пустой"
    date_str = date_str.strip()
    if len(date_str) != 10 or date_str[4] != '-' or date_str[7] != '-':
        return False, "Неверный формат даты. Используйте ГГГГ-ММ-ДД"
    try:
        parsed_date = datetime.strptime(date_str, '%Y-%m-%d')

        if parsed_date > datetime.now():
            return False, "Дата не может быть в будущем"

        if parsed_date.year < 2000:
            return False, "Год должен быть не раньше 2000"
        
        if parsed_date.year > 2030:
            return False, "Год должен быть не позже 2030"
        
        return True, date_str
    except ValueError:
        return False, "Несуществующая дата"

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
    title = request.forms.getunicode('title', '')
    category = request.forms.getunicode('category', '')
    description = request.forms.getunicode('description', '')
    date = request.forms.getunicode('date', '')

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