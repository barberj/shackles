Shackles
========

.. image:: https://secure.travis-ci.org/barberj/shackles.png?branch=develop

Access and inspect attributes shackled to an object.

Shackles is ISC `LICENSED <https://github.com/barberj/shackles/blob/master/LICENSED.rst>`_.

Installation
------------

To install shackles, simply: ::

    $ pip install shackles


API Documentation
-----------------

shackles.broken(obj, chain)
    Return name of first missing named attribute of object.

    If chain is not broken (all attributes are represented in chain)
    nothing is returned.

::

    # obj.a.b.e
    assert shackles.broken(obj, 'a.b.c') == 'c'

shackles.get(obj, chain[, default])
    Return value of final named attribute in chain of object.

    If a final named attribute does not exist,
    default is returned if provided, otherwise *AttributeError* is raised.

::

    # obj.a.b
    assert shackles.get(obj, 'a.b.c', 5) == 5

    # obj.a.b.c = 6
    assert shackles.get(obj, 'a.b.c', 5) == 6

shackles.has(obj, chain)
    Return *True* if the chain of attributes exists on the object, *False* if not.

::

    # obj.a.b.c
    assert shackles.has(obj, 'a.b.c']) == True

shackles.walk(obj, chain)
    Generate the values of the attributes in the chain by walking the named attributes in the chain from the object.

    If a named attribute does not exist, *AttributeError* is raised.

::

    # a = obj; b = obj; c = obj
    # a.name = 'a'; b.name = 'b'; c.name = 'c'
    # a.b = b; b.c = c
    assert next(shackles.walk(a, 'b.c')).name == 'b'

shackles.attrgetter(chain[, default])
    Return a callable object that fetches the final named attribute from its operand. The returned callable object is equivalent to shackles.get with the chain and default parameters arleady defined.

    If the final named attribute does not exist,
    default is returned if provided, otherwise *AttributeError* is raised.

::

    # obj.a.b = 5
    # obj2.a.b
    agetter = shackles.attrgetter('a.b.c', 6)
    assert agetter(obj) == 5
    assert agetter(obj2) == 6

**For further examples refer to included tests.**


Contribute
----------

#. Fork `the repository <https://github.com/barberj/shackles>`_ on Github to start making your changes to the **develop** branch (or branch off of it).
#. Install to your env or venv by running: ::

    $ python setup.py develop

#. Write a test which shows that the bug was fixed or that the feature works as expected.
#. Send a pull request and bug the maintainer until it gets merged and published. :) Make sure to add yourself to `AUTHORS <https://github.com/barberj/shackles/blob/master/AUTHORS.rst>`_.
