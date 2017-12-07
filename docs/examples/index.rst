########
Examples
########

Set token for all the examples.

.. code-block:: python

    token = 'YOUR TOKEN'

REST: Request with filters
--------------------------

.. code-block:: python

    from accern import API as AccernAPI
    API = AccernAPI()
    API.token = token
    response = API.request('get')
    print (response['total'])

REST: Get one week data for restaurants entities
------------------------------------------------

.. code-block:: python

    restaurants = ['DPZ', 'SONC', 'MCD', 'CMG', 'BWLD', 'DNKN', 'TXRH', 'PZZA',
        'EAT', 'SHAK', 'CAKE', 'YUM', 'SBUX', 'WEN', 'JACK', 'PLAY', 'DFRG',
        'TACO', 'DENN', 'HABT', 'LOCO', 'WING', 'BLMN', 'PBPB', 'RRGB', 'FRGI',
        'FOGO', 'DRI']

    start_time = datetime(2017, 12, 1, 0, 0, 0, 000)
    end_time = datetime(2017, 12, 7, 23, 59, 59, 999999)

    kwargs = {
        'fields': ['entity_ticker', 'entity_sentiment', 'harvested_at', 'entity_relevance'],
        'params': {
            'entity_ticker': restaurants,
            'last_id': 0
        }
    }

    API = AccernAPI()

    API.token = token
    response = API.request('get', **kwargs)
    ############### Get restaurants data ###############
    result = pd.DataFrame({})
    print ('loading data for restaurants')
    while response['total'] > 0:
        df = pd.DataFrame.from_dict(response['signals'], orient='columns')
        result = result.append(df, ignore_index=True)
        kwargs['params']['last_id'] = response['last_id']
        response =API.request('get', **kwargs)

    result['harvested_at'] = pd.to_datetime(result['harvested_at'])
    result = result[(result['harvested_at'] > start_time) & (result['harvested_at'] < end_time)].reset_index(drop=True)
    result = result.drop_duplicates().reset_index(drop=True)
    result.to_csv('restaurants.csv', index=False)


Streaming: Save to csv
--------------------------

.. code-block:: python

    from accern import StreamClient, StreamListener
    from datetime import datetime
    import json
    import os
    import pandas as pd


    class MyStreamListener(StreamListener):
        def on_data(self, data):
            df = pd.DataFrame.from_dict(json.loads(data), orient='columns')
            print ("%s - Saving %s signals..." % (datetime.now(), len(df)))
            if not os.path.exists('output.csv'):
                df.to_csv('output.csv', encoding='utf-8', index=False)
            else:
                df.to_csv('output.csv', mode='a', header=False, encoding='utf-8', index=False)

    print ("%s - Start streaming..." % (datetime.now()))
    stream = StreamClient(MyStreamListener(), token)
    stream.performs()

Streaming: Save to mongo
------------------------

.. code-block:: python

    from accern import StreamClient, StreamListener
    from datetime import datetime
    import json
    from pymongo import MongoClient


    class MyStreamListener(StreamListener):
        def __init__(self):
            self.db = MongoClient()['accern'] # Replace with your db name

        def on_data(self, data):
            data_json = json.loads(data)
            print ("%s - Saving %s signals..." % (datetime.now(), len(data_json)))
            # Replace with your db, collection names
            self.db['accern']['stream'].insert_many(data_json)

    print ("%s - Start streaming..." % (datetime.now()))
    stream = StreamClient(MyStreamListener(), token)
    stream.performs()
