import json
import functools
import os
import sys
import tempfile
from argparse import ArgumentParser


def to_json(func):
    @functools.wraps(func)
    def wrapped(*args, **kwargs):

        return json.dumps(func(*args, **kwargs))
    return wrapped


@to_json
def get_data():
    return {
        'data': 42
    }


get_data()  # вернёт '{"data": 42}'
