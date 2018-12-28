import json
import os
import unittest

from app import app


class BaseTestCase(unittest.TestCase):
    """Base class for all tests"""

    def setUp(self):
        app.config["TESTING"] = True
        self.app = app.test_client()

    def load_test_json_file(self, file_name):
        return json.loads(self.read_test_file(file_name))

    def read_test_file(self, file_name, mode="r"):
        dir = os.path.dirname(__file__)
        full_path = f"{dir}/{file_name}"
        with open(full_path, mode) as data:
            return data.read()
