.. _start:

===============
Getting started
===============

This is a short tutorial on how to use accern python library for new users. You
can see complex usage in :ref:`API<API>`.

1. Contact `support@accern.com`. and inquire about an Accern API token.

2. To quickly start using the Accern API, create an API instance and pass your token:

.. code-block:: python

    from accern import API
    token = 'YOUR TOKEN'
    Client = API(token)

3. Pass params to get filtered data and make an API request.

.. code-block:: python

    schema = {
        'filters': {
            'entity_ticker': 'AAPL'
        }
    }
    resp = Client.request(schema)

4. Specify the fields that your are looking for in the data and filter the results.

.. code-block:: python

    schema = {
        'select': [
            {
                'field': 'entity_industry'
            }, {
                'field': 'entity_ticker'
            }, {
                'field': 'entity_relevance'
            }
        ]
    }
    resp = Client.request(schema)
