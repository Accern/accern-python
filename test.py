from accern import API
TOKEN = '1c5da36c654b5f1252bdac1cf7924664'
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
        ],
        'harvested_at': ['2017-12-01 00:00:00', '2017-12-07 00:00:00']
    }
}

resp = Client.request(schema)
print resp
