GFM
===

GFM is a small module to convert `GitHub Flavored Markdown`_ to HTML.

Usage
-----

GFM offers two methods, ``gfm`` and ``markdown``.

``gfm`` simply preprocesses the parts of Markdown that GitHub Flavored
Markdown is interested in, without converting the Markdown to HTML.

``markdown`` does this as well as passing the result through the
``markdown`` module to generate HTML.

::

    >>> import gfm
    >>> string = "Roses are red\nViolets are blue"
    >>> gfm.gfm(string)
    'Roses are red  \nViolets are blue'
    >>> gfm.markdown(string)
    '<p>Roses are red<br />\nViolets are blue</p>'

Installation
------------

::

    pip install gfm

License
-------

MIT, plain and simple.

.. _GitHub Flavored Markdown: https://help.github.com/articles/github-flavored-markdown
