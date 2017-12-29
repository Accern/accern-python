.. _schema:

####################
Schema Class/ Object
####################

Accern Python Library allows user to filter and select Accern data in 3 different
ways: REST API, streaming and historical data request. ``schema`` object is used
in these three methods to convey user's idea of how to slice data.

``Schema`` class here will provide some help functions and validate functions to
help user build a right one.

Get Fields
==========
Get available fields in the data.

.. code-block:: python

    from accern import Schema
    print Schema.get_fields()


Get field options
=================
For field type and available options.

.. code-block:: python

    Schema.get_options('event_group')


Build your schema
=================

.. code-block:: python

    schema = {
        'select': [
            {
                'field': 'entity_ticker',
                'alias': 'ticker'
            }
        ],
        'filters': {
            'entity_sentiment': [
                [70, 100],
                [-100, -70]
            ]
        }
    }

Validate schema
===============
After drafting a schema, validate it along with the method you want to use.

.. code-block:: python

    Schema.validate_schema(method='api', schema=schema)


Select and add alias
====================

To select only a few fields or rename the fields, pass the alias of the fields
you want to ``schema``.

.. code-block:: python

    schema = {
        'select': [
            {
                'field': 'entity_ticker',
                'alias': 'ticker'
            }
        ]
    }

    response = Client.request(schema)

The alias for the selected fields is optional and you can select multiple fields.

.. code-block:: python

    schema = {
        'select': [
            {
                'field': 'entity_ticker',
                'alias': 'ticker'
            }, {
                'field': 'harvested_at'
            }
        ]
    }

    response = Client.request(schema)

If you want to filter the data, here is a list of available fields to filter by:

.. include:: ../data/table_filter.rst
    :start-after: .. snip
    :end-before: .. snap

For the full list and available values, you can use the helper function menthioned above.


Pass the filters to ``schema``. The value can be a single value or an array of
values.

.. code-block:: python

    schema = {
        'filters': {
            'entity_industry': ['Apparel', 'Food Chains'],
            'event': 'Accident'
        }
    }

    response = Client.request(schema)

A list of filter examples is available at :ref:`Cookbook<Field Filter Cookbook>`
