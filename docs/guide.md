# User guide

## Installing pythapi
pythapi is made available through pypi. It can be installed using pip:

    $ pip install pythapi

If your system uses both Python 2 or Python 3, you can also install pathapi for python 3:

    $ pip3 install pythapi

If you're not using pip or pip isn't available on you system. You can also download pythap from pypi or directly from github, extract and then install it:

    $ python setup.py install

## Basic methods
pythapi has the 4 default HTTP(s) methods:

* GET
* POST
* PUT
* DELETE

All 4 methods can be called after you've created an endpoint connection.

## Creating the API connection
Before you can execute any API calls, pythapi has to know the endpoint and the base URL:

    apiEndpoint = pythapi.Connect('localhost', '/base/api/url')

## GET
`GET` is a basic API call with an URL and a query part. If you don't need authentication with your API call, you have to set authentication to `False`:

    apiEndpoint.get("/users", , authentication=False)

If you have parameters to pass:

    apiEndpoint.get("/users?name=john&age=34", authentication=False)

## POST
Passing a body using `POST` can be done by passing a data parameter:

    data={
        "password": "password",
        "username": "username"
    }
    
    # This post call will get a token. The authorication has been disabled for this because an username and password is send without an authorization in the header
    result = apiEndpoint.post('/login', data, authentication=False)

## PUT
The same example as above can be used for `PUT`:

    data={
        "oldpassword": "password",
        "username": "username",
        "newpassword": "iamanewpassword"
    }
    
    # This time I'm not passing the 'authentication' parameter because it's 'True' by default.
    result = apiEndpoint.put('/changepassword', data)

## DELETE
The `DELETE` method looks the same as the `GET`method:

    # Delete user with ID 12
    result = apiEndpoint.delete('/users/12')

## Security
pythapi currenlty only supports API calls over `HTTPS`. By default, it requires an `authorization` parameter in the `header`. This parameter contains an access token and a token type in the format of:

    <type> + ' ' + <token>

For example, the `POST` API call example performs a login with an username and a password. The `authorization` is set to `False` so pythapi sends a header without the `authorization`parameter.

As soon you have the result from this `POST` call, you can configure the `authorization`with the results:

    # Configure the authorization header info
    apiEndpoint.authorization = result['tokenType'] + ' ' + result['accessToken']

This results in:

    'Basic abcdefghijklmnopqrstuvwxyz'

Now every other API call you perform will pass this result as its `authorization` parameter. Other authorization types can be:

* Bearer
* Digest
* HOBA
* Mutual
* AWS4-HMAC-SHA256