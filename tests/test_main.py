import urllib3
import unittest
import pythapi

# The following test are written with the help of https://my-json-server.typicode.com
# Tests are based on the Python default unittest module

class testPythapi(unittest.TestCase):
    def test_get(self):
        """
        Test that we can receive a GET request
        """
        # Disable certificate warnings and connect to Rubrik Cluster
        urllib3.disable_warnings()
        jsonplaceholder = pythapi.Connect('my-json-server.typicode.com', '/geluyan/pythapi')

        name = "geluykens"
        user = jsonplaceholder.get("/users/1", authentication=False)

        self.assertEqual(name, user['name'])
    
    def test_post(self):
        """
        Test that we can send a POST request
        """
        # Disable certificate warnings and connect to Rubrik Cluster
        urllib3.disable_warnings()
        jsonplaceholder = pythapi.Connect('my-json-server.typicode.com', '/geluyan/pythapi')

        data = {
            "id": 4,
            "name": "Doe",
            "firstname": "Luc",
            "title": "Testing Engineer"
        }
        user = jsonplaceholder.post("/users", data, authentication=False)

        self.assertEqual(data, user)

    def test_put(self):
        """
        Test that we can send a PUT request
        """
        # Disable certificate warnings and connect to Rubrik Cluster
        urllib3.disable_warnings()
        jsonplaceholder = pythapi.Connect('my-json-server.typicode.com', '/geluyan/pythapi')

        data = {
            "id": 1,
            "name": "Doe",
            "firstname": "Luc",
            "title": "Testing Engineer"
        }
        user = jsonplaceholder.put("/users/1", data, authentication=False)

        self.assertEqual(data, user)
    
    def test_delete(self):
        """
        Test that we can send a DELETE request
        """
        # Disable certificate warnings and connect to Rubrik Cluster
        urllib3.disable_warnings()
        jsonplaceholder = pythapi.Connect('my-json-server.typicode.com', '/geluyan/pythapi')

        user = jsonplaceholder.delete("/users/1", authentication=False)

if __name__ == '__main__':
    unittest.main()