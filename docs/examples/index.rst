########
Examples
########

REST: Request with filters
--------------------------

.. code-block:: python

    from accern import API as AccernAPI
    API = AccernAPI()
    token = 'YOUR TOKEN'
    response = API.request('get')
    print (response['total'])


Streaming: Save to csv
--------------------------

.. code-block:: python

    from accern import StreamListener, Stream
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

    token = 'YOUR TOKEN'
    print ("%s - Start streaming..." % (datetime.now()))
    stream = Stream(MyStreamListener(), token)
    stream.performs()

Streaming: Save to mongo
------------------------

.. code-block:: python

    from accern import StreamListener, Stream
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


    token = 'YOUR TOKEN'
    print ("%s - Start streaming..." % (datetime.now()))
    stream = Stream(MyStreamListener(), token)
    stream.performs()
