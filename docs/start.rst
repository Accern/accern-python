.. _start:

===============
Getting started
===============

This is a short tutorial on how to use accern python library for new users. You
can see complex usage in :ref:`API<API>`.

1. Contact `support@accern.com`. and inquire an Accern API token..

2. To quickly start using Accern API, create a API class and pass your token:

.. code-block:: python

    from accern import API as AccernAPI
    token = 'YOUR TOKEN'
    API = AccernAPI()
    resp = API.request(method='get')

3. Make a API request and pass params to get filtered data.

.. code-block:: python

    kwargs = {
        'params': {
            'entity_ticker': 'AAPL'
        }
    }
    resp = API.request(method='get', **kwargs)

4. Specify the fields that your are looking from the data and filter the results.

.. code-block:: python

    kwargs = {
        'fields': ['entity_industry', 'entity_ticker', 'entity_relevance']
    }
    resp = API.request(method='get', **kwargs)
