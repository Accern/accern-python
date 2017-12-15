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

To authenticate, pass it through the constructor or assign your secret token to
the API instance.

.. code-block:: python

    token = 'SECRET TOKEN'
    Client = API(token)

or

.. code-block:: python

    token = 'SECRET TOKEN'
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

To select only a few fields or rename the fields, pass the names of the fields
you want to ``schema``. All the available fields are shown in the above example.

.. code-block:: python

    schema = {
        'select': [
            {
                'field': 'entity_ticker',
                'name': 'ticker'
            }
        ]
    }

    response = Client.request(schema)

The name for the selected fields is optional and you can select multiple fields.

.. code-block:: python

    schema = {
        'select': [
            {
                'field': 'entity_ticker',
                'name': 'ticker'
            }, {
                'field': 'harvested_at'
            }
        ]
    }

    response = Client.request(schema)

If you want to filter the data, the available fields to filter by are the
following:

.. include:: ../data/table_filter.rst
    :start-after: .. snip
    :end-before: .. snap

Pass the filters to ``schema``. The value can be a single value or an array of
values.

.. code-block:: python

    schema = {
        'filters': {
            'entity_industry': ['Apparel', 'Food Chains'],
            'event': 'Accident'
        }
    }

    response = Client.request(schema)

Cookbook
========

A list of filter examples is available at :ref:`Cookbook<Field Filter Cookbook>`
