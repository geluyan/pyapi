# CLI Operations
The biggest advantage of pythapi is the CLI interface. You can directly perform API call against your endpoint on the CLI. How awesome is that ;)

After you've installed pythapi through pip, pythapi is available over the CLI using:

    $pythapi

## Help
While you're using pythapi over the CLI, you can access the help menu during every command using the `-h` argument:

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

## Configuration
Before you can use the CLI, you need to create a configuration file. The configuration file contains very important parameters required for pythapi to work.
Create a `config` file in your home directory under the folder `.pythapi`:

    $vi ~/.pythapi/config

    [default]
    endpoint = localhost
    base_url = /base/api/url

    [auth]
    authentication = True
    auth_key = Basic abcdefghijklmnopqrstuvwxyz

    [swagger]
    file = swagger.yaml

Initially, you probably have to authenticate against your endpoint. Set the `authentication` to `False` when you launch a login `POST` request to get your authentication type and token.
After you received your authentication type and code, enter them in the config file and set the `authentication` parameter back to `True`.

!!! warning
    Don't add `''` or `""` to any of these parameters.

## GET
The `get` is the most easiest HTTP method. Just use the `get` method and pass a `path` argument:

    $pythapi get /users

## POST
`post` requires a body to be send. You can't enter the body on the CLI. In some circumstances the body is very small but currenlty pythapi only supports the body from a json file:

    $cat body.json
    {
        "password": "password",
        "username": "username"
    }

    $pythapi post /login body.json

## PUT
`put` acts the same like `post`:

    $cat body.json
    {
        "oldpassword": "password",
        "username": "username",
        "newpassword": "iamanewpassword"
    }

    $pythapi put /changepassword body.json

## DELETE
And at last, the `delete` method is the same as the `get` method:

    $pythapi delete /users/12

## Swagger
pythapi also includes a swagger viewer. You can list all available API paths and methods. You can even get the description of a path and it's paramaters.
To be able to use the viewer, pythapi need to know where your Swagger yaml of json file is located. This can be configured in your config file:

    $vi ~/.pythapi/config

    ...
    [swagger]
    file = swagger.yaml
    ...

Because Python isn't very fast with processing yaml files, the file is first converted to a json file. As soon you call `$pythapi swagger`, a new file will be created with a `.json` postfix. The next time you call `pythapi swagger`, the file isn't converted anymore and the `.json` file is used for future references. If you delete the `.json` file, the next time you call `$pythapi swagger`, the file is converted again.

    # Get a list of available API calls
    $pythapi swagger -l

    # Filter the output
    #pythapi swagger -l -f login

    # Get more information about a API call
    $pythapi swagger /login

Currenlty `pythapi` doesn't support the viewing of a `body` example for `POST` and `PUT`. You still need the documentation of your API endpoint on how to format a body file.