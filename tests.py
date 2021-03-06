import unittest
from app import meu_web_app


class TestCuducos(unittest.TestCase):

    def setUp(self):
        app = meu_web_app.test_client()
        self.response = app.get('/cuducos')

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_content_type(self):
        self.assertIn('text/html', self.response.content_type)

    def test_content(self):
        response_str = self.response.data.decode('utf-8')
        self.assertIn('<title>Eduardo Cuducos</title>', str(response_str))
        self.assertIn('<h1>Eduardo Cuducos</h1>', str(response_str))
        self.assertIn('<p>Sociólogo, ', str(response_str))

    def test_bootstrap_css(self):
        response_str = self.response.data.decode('utf-8')
        self.assertIn('bootstrap.min.css', response_str)

    def test_profile_image(self):
        response_str = self.response.data.decode('utf-8')
        self.assertIn('<img src="', response_str)
        self.assertIn('class="img-circle"', response_str)

    def test_link(self):
        response_str = self.response.data.decode('utf-8')
        self.assertIn('href="http://twitter.com/cuducos"', response_str)
        self.assertIn('>Me siga no Twitter</a>', response_str)


class TestZ4r4tu5tr4(unittest.TestCase):

    def setUp(self):
        app = meu_web_app.test_client()
        self.response = app.get('/z4r4tu5tr4')

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_content_type(self):
        self.assertIn('text/html', self.response.content_type)

    def test_content(self):
        response_str = self.response.data.decode('utf-8')
        self.assertIn('<title>Eduardo Mendes</title>', str(response_str))
        self.assertIn('<h1>Eduardo Mendes</h1>', str(response_str))
        self.assertIn('<p>Apaixonado por software livre', str(response_str))

    def test_bootstrap_css(self):
        response_str = self.response.data.decode('utf-8')
        self.assertIn('bootstrap.min.css', response_str)

    def test_profile_image(self):
        response_str = self.response.data.decode('utf-8')
        self.assertIn('<img src="', response_str)
        self.assertIn('class="img-circle"', response_str)

    def test_link(self):
        response_str = self.response.data.decode('utf-8')
        self.assertIn('href="http://github.com/z4r4tu5tr4"', response_str)
        self.assertIn('>Me siga no GitHub</a>', response_str)

if __name__ == '__main__':
    unittest.main()