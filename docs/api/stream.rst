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

Authenticate your account when using the API token. Pass it into Stream Client
and the library will pass it to every request. Stream request without token will
fail.

Your API tokens carry many privileges. Don't share your secret API tokens in any
public areas like Github, client-side code, etc.

.. code-block:: python

    from accern import StreamClient
    token = 'YOUR TOKEN'
    stream = StreamClient(myStreamListener, token)
