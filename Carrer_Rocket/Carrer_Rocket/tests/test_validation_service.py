# tests/test_validation_service.py
import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from services.validation_service import ValidationService


class TestValidationService(unittest.TestCase):
    
    def setUp(self):
        self.valid_form_data = {
            'header': 'Тестовая новость',
            'description': 'Это описание тестовой новости',
            'author': 'Тест Автор',
            'postDate': '2025-05-27',
            'text': 'Это достаточно длинный текст новости для тестирования валидации'
        }
    
    def test_valid_form_no_errors(self):
        errors = ValidationService.validate_news_form(self.valid_form_data)
        self.assertEqual(len(errors), 0)
    
    def test_empty_header_returns_error(self):
        self.valid_form_data['header'] = ''
        errors = ValidationService.validate_news_form(self.valid_form_data)
        self.assertIn('header', errors)
        self.assertEqual(errors['header'], 'Заголовок обязателен для заполнения')
    
    def test_short_header_returns_error(self):
        self.valid_form_data['header'] = 'ab'
        errors = ValidationService.validate_news_form(self.valid_form_data)
        self.assertIn('header', errors)
        self.assertEqual(errors['header'], 'Заголовок должен содержать не менее 3 символов')
    
    def test_empty_description_returns_error(self):
        self.valid_form_data['description'] = ''
        errors = ValidationService.validate_news_form(self.valid_form_data)
        self.assertIn('description', errors)
        self.assertEqual(errors['description'], 'Описание обязательно для заполнения')
    
    def test_short_description_returns_error(self):
        self.valid_form_data['description'] = 'коротко'
        errors = ValidationService.validate_news_form(self.valid_form_data)
        self.assertIn('description', errors)
        self.assertEqual(errors['description'], 'Описание должно содержать не менее 10 символов')
    
    def test_empty_author_returns_error(self):
        self.valid_form_data['author'] = ''
        errors = ValidationService.validate_news_form(self.valid_form_data)
        self.assertIn('author', errors)
        self.assertEqual(errors['author'], 'Автор обязателен для заполнения')
    
    def test_short_author_returns_error(self):
        self.valid_form_data['author'] = 'А'
        errors = ValidationService.validate_news_form(self.valid_form_data)
        self.assertIn('author', errors)
        self.assertEqual(errors['author'], 'Имя автора должно содержать не менее 2 символов')
    
    def test_empty_date_returns_error(self):
        self.valid_form_data['postDate'] = ''
        errors = ValidationService.validate_news_form(self.valid_form_data)
        self.assertIn('postDate', errors)
        self.assertEqual(errors['postDate'], 'Дата обязательна для заполнения')
    
    def test_invalid_date_format_returns_error(self):
        self.valid_form_data['postDate'] = '27.05.2025'
        errors = ValidationService.validate_news_form(self.valid_form_data)
        self.assertIn('postDate', errors)
        self.assertEqual(errors['postDate'], 'Дата должна быть в формате ГГГГ-ММ-ДД')
    
    def test_future_date_returns_error(self):
        self.valid_form_data['postDate'] = '2030-12-31'
        errors = ValidationService.validate_news_form(self.valid_form_data)
        self.assertIn('postDate', errors)
        self.assertEqual(errors['postDate'], 'Дата не может быть в будущем')
    
    def test_valid_date_format_no_error(self):
        self.valid_form_data['postDate'] = '2023-01-15'
        errors = ValidationService.validate_news_form(self.valid_form_data)
        self.assertNotIn('postDate', errors)
    
    def test_empty_text_returns_error(self):
        self.valid_form_data['text'] = ''
        errors = ValidationService.validate_news_form(self.valid_form_data)
        self.assertIn('text', errors)
        self.assertEqual(errors['text'], 'Текст новости обязателен для заполнения')
    
    def test_short_text_returns_error(self):
        self.valid_form_data['text'] = 'Короткий текст'
        errors = ValidationService.validate_news_form(self.valid_form_data)
        self.assertIn('text', errors)
        self.assertEqual(errors['text'], 'Текст новости должен содержать не менее 20 символов')
    
    def test_multiple_errors_returned(self):
        invalid_data = {
            'header': '',
            'description': '',
            'author': '',
            'postDate': 'invalid',
            'text': ''
        }
        errors = ValidationService.validate_news_form(invalid_data)
        self.assertIn('header', errors)
        self.assertIn('description', errors)
        self.assertIn('author', errors)
        self.assertIn('postDate', errors)
        self.assertIn('text', errors)
        self.assertEqual(len(errors), 5)


if __name__ == '__main__':
    unittest.main()