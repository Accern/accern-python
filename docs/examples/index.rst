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
--------------------------

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
`Historical Job Example <https://raw.githubusercontent.com/Accern/accern-python/master/docs/_static/historical_job.html>`_

.. code-block:: python

    from accern import HistoricalClient

    TOKEN = 'YOUR TOKEN'
    Client = HistoricalClient(TOKEN)

    schema = {
        'name': 'Daily Sentiment',
        'description': 'Get Daily Sentiment data',
        "select": [
            {
                "field":"entity_ticker",
                "name": "ticker"
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
