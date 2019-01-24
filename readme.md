# Stores REST API Testing

This is built with Flask, Flask-RESTful, Flask-JWT, and Flask-SQLAlchemy.

Deployed with Docker.

## Section 8

### Testing

> Note : This section code stars at end of last section.

Set up for Pycharm Docker plugin:

1. Build local Flask app image:

    ```bash
    $ docker build --rm -t automated_testing:section08 .
    ```
2. Start Postgres container:

    ```bash
    $ docker run --env POSTGRES_PASSWORD=password \
       --name postgres \
       -d \
       postgres:9.6 
    ```
3. Run tests container with bind mount:

    ```bash
    $ docker run -v "C:\MOOC18\Automated Software Testing with Python\section6\code:/code" \
       --env DATABASE_URL=postgresql://postgres:password@postgres:5432/ \
       --name unittests \
       --link postgres \
       automated_testing:section08 \
       python -m unittest
    ```
    
    > Note: we are not using `--rm` flag here, this is because the PyCharm Docker plugin does not remove containers correctly.
    You will have to remove the container manually after every run (for now).
    
    You can also run
    
    - `python -m unittest discover -v -s tests/unit -t . -p "test_*.py"` to perform unit tests only and
    - `python -m unittest discover -v -s tests/integration -t . -p "test_*.py"` to just run integration tests
    
    Where:
    
    - `-v` verbose
    - `-s <start directory>` where to look for test cases
    - `-t <top level directory>` where your top directory is, (`.` means source code root)
    - `-p <pattern>` file naming pattern for test cases

### Running App

You may also choose to run the app so that it is possible to run API tests using an external tool, e.g. Postman.

- Simply repeat steps 1 and 2 of the [Testing](#testing) section, then run the following command:

    ```bash
    $ docker run -v "C:\MOOC18\Automated Software Testing with Python\section6\code:/code" \
       --env DATABASE_URL=postgresql://postgres:password@postgres:5432/ \
       --name app \
       --link postgres \
       automated_testing:section08 \
       python app.py
    ```
    
    This *should* expose port `5000` on localhost.