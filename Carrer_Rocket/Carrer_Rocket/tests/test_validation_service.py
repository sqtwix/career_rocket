# tests/test_validation_service.py
import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from services.validation_service import ValidationService


class TestValidationService(unittest.TestCase):
    
    def setUp(self):
        self.valid_form_data = {
            'header': 'Тестовая статья',
            'description': 'Это описание тестовой статьи',
            'author': 'Тест Автор',
            'postDate': '2025-05-27',
            'text': 'Это достаточно длинный текст статьи для тестирования валидации'
        }
    
    def test_empty_header_returns_error(self):
        self.valid_form_data['header'] = ''
        errors = ValidationService.validate_article_form(self.valid_form_data)
        self.assertIn('header', errors)
        self.assertEqual(errors['header'], 'Заголовок обязателен для заполнения')
    
    def test_short_header_returns_error(self):
        self.valid_form_data['header'] = 'ab'
        errors = ValidationService.validate_article_form(self.valid_form_data)
        self.assertIn('header', errors)
        self.assertEqual(errors['header'], 'Заголовок должен содержать не менее 3 символов')
    
    def test_long_header_returns_error(self):
        self.valid_form_data['header'] = 'A' * 201
        errors = ValidationService.validate_article_form(self.valid_form_data)
        self.assertIn('header', errors)
        self.assertEqual(errors['header'], 'Заголовок не должен превышать 200 символов')
    
    def test_empty_description_returns_error(self):
        self.valid_form_data['description'] = ''
        errors = ValidationService.validate_article_form(self.valid_form_data)
        self.assertIn('description', errors)
        self.assertEqual(errors['description'], 'Описание обязательно для заполнения')
    
    def test_short_description_returns_error(self):
        self.valid_form_data['description'] = 'коротко'
        errors = ValidationService.validate_article_form(self.valid_form_data)
        self.assertIn('description', errors)
        self.assertEqual(errors['description'], 'Описание должно содержать не менее 10 символов')
    
    def test_long_description_returns_error(self):
        self.valid_form_data['description'] = 'A' * 501
        errors = ValidationService.validate_article_form(self.valid_form_data)
        self.assertIn('description', errors)
        self.assertEqual(errors['description'], 'Описание не должно превышать 500 символов')
    
    def test_empty_author_returns_error(self):
        self.valid_form_data['author'] = ''
        errors = ValidationService.validate_article_form(self.valid_form_data)
        self.assertIn('author', errors)
        self.assertEqual(errors['author'], 'Автор обязателен для заполнения')
    
    def test_short_author_returns_error(self):
        self.valid_form_data['author'] = 'А'
        errors = ValidationService.validate_article_form(self.valid_form_data)
        self.assertIn('author', errors)
        self.assertEqual(errors['author'], 'Имя автора должно содержать не менее 2 символов')
    
    def test_long_author_returns_error(self):
        self.valid_form_data['author'] = 'A' * 101
        errors = ValidationService.validate_article_form(self.valid_form_data)
        self.assertIn('author', errors)
        self.assertEqual(errors['author'], 'Имя автора не должно превышать 100 символов')
    
    def test_empty_date_returns_error(self):
        self.valid_form_data['postDate'] = ''
        errors = ValidationService.validate_article_form(self.valid_form_data)
        self.assertIn('postDate', errors)
        self.assertEqual(errors['postDate'], 'Дата обязательна для заполнения')
    
    def test_invalid_date_format_returns_error(self):
        self.valid_form_data['postDate'] = '27.05.2025'
        errors = ValidationService.validate_article_form(self.valid_form_data)
        self.assertIn('postDate', errors)
        self.assertEqual(errors['postDate'], 'Дата должна быть в формате ГГГГ-ММ-ДД')
    
    def test_future_date_returns_error(self):
        self.valid_form_data['postDate'] = '2030-12-31'
        errors = ValidationService.validate_article_form(self.valid_form_data)
        self.assertIn('postDate', errors)
        self.assertEqual(errors['postDate'], 'Дата не может быть в будущем')
    
    def test_valid_date_format_no_error(self):
        self.valid_form_data['postDate'] = '2023-01-15'
        errors = ValidationService.validate_article_form(self.valid_form_data)
        self.assertNotIn('postDate', errors)
    
    def test_empty_text_returns_error(self):
        self.valid_form_data['text'] = ''
        errors = ValidationService.validate_article_form(self.valid_form_data)
        self.assertIn('text', errors)
        self.assertEqual(errors['text'], 'Текст статьи обязателен для заполнения')
    
    def test_short_text_returns_error(self):
        self.valid_form_data['text'] = 'Короткий текст'
        errors = ValidationService.validate_article_form(self.valid_form_data)
        self.assertIn('text', errors)
        self.assertEqual(errors['text'], 'Текст статьи должен содержать не менее 20 символов')
    
    def test_long_text_returns_error(self):
        self.valid_form_data['text'] = 'A' * 5001
        errors = ValidationService.validate_article_form(self.valid_form_data)
        self.assertIn('text', errors)
        self.assertEqual(errors['text'], 'Текст статьи не должен превышать 5000 символов')
    
    def test_valid_yandex_ru_email(self):
        result = ValidationService.check_mail('username@yandex.ru')
        self.assertTrue(result)
    
    def test_valid_gmail_com_email(self):
        result = ValidationService.check_mail('testuser@gmail.com')
        self.assertTrue(result)
    
    def test_valid_mail_ru_email(self):
        result = ValidationService.check_mail('contact@mail.ru')
        self.assertTrue(result)
    
    def test_valid_mail_com_email(self):
        result = ValidationService.check_mail('info@mail.com')
        self.assertTrue(result)
    
    def test_valid_yahoo_com_email(self):
        result = ValidationService.check_mail('user@yahoo.com')
        self.assertTrue(result)
    
    def test_email_with_numbers(self):
        result = ValidationService.check_mail('user12345@yandex.ru')
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main(verbosity=2)