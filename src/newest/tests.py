import app
import unittest
import tempfile


class AppTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.app.test_client()
        with app.app.app_context():
            app.app.config["DB_PATH"] = tempfile.mktemp()
            app.create_db()

    def tearDown(self):
        with app.app.app_context():
            app.close_db(0)

    def test_passthis(self):
        self.assertEqual(1, 1)

if __name__ == "__main__":
    unittest.main()
