.. _rest:

#########
REST APIs
#########

To start with, we import the following:

.. code-block:: python

    from accern import API as AccernAPI

Class Creation
==============

Create a API class

.. code-block:: python

    API = AccernAPI()


To authenticate, pass your secret token to a API class.

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
``kwargs``. All the available fields are shown in the above example.

.. code-block:: python

    kwargs = {
        'select': ['entity_ticker', 'entity_relevance', 'entity_industry', 'entity_sentiment']
    }

    response = API.request(method='get', **kwargs)

If you want to filter the data, the available fields for querying are the
followings:

.. include:: ../data/table_filter.rst
    :start-after: .. snip
    :end-before: .. snap

Pass the query to ``kwargs``.

.. code-block:: python

    kwargs = {
        'filter': {
            'entity_industry': ['Apparel', 'Food Chains'],
            'event': 'Accident'
        }
    }

    response = API.request(method='get', **kwargs)
