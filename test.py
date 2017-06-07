import unittest
import vcr
import requests


def request():
    res = requests.get('http://github.com')
    return res.status_code


class RequestTest(unittest.TestCase):

    @vcr.use_cassette('github.yml')
    def test_request(self):
        code = request()
        self.assertEqual(code, 400)


if __name__ == '__main__':
    unittest.main()
