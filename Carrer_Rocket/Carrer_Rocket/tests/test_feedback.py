import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest
from controllers.feedback_controller import getErrorList

class TestFeedbackValidation(unittest.TestCase):
    """Тесты для проверки ввода данных в форме отзывов"""

    def test_author_validation(self):
        """Проверка имени автора"""
        valid_authors = ["Иван", "Анна-Мария", "О'Коннор", "Ли", "Алексей123"]
        for name in valid_authors:
            with self.subTest(author=name):
                errors = getErrorList(author=name, title="Нормально", text="Всё хорошо", email="test@mail.ru")
                self.assertNotIn("Имя автора должно содержать не менее 2 символов", errors)

        invalid_authors = ["", "А", "   ", "A"*1]
        for name in invalid_authors:
            with self.subTest(author=name):
                errors = getErrorList(author=name, title="Нормально", text="Всё хорошо", email="test@mail.ru")
                self.assertIn("Имя автора должно содержать не менее 2 символов", errors)

    def test_title_validation(self):
        """Проверка заголовка"""
        valid_titles = ["Супер", "Нормально", "A"*3, "A"*100]
        for title in valid_titles:
            with self.subTest(title=title):
                errors = getErrorList(author="Иван", title=title, text="Отлично", email="test@mail.ru")
                self.assertNotIn("Заголовок отзыва должен содержать не менее 3 символов", errors)
                self.assertNotIn("Заголовок не должен превышать 100 символов", errors)

        invalid_titles = ["", "AB", "A"*101, "   "]
        for title in invalid_titles:
            with self.subTest(title=title):
                errors = getErrorList(author="Иван", title=title, text="Отлично", email="test@mail.ru")
                # Проверяем, что появилась хотя бы одна из двух ошибок
                self.assertTrue(
                    any(err in errors for err in [
                        "Заголовок отзыва должен содержать не менее 3 символов",
                        "Заголовок не должен превышать 100 символов"
                    ])
                )

    def test_text_validation(self):
        """Проверка текста отзыва"""
        valid_texts = ["Отлично", "A"*5, "12345", "   Ок   "]
        for text in valid_texts:
            with self.subTest(text=text):
                errors = getErrorList(author="Иван", title="Норм", text=text, email="test@mail.ru")
                self.assertNotIn("Текст отзыва должен содержать не менее 5 символов", errors)
                if text.strip().isdigit():
                    self.assertIn("Текст не может состоять только из цифр.", errors)
                else:
                    self.assertNotIn("Текст не может состоять только из цифр.", errors)

        invalid_texts = ["", "A"*4, "12", "    "]
        for text in invalid_texts:
            with self.subTest(text=text):
                errors = getErrorList(author="Иван", title="Норм", text=text, email="test@mail.ru")
                self.assertIn("Текст отзыва должен содержать не менее 5 символов", errors)

        # Текст из одних цифр
        numeric_text = "123456"
        errors = getErrorList(author="Иван", title="Норм", text=numeric_text, email="test@mail.ru")
        self.assertIn("Текст не может состоять только из цифр.", errors)

    def test_email_validation(self):
        """Проверка email"""
        valid_emails = [
            "user@example.com",
            "m1@gmail.com",
            "first.last@domain.org",
            "123@test.ru",
            "user_name@mail.io",
            "ass@csb.cd",
            "user+filter@example.net",
            "user-name@example.co",
            "x@example.company",
            "simple@domain.name",
            "test_123@site.ru",
            "admin@mail.com"
        ]
        for email in valid_emails:
            with self.subTest(email=email):
                errors = getErrorList(author="Иван", title="Норм", text="Текст", email=email)
                self.assertNotIn("Почта не соответствует паттерну!", errors)
                self.assertNotIn("Невалидный домен", errors)

        invalid_emails = [
            "",                       # пустая строка
            "1",                      # слишком коротко
            "m1@",                    # нет домена
            "@mail",                  # нет локальной части
            "user@.com",              # точка в начале домена
            "user@domain..com",       # две точки подряд
            "user@domain.c",          # домен верхнего уровня слишком короткий
             "user@domain.cfggfgfgfg", # домен верхнего уровня слишком длинный
            "user name@domain.com",   # пробел в локальной части
            "user@domain,com",        # запятая вместо точки
            "user@domain.cоm",        # кириллическая 'о' в домене
            "user@-domain.com",       # домен начинается с дефиса
            "user@domaiы-.com",       # домен заканчивается дефисом
            "user@domain.com.",       # точка в конце
            ".user@domain.com",       # локальная часть начинается с точки
            "user@domain..com",       # две точки в домене
            "a" * 65 + "@example.com", # локальная часть длиннее 63 символов
            "user@a" * 30 + ".com",   # слишком длинное имя домена
        ]
        for email in invalid_emails:
            with self.subTest(email=email):
                errors = getErrorList(author="Иван", title="Норм", text="Текст", email=email)
                self.assertTrue(
                    any(err in errors for err in [
                        "Почта не соответствует паттерну!",
                        "Невалидный домен"
                    ])
                )

        # Домены не из списка
        bad_domains = ["test@site.xyz",  "foo@bar.org.ua"]
        for email in bad_domains:
            with self.subTest(email=email):
                errors = getErrorList(author="Иван", title="Норм", text="Текст", email=email)
                self.assertIn("Невалидный домен", errors)


if __name__ == '__main__':
    unittest.main()