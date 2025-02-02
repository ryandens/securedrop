import secrets
import string
from datetime import datetime


def random_bool():
    return bool(secrets.randbits(1))


def bool_or_none():
    return secrets.choice([None, True, False])


def random_bytes(min, max, nullable):
    if nullable and random_bool():
        return None
    else:
        # python2 just wants strings, fix this in python3
        return random_chars(secrets.SystemRandom().randint(min, max))


def random_name():
    len = secrets.SystemRandom().randint(1, 100)
    return random_chars(len)


def random_username():
    len = secrets.SystemRandom().randint(3, 64)
    return random_chars(len)


def random_chars(len, chars=string.printable):
    return "".join([secrets.choice(chars) for _ in range(len)])


def random_ascii_chars(len, chars=string.ascii_lowercase):
    return "".join([secrets.choice(chars) for _ in range(len)])


def random_datetime(nullable):
    if nullable and random_bool():
        return None
    else:
        return datetime(
            year=secrets.SystemRandom().randint(1, 9999),
            month=secrets.SystemRandom().randint(1, 12),
            day=secrets.SystemRandom().randint(1, 28),
            hour=secrets.SystemRandom().randint(0, 23),
            minute=secrets.SystemRandom().randint(0, 59),
            second=secrets.SystemRandom().randint(0, 59),
            microsecond=secrets.SystemRandom().randint(0, 1000),
        )
