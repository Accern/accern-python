########
Appendix
########

Field Filter Cookbook
=====================

Here is a cookbook of how to filter fields by using our REST API.

.. code-block:: python

    from accern import API

    TOKEN = 'YOUR TOKEN'
    Client = API()
    Client.token = TOKEN


Filter by single event.

.. code-block:: python

    schema = {
        'filters': {
            'event': 'Analyst Ratings'
        }
    }

    resp = Client.request(schema)

Filter by a list of events.

.. code-block:: python

    schema = {
        'filters': {
            'event': ['Analyst Ratings', 'Corporate Actions']
        }
    }

Get only ``entity_type = US_EQUITY``.

.. code-block:: python

    schema = {
        'filters': {
            'entity_type': 'US_EQUITY'
        }
    }

Get only ``story_type = news``.

.. code-block:: python

    schema = {
        'filters': {
            'story_type': 'news'
        }
    }


Get articles with low ``story_group_exposure``.

.. code-block:: python

    schema = {
        'filters': {
            'story_group_exposure': 'low'
        }
    }

You can provide multiple fields in the filter (they will be AND'd).

.. code-block:: python

    schema = {
        'filters': {
            'event': ['Analyst Ratings', 'Corporate Actions'],
            'story_group_exposure': 'low',
            'story_type': 'news'
        }
    }

Field Value List
================


entity_sector
-------------

entity_industry
---------------

.. include:: ../data/table_sector_industry.rst
    :start-after: .. snip
    :end-before: .. snap

event
-----

event_group
-----------

.. include:: ../data/table_event_group.rst
    :start-after: .. snip
    :end-before: .. snap


story_type
----------

+------------+
| blog       |
+------------+
| feed       |
+------------+
| news       |
+------------+
| sec_filing |
+------------+
