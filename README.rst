xp
==

Apply XPath expressions to XML, like ``jq`` does for JSON.


Usage
-----

Extract download URLs from an RSS feed::

    http get 'http://br-rss.jeffbr13.net/rss/channels/1/' | python -m xp '//item/enclosure/@url'
