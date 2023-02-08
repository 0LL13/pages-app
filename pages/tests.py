from django.test import SimpleTestCase


class SimpleTests(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_about_page_status_code(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

    def test_musik_page_status_code(self):
        response = self.client.get('/musik/')
        self.assertEqual(response.status_code, 200)

    def test_verpflegung_page_status_code(self):
        response = self.client.get('/verpflegung/')
        self.assertEqual(response.status_code, 200)

    def test_parken_page_status_code(self):
        response = self.client.get('/parken/')
        self.assertEqual(response.status_code, 200)
