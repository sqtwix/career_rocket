import unittest

from services import news_service

class NewsServiceTest(unittest.TestCase):
    def news_service_data_amount_test(self):
        expect = news_service.NewsService.get_all_news().count()
        actual = 30
        self.assertEqual(expect, actual)

        