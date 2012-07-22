def broken(object, attr_chain):
    """Return name of attribute where the chain
    is broken.

    If chain is unbroken nothing is returned."""

    if isinstance(attr_chain, (str, unicode)):
        attr_chain = attr_chain.split('.')

    if isinstance(attr_chain, (list, tuple)):
        for attr in attr_chain:
            object = getattr(object, attr, None)
            if not object:
                return attr

def value(object, attr_chain):
    """Recursively gets attributes in chain.
    If at any point in the chain a link is missing
    None is returned.

    Replaces doing things like:
    object.attr1.attr2.attr3 if object and object.attr1.attr2 else None

    or

    getattr(getattr(getattr(object, 'attr1', None), 'attr2', None), 'attr3', None)
    """

    if isinstance(attr_chain, (str, unicode)):
        attr_chain = attr_chain.split('.')

    if isinstance(attr_chain, (list, tuple)):
        for attr in attr_chain:
            object = getattr(object, attr, None)
            if not object:
                break
    return object
