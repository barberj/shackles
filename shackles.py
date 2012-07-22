def broken(obj, chain):
    """Return name of attribute where the chain
    is broken.

    If chain is not broken (all attributes are represented in chain)
    nothing is returned."""

    if isinstance(chain, (str, unicode)):
        chain = chain.split('.')

    if isinstance(chain, (list, tuple)):
        for attr in chain:
            obj = getattr(obj, attr, None)
            if not obj:
                return attr

def getattr(obj, chain, default=None):
    """Recursively walk chain. Return the value
    of the final named attribute in the chain.

    If a named attribute does not exist,
    default is returned if provided, otherwise AttributeError is raised.

    Replaces doing things like:
    object.attr1.attr2.attr3 if object and object.attr1.attr2 else None

    or

    getattr(getattr(getattr(object, 'attr1', None), 'attr2', None), 'attr3', None)
    """

    if isinstance(chain, (str, unicode)):
        chain = chain.split('.')

    if isinstance(chain, (list, tuple)):
        for attr in chain:
            obj = getattr(obj, attr, None)
            if not obj:
                break
    return obj

def walk(obj, chain):
    pass
