# Contributing to pythapi
If you like to help out and add new features or fix any kind of bugs, you need to follow specific procedures and rules.

## Contribution Procedure
1. Fork the project to your personal Github account
2. Clone the fork to your local development machine
3. Checkout the `devel` branche
4. Make changes to the code
5. Run any kind of tests by building the project localy using `python setup.py install`
6. Repeat step 4-5 until everything is working as expected
7. Commit to your `devel` branche
8. Push the changes to your Github fork
9. Make a pull request from your `devel` branche to the original `devel` branche

Don't change the CHANGELOG, make sure you have documented your changes in the `docs` using `mkdocs`

## Documentation
The documentation is written using `mkdocs`. You can serve the documentation site using the next command in the root of the project folder:

    $pip install mkdocs
    $mkdocs serve

This will launch the web server on `http://localhost:8000`. As soon you've updated the documentation, the changes are updated immediatly on the web interface.