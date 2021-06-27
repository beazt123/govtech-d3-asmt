import json
import unittest
from BaseTestCase import BaseTestCase




class TestShortenerEndpt(BaseTestCase):
    def testNoLink(self):
        test_request = {
            "url": None
        }
        response = self.client.post("/shortener", json=test_request)
        response_dict = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response_dict["description"], "No URL submitted")
        

    def TestFaultyLink(self):

        pass
if __name__ == "__main__":
    unittest.main()