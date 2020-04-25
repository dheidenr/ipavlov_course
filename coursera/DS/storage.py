import json
import os
import sys
import tempfile
from argparse import ArgumentParser


if __name__ == "__main__":
    parser = ArgumentParser()
    _dict = {}
    key = None
    value = None

    if len(sys.argv) == 5:
        parser.add_argument('--key', type=str)
        parser.add_argument('--val', type=str)
        args = parser.parse_args()
        key = args.key
        value = args.val
        storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
        if os.path.isfile(storage_path):
            with open(storage_path, 'r') as file:
                _dict = dict(json.load(file))
        else:
            print(None)
        with open(storage_path, 'w') as file:
            _dict.setdefault(key, [])
            _dict[key].append(value)
            json.dump(_dict, file)
    if len(sys.argv) == 3:
        parser.add_argument('--key', type=str)
        args = parser.parse_args()
        key = args.key
        storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
        if os.path.isfile(storage_path):
            with open(storage_path, 'r') as file:
                _dict = dict(json.load(file))
                if key in _dict:
                    print(', '.join(_dict[key]))
        else:
            print(None)
