# Micro API Call Framework
Micro API Call Framework (pythapi) is a Python module for executing API calls without leveraging the native curl command. 
It uses the Python requests module to perform API calls. Why not using requests directly? The mean advantage of pythapi is that it's also available through CLI:

    $pythapi -h

You should be able to use pythapi with every API endpoint. It currently allows you the execute the next methods over HTTPS:

* GET
* POST
* PUT
* DELETE

## Requirements
pythapi uses the requests module to perform API calls. This isn't native installed and has to be installed using pip:

    $pip install requests configparser pyyaml

## Script Usage

    import pythapi

    # Specify the endpoint and the base URL.
    apiEndpoint = pythapi.Connect('localhost', '/base/api/url')

    # Get all users
    # This will perform a GET request using the URL https://localhost/base/api/url/users
    apiEndpoint.get("/users")

## CLI Usage

    $pythapi -h
    usage: pythapi <command> [<args>]

    The most commonly used HTTP methods are:
    get     HTTP GET Request
    post    HTTP POST Request
    put     HTTP PUT Request
    delete  HTTP DELETE Request

    positional arguments:
    method      HTTP method to run

    optional arguments:
    -h, --help  show this help message and exit