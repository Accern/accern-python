.. _rest:

#########
REST APIs
#########

To start with, we import the following:

.. code-block:: python

    from accern import API as AccernAPI

Create API Instance
===================

Create a API instance

.. code-block:: python

    API = AccernAPI()


Authenticate RESP API Client
============================

Authenticate your account when using the API token. Pass it into Stream Client
and the library will pass it to every request. Stream request without token will
fail.

Your API tokens carry many privileges. Don't share your secret API tokens in any
public areas like Github, client-side code, etc.


To authenticate, assign your secret token to the API instance.

.. code-block:: python

    token = 'SECRET TOKEN'
    API.token = token

If token is not passed or invalid, an ``AuthenticateError`` will be raised

Request Data
============

Get Request to get data. The response return the most recent 100 documents.

.. code-block:: python

    response = API.request(method='get')

A response example.

.. include:: ../data/response.rst
    :start-after: .. snip
    :end-before: .. snap

To hide some fields from the response, pass the names of the fields you want to
``schema``. All the available fields are shown in the above example.

.. code-block:: python

    schema = {
        'select': [
            {
                'field': 'entity_ticker',
                'name': 'ticker'
            }]
    }

    response = API.request(schema)

The name for the selected fields is optional. Can select multiple fields.

.. code-block:: python

    schema = {
        'select': [
            {
                'field': 'entity_ticker',
                'name': 'ticker'
            }, {
                'field': 'harvested_at',
                'name': 'ticker'
            }
        ]
    }

    response = API.request(schema)

If you want to filter the data, the available fields to filter are the
followings:

.. include:: ../data/table_filter.rst
    :start-after: .. snip
    :end-before: .. snap

Pass the query to ``schema``.

.. code-block:: python

    schema = {
        'filters': {
            'entity_industry': ['Apparel', 'Food Chains'],
            'event': 'Accident'
        }
    }

    response = API.request(schema)

Cookbook
========

A list of examples of ``filters`` example is available at
:ref:`Cookbook<Field Filter Cookbook>`
