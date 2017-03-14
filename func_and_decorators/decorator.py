import functools


def escape_unicode(f):
    @functools.wraps(f)
    def wrap(*args, **kwargs):
        x = f(*args, *kwargs)
        return ascii(x)
    return wrap


def polish_city(city):
    """
    Returns a greeting.
    """
    return "Cześć {city}".format(city=city)

polish_city = escape_unicode(polish_city)
print(polish_city("Poznań"))

print(polish_city.__name__)
print(polish_city.__doc__)
