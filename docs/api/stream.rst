.. _stream:

####################
Streaming API Client
####################

Stream Listener
===============

Create StreamListener and to handle streaming data.

.. code-block:: python

    from accern import Stream

    myStreamListener = StreamListener()

Override `on_data` function if you want to handle the data yourself.

By default, it's returning the raw data.

.. code-block:: python

    class MyStreamListener(StreamListener):
        def on_data(self, data):
            df = json.loads(data), orient='columns')
            print (df.head())


Authenticate Stream Client
==========================

.. code-block:: python

    from accern import StreamClient
    token = 'YOUR TOKEN'

    schema = {}
    stream = StreamClient(myStreamListener, token, **schema)


Filter and select with schema
=============================

.. code-block:: python

    from accern import StreamClient, StreamListener

    schema = {
        'select': [
            {
                'field': 'entity_ticker',
                'name': 'ticker'
            },
            {
                'field': 'harvested_at',
                'name': 'hour'
            }
        ],
        'filters': {
            'entity_ticker': [
                'AAPL', 'AMZN'
            ]
        }
    }
    stream = StreamClient(MyStreamListener(), token, **schema)
    stream.performs()
