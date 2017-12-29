########
Examples
########


REST: Request with filters
--------------------------

.. code-block:: python

    from accern import API
    TOKEN = 'YOUR TOKEN'
    Client = API(TOKEN)

    schema = {
        'select': [
            {
                'field': 'entity_ticker',
                'name': 'ticker'
            },
            {
                'field': 'harvested_at',
                'name': 'time'
            }
        ],
        'filters': {
            'entity_ticker': [
                "AAPL", "GOOG"
            ]
        }
    }

    resp = Client.request(schema)


REST: Get one week data for restaurants entities
------------------------------------------------

.. code-block:: python

    from accern import API
    from datetime import datetime
    import pandas as pd
    restaurants = [
        'DPZ', 'SONC', 'MCD', 'CMG', 'BWLD', 'DNKN', 'TXRH', 'PZZA',
        'EAT', 'SHAK', 'CAKE', 'YUM', 'SBUX', 'WEN', 'JACK', 'PLAY', 'DFRG',
        'TACO', 'DENN', 'HABT', 'LOCO', 'WING', 'BLMN', 'PBPB', 'RRGB', 'FRGI',
        'FOGO', 'DRI'
    ]

    schema = {
        'select': [
            {
                'field': 'entity_ticker'
            }, {
                'field': 'entity_sentiment'
            }, {
                'field': 'harvested_at'
            }, {
                'field': 'entity_relevance'
            }
        ],
        'filters': {
            'entity_relevance': [70, 100],
            'entity_ticker': restaurants,
            'harvested_at': ['2017-12-01 00:00:00', '2017-12-07 00:00:00']
        }
    }

    TOKEN = 'YOUR TOKEN'
    Client = API(TOKEN)

    response = Client.request(schema)
    ############### Get restaurants data ###############
    result = pd.DataFrame()
    while response['total'] > 0:
        df = pd.DataFrame.from_dict(response['signals'], orient='columns')
        result = result.append(df, ignore_index=True)
        schema['filters']['last_id'] = response['last_id']
        response = Client.request(schema)

    result = result.drop_duplicates().reset_index(drop=True)
    result.to_csv('restaurants.csv', index=False)

Streaming: Save to csv
----------------------

.. code-block:: python

    from accern import StreamClient, StreamListener
    from datetime import datetime
    import os
    import pandas as pd


    class MyStreamListener(StreamListener):
        def on_data(self, raw_data):
            df = pd.DataFrame.from_dict(raw_data, orient='columns')
            print ("%s - Saving %s signals..." % (datetime.now(), len(df)))
            if not os.path.exists('output.csv'):
                df.to_csv('output.csv', encoding='utf-8', index=False)
            else:
                df.to_csv('output.csv', mode='a', header=False, encoding='utf-8', index=False)

    TOKEN = 'YOUR TOKEN'
    stream = StreamClient(MyStreamListener(), TOKEN)
    stream.performs()

Streaming: Create output csv structure and seperate by hour
-----------------------------------------------------------
.. code-block:: python

    from accern import StreamListener, StreamClient
    from datetime import datetime, timedelta
    import os
    import pandas as pd
    from pymongo import MongoClient

    record = datetime.now()
    record_time = datetime(year=record.year, month=record.month, day=record.day, hour=record.hour - 1, minute=0, second=0, microsecond=0)

    class MyStreamListener(StreamListener):
        def __init__(self):
            self.db = MongoClient().accern

        def on_data(self, raw_data):
            global record_time
            df = pd.DataFrame.from_dict(raw_data, orient='columns')
            time = datetime.now()
            if (time - record_time).seconds / 60 > 60:
                record_time = record_time + timedelta(hours=1)
                df.to_csv('./accern_stream/2017-12-01/%s.csv' % (record_time.strftime('%Y-%m-%dT%H:%M:%S')), index=False, encoding='utf-8')
                print ('Appended %s signals' % (len(df)))
            else:
                df.to_csv('./accern_stream/2017-12-01/%s.csv' % (record_time.strftime('%Y-%m-%dT%H:%M:%S')), index=False, mode='a', header=False, encoding='utf-8')
                print ('Appended %s signals' % (len(df)))
    myStreamListener = MyStreamListener()

    TOKEN = 'YOUR TOKEN'
    Streamer = StreamClient(MyStreamListener(), TOKEN)

    if not os.path.exists('./accern_stream'):
        os.mkdir('./accern_stream')
    if not os.path.exists('./accern_stream/2017-12-01'):
        os.mkdir('./accern_stream/2017-12-01')

    Streamer.performs()


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

        def on_data(self, raw_data):
            data_json = raw_data
            print ("%s - Saving %s signals..." % (datetime.now(), len(data_json)))
            # Replace with your db, collection names
            self.db['accern']['stream'].insert_many(data_json)
    TOKEN = 'YOUR TOKEN'
    stream = StreamClient(MyStreamListener(), TOKEN)
    stream.performs()


Historical Data: Create one historical job
------------------------------------------

A full example can be found at
`Historical Job Example <https://github.com/Accern/accern-python/blob/master/docs/examples/historical_job.ipynb>`_

.. code-block:: python

    from accern import HistoricalClient

    TOKEN = 'YOUR TOKEN'
    Client = HistoricalClient(TOKEN)

    schema = {
        'name': 'Daily Sentiment',
        'description': 'Get Daily Sentiment data',
        "select": [
            {
                "field": "entity_ticker",
                "alias": "ticker"
            }, {
                "field": "harvested_at"
            }
        ],
        "filters": [
            {
                "entity_ticker": ["AAPL", "GOOG","MSFT"]
            }
        ]
    }
    resp = Client.create_job(schema)


Historical Data: Check the status of a historical job
-----------------------------------------------------

.. code-block:: python

    from accern import HistoricalClient
    import io
    import requests
    import pandas as pd

    token = 'YOUR TOKEN'
    Client = HistoricalClient(token)

    resp = Client.get_jobs('YOUR JOB ID')
    print resp['job']


Historical Data: Read the csv from the job's download link
----------------------------------------------------------

.. code-block:: python

    from accern import HistoricalClient
    import io
    import requests
    import pandas as pd

    token = 'YOUR TOKEN'
    Client = HistoricalClient(token)

    resp = Client.get_jobs('YOUR JOB ID')
    link = resp['job']['link']
    raw_data = requests.get(link).content
    data = pd.read_csv(io.StringIO(raw_data.decode('utf-8')))
    print data.head()
