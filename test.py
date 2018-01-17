from accern import HistoricalClient

# token = '3d6aad5b2ad363f0236faaf779cf0f499d25f309b8bc0199a677129c'
token = 'f72fd5db6eb16da7764e243051df0f08edb9c116d5310ecce5a06964'
Client = HistoricalClient(token)

schema = {
    "name": "Hourly data",
    "description": "Hourly data request",
    "filters": [
        {
            "entity_ticker": [
                "AAPL"
            ],
            "harvested_at": [
                ["2017-11-29 00:00:00", "2017-11-30 00:00:00"]
            ],
            "entity_sentiment": [
                [70, 100]
            ]
        }
    ],
    'select': [
        {
            'field': 'author_id',
            'function': 'group'
        },
        {
            'field': 'entity_sentiment',
            'function': 'average'
        },
        {
            'field': 'entity_ticker',
            'function': 'group'
        },
        {
            'field': 'harvested_at',
            'function': 'hour',
            'alias': 'hour'
        }
    ]
}

resp = Client.create_job(schema)

print resp
