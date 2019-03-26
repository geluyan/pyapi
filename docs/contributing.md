# Contributing to pythapi
If you like to help out and add new features or fix any kind of bugs, you need to follow specific procedures and rules.

## Contribution Procedure
1. Fork the project to your personal Github account
2. Clone the fork to your local development machine
3. Checkout the `devel` branche
4. Make changes to the code
5. Run any kind of tests by building the project localy using `python setup.py install`
6. Use the tests folder to perform and create Unit Tests with Python unittest module
7. Repeat step 4-6 until everything is working as expected
8. Commit to your `devel` branche
9. Push the changes to your Github fork
10. Make a pull request from your `devel` branche to the original `devel` branche

Don't change the CHANGELOG, make sure you have documented your changes in the `docs` using `mkdocs`

## Documentation
The documentation is written using `mkdocs`. You can serve the documentation site using the next command in the root of the project folder:

    $pip install mkdocs
    $mkdocs serve

This will launch a web server on `http://localhost:8000`. As soon you've updated the documentation, the changes are updated immediatly on the web interface.