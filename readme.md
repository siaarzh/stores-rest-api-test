# Stores REST API Testing

This is built with Flask, Flask-RESTful, Flask-JWT, and Flask-SQLAlchemy.

Deployed with Docker.

## Section 6

> Note: at this point I have switched to developing all my apps with Docker

Set up for Pycharm Docker plugin:

1. Build local Flask app image:

    ```bash
    $ docker build --rm -t automated-testing:section06 .
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
       automated-testing:section06 \
       python -m unittest discover tests
    ```
    > Note: we are not using `--rm` flag here, this is because the PyCharm Docker plugin does not remove containers correctly.
    You will have to remove the container manually after every run (for now).