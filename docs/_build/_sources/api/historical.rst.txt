.. _historical:

#######################
Historical Data Request
#######################

Accern Historical Batch data request is available for user who has the permission
to create a job(data request). The data can be downloaded when the job request is
finished.

Create Historical Instance
--------------------------

Create an Historical instance

.. code-block:: python

    from accern import HistoricalClient
    token = 'YOUR TOKEN'
    Client = HistoricalClient(token)

Set up a job
------------

``name``, ``description``, ``filters`` and ``select`` are required field to
create a job schema. For more detail of how to work with ``filters`` and
``select``, please refer to the :ref:`Schema<Schema Class>`.

.. code-block:: python

    schema = {
        'name': 'test',
        'description': 'request 2017 November data',
        'filters': [
            {
                'harvested_at': [
                    ['2017-11-01 00:00:00', '2017-11-30 23:59:59']
                ],
                'entity_sentiment': [
                    [-100, 50]
                ]
            }
        ],
        'select': [
            {'field': 'entity_sentiment'},
            {'field': 'entity_ticker'},
            {'field': 'event'},
            {'field': 'harvested_at'}
        ]
    }

Check your job history
----------------------

.. code-block:: python

    resp = Client.get_jobs()

If you pass a job id to the ``get_jobs`` function, you will get the information
of that job.

.. code-block:: python

    job_id = 'YOUR JOB ID'
    resp = Client.get_jobs(job_id)

Select and Aggregations
-------------------------

You can add ``minute``, ``hour``, ``day``, ``week``, or ``month``
aggregation function to the field ``harvested_at``. The ``alias`` field should
match the function name you choose.

.. code-block:: python

    schema = {
        'name': 'Month',
        'description': 'Month Sentiment data',
        'select': [
            {
                'field': 'harvested_at',
                'alias': 'month',
                'function': 'month'
            }
        ]
    }

The aggregation function will group signals based on the time interval you choose.
If your data will contain other fields, an aggregation function should be given.
Otherwise, an API error will occur.

.. code-block:: python

    schema = {
        'name': 'Month',
        'description': 'Month Sentiment data',
        'filters': [
            {
                'harvested_at': [
                    ['2012-08-01 00:00:00', '2017-11-30 00:00:00']
                ],
                'entity_sentiment': [
                    [-100, 50]
                ],
                'entity_ticker': [
                    'AAPL',
                    'AMZN'
                ]
            }
        ],
        'select': [
            {
                'field': 'entity_sentiment',
                'function': 'sum'
            },
            {
                'field': 'entity_ticker',
                'function': 'group'
            },
            {
                'field': 'harvested_at',
                'alias': 'month',
                'function': 'month'
            }
        ]
    }


A full list of the available aggregation functions can be found at :ref:`Aggregation function<Field Aggregate Function>`
