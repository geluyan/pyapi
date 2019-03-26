import urllib3
import unittest
import pythapi

# The following test are written with the help of https://jsonplaceholder.typicode.com
# Tests are based on the Python default unittest module

class testPythapi(unittest.TestCase):
    def test_get(self):
        """
        Test that we can receive a GET request
        """
        # Disable certificate warnings and connect to Rubrik Cluster
        urllib3.disable_warnings()
        jsonplaceholder = pythapi.Connect('jsonplaceholder.typicode.com', '')

        name = "Leanne Graham"
        user = jsonplaceholder.get("/users/1", authentication=False)

        self.assertEqual(name, user['name'])
    
    def test_post(self):
        """
        Test that we can send a POST request
        """
        # Disable certificate warnings and connect to Rubrik Cluster
        urllib3.disable_warnings()
        jsonplaceholder = pythapi.Connect('jsonplaceholder.typicode.com', '')

        data = "Leanne Graham"
        user = jsonplaceholder.get("/users/1", authentication=False)

        self.assertEqual(name, user['name'])

if __name__ == '__main__':
    unittest.main()