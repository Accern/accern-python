.. _rest:

#########
REST APIs
#########

To start with, we import the following:

.. code-block:: python

    from accern import API

Create API Instance
===================

Create an API instance

.. code-block:: python

    Client = API()


Authenticate REST API Client
============================

Authenticate your account when using the API token. Pass it into the REST Client
and the library will pass it to every request. An API request without a token will
fail.

Your API tokens carry many privileges. Don't share your secret API tokens in any
public spaces like Github, client-side code, etc.

To authenticate, pass it through the constructor or assign your YOUR TOKEN to
the API instance.

.. code-block:: python

    token = 'YOUR TOKEN'
    Client = API(token)

or

.. code-block:: python

    token = 'YOUR TOKEN'
    Client.token = token


If token is not passed or invalid, an ``AuthenticateError`` will be raised

Request Data
============

The request method will send a ``GET`` request to retrieve data. The response
will be the most recent 100 documents.

.. code-block:: python

    response = Client.request()

A response example.

.. include:: ../data/response.rst
    :start-after: .. snip
    :end-before: .. snap

To select only a few fields or filter some fields, build your schema and pass it
to the function.

.. code-block:: python

    schema = {
        'select': [
            {
                'field': 'entity_ticker',
                'alias': 'ticker'
            }
        ]
    }

    response = Client.request(schema)
