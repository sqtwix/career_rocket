import re
from datetime import datetime

class ValidationError(Exception):
    def __init__(self, errors: dict):
        self.errors = errors
        super().__init__(str(errors))

class ValidationService:
    @staticmethod
    def check_mail(mail : str) -> bool:
        allowed_combinations = {
            'yandex': ['ru'],
            'gmail': ['com'],
            'mail': ['ru', 'com'],
            'yahoo' : ['com']
        }

        mail_pattern = r'^[a-zA-Z0-9x]{2,34}@[a-zA.-]+\.[a-zA-Z]{2,}$'

        if not re.match(mail_pattern, mail): return False

        local_part, domain_full = mail.split('@')
        domain_parts = domain_full.split('.')

        if domain_parts[0] not in allowed_combinations: return False
        if domain_parts[1] not in allowed_combinations[domain_parts[0]]: return False
        return True

    @staticmethod
    def validate_article_form(form_data: dict) -> dict:
        errors = {}
        
        header = form_data.get('header', '')
        if not header:
            errors['header'] = 'Заголовок обязателен для заполнения'
        elif len(header) < 3:
            errors['header'] = 'Заголовок должен содержать не менее 3 символов'
        elif len(header) > 200:
            errors['header'] = 'Заголовок не должен превышать 200 символов'
        
        description = form_data.get('description', '')
        if not description:
            errors['description'] = 'Описание обязательно для заполнения'
        elif len(description) < 10:
            errors['description'] = 'Описание должно содержать не менее 10 символов'
        elif len(description) > 500:
            errors['description'] = 'Описание не должно превышать 500 символов'
        
        author = form_data.get('author', '')
        if not author:
            errors['author'] = 'Автор обязателен для заполнения'
        elif len(author) < 2:
            errors['author'] = 'Имя автора должно содержать не менее 2 символов'
        elif len(author) > 100:
            errors['author'] = 'Имя автора не должно превышать 100 символов'
        
        authorMail = form_data.get('authorMail', '')
        if not ValidationService.check_mail(authorMail):
            errors['authorMail'] = 'Адрес электронной почты не соотвествует шаблону'

        post_date = form_data.get('postDate', '')
        if not post_date:
            errors['postDate'] = 'Дата обязательна для заполнения'
        else:
            date_pattern = r'^\d{4}-\d{2}-\d{2}$'
            if not re.match(date_pattern, post_date):
                errors['postDate'] = 'Дата должна быть в формате ГГГГ-ММ-ДД'
            else:
                try:
                    parsed_date = datetime.strptime(post_date, '%Y-%m-%d').date()
                    if parsed_date > datetime.now().date():
                        errors['postDate'] = 'Дата не может быть в будущем'
                except ValueError:
                    errors['postDate'] = 'Введена некорректная дата'
        
        text = form_data.get('text', '')
        if not text:
            errors['text'] = 'Текст статьи обязателен для заполнения'
        elif len(text) < 20:
            errors['text'] = 'Текст статьи должен содержать не менее 20 символов'
        elif len(text) > 5000:
            errors['text'] = 'Текст статьи не должен превышать 5000 символов'
        
        return errors