import sys

PY2 = sys.version_info[0] == 2
VER = sys.version_info

if not PY2:
    text_type = str
    string_types = (str,)
    integer_types = (int, )

    iterkeys = lambda d: iter(d.keys())
    itervalues = lambda d: iter(d.values())
    iteritems = lambda d: iter(d.items())

    def as_unicode(s):
        if isinstance(s, bytes):
            return s.decode('utf-8')

        return str(s)

    # Various tools
    from functools import reduce
    from urllib.parse import urljoin, urlparse
else:
    text_type = unicode
    string_types = (str, unicode)
    integer_types = (int, long)

    iterkeys = lambda d: d.iterkeys()
    itervalues = lambda d: d.itervalues()
    iteritems = lambda d: d.iteritems()

    def as_unicode(s):
        if isinstance(s, str):
            return s.decode('utf-8')

        return unicode(s)

    # Helpers
    reduce = __builtins__['reduce'] if isinstance(__builtins__, dict) else __builtins__.reduce
    from urlparse import urljoin, urlparse
