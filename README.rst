xp
==

Apply XPath expressions to XML, like ``jq`` does for JSON.


Usage
-----

Extract download URLs from an RSS feed::

    http get 'http://br-rss.jeffbr13.net/rss/channels/1/' | python -m xp '//item/enclosure/@url'


Extract all links from an HTML page footer::

    http get 'http://br-rss.jeffbr13.net/ | python -m xp '//footer//a/@href'



Distribute
----------

Increment the ``xp.VERSION`` version number and run the following two commands
to create a `source distribution <https://packaging.python.org/tutorials/distributing-packages/#source-distributions>`_,
create a `universal wheel <https://packaging.python.org/tutorials/distributing-packages/#universal-wheels>`_,
and `upload to PyPI <https://packaging.python.org/tutorials/distributing-packages/#upload-your-distributions>`_ ::

    python setup.py sdist
    python setup.py bdist_wheel --universal
    twine upload dist/*
