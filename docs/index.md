# Micro API Call Framework

Micro API Call Framework (pythapi) is a Python module for executing API calls without leveraging the native curl command.

You should be able to use pythapi with every API endpoint. It currently allows you the execute the next methods over HTTPS:

* GET
* POST
* PUT
* DELETE

## Basic Usage

    import pythapi

    # Specify the endpoint and the base URL.
    apiEndpoint = pythapi.Connect('localhost', '/base/api/url')

    # Get all users
    # This will perform a GET request using the URL https://localhost/base/api/url/users
    apiEndpoint.get("/users")
