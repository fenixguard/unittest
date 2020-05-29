import requests
import unittest


class YaTest(unittest.TestCase):

    def test_smoke(self):
        resp = requests.get('http://yandex.ru')
        self.assertEqual(resp.status_code, 200)

        data = resp.content
        self.assertNotEqual(data, '')


