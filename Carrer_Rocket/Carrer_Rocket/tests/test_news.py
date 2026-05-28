from newsform import validate_date
import unittest

class TestDateValidation(unittest.TestCase):
    def test_valid_date_formats(self):
        test_cases = [
            '2025-12-31',
            '2024-02-29',
            '2000-01-01',
        ]
        for date_str in test_cases:
            with self.subTest(date=date_str):
                is_valid, result = validate_date(date_str)
                self.assertTrue(is_valid, f"Дата {date_str} должна быть валидной")

    def test_invalid_date_formats(self):
        test_cases = [
            ('', "Пустая строка"),
            ('2025-13-01', "Несуществующий месяц"),
            ('2025-12-32', "Несуществующий день"),
            ('2025-02-30', "Несуществующий день в феврале"),
            ('31.12.2025', "Неправильный формат (день.месяц.год)"),
            ('2025/12/31', "Неправильный разделитель"),
            ('abc', "Не дата"),
            ('2025-12-31 10:00', "С временем"),
        ]
        
        for date_str, description in test_cases:
            with self.subTest(date=date_str, description=description):
                is_valid, result = validate_date(date_str)
                self.assertFalse(is_valid, f"Дата {date_str} должна быть не валидной")
