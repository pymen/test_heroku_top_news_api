import unittest

from mock import patch
from werkzeug.exceptions import Forbidden

from tests import BaseTestCase


class TestViewsCase(BaseTestCase):
    """Testing API views"""

    def get_news_response(self):
        return self.app.get("/")

    @patch("app.get_top_news")
    def test_news_api_success(self, _mock):
        """Check good case: when 3rd party api response is correct"""
        good_response_data = self.load_test_json_file("valid_news_api_data.json")

        _mock.return_value = good_response_data
        response = self.get_news_response()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, good_response_data)

    @patch("app.get_top_news")
    def test_news_api_fail(self, _mock):
        """Check good case: when 3rd party api response is not valid (Forbidden)"""
        _mock.side_effect = Forbidden
        response = self.get_news_response()
        self.assertEqual(response.status_code, 403)
        self.assertIn("403 Forbidden: You don't have the permission", response.json["error"])

    @patch("app.get_top_news")
    def test_news_api_invalid_api_key(self, _mock):
        """Check good case: when 3rd party api key is invalid"""
        invalid_api_key_response_data = self.load_test_json_file("invalid_api_key_news_api.json")

        _mock.return_value = invalid_api_key_response_data
        response = self.get_news_response()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, invalid_api_key_response_data)


if __name__ == "__main__":
    unittest.main()
