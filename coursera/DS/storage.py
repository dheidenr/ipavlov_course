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
    parser.add_argument('--key', type=str)
    parser.add_argument('--val', type=str)
    args = parser.parse_args()
    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

    if args.key and args.val:
        key = args.key
        value = args.val
        if os.path.isfile(storage_path):
            with open(storage_path, 'r') as file:
                file.read()
                if file.tell() == 0:
                    _dict = {}
                else:
                    file.seek(0)
                    _dict = dict(json.load(file))
        else:
            _dict = {}
        with open(storage_path, 'w') as file:
            _dict.setdefault(key, [])
            _dict[key].append(value)
            json.dump(_dict, file)
    elif args.key:
        key = args.key
        if os.path.isfile(storage_path):
            with open(storage_path, 'r') as file:
                file.read()
                if file.tell() == 0:
                    _dict = {}
                    print(_dict.get(key))
                else:
                    file.seek(0)
                    _dict = dict(json.load(file))
                    if key in _dict:
                        print(', '.join(_dict.get(key)))
                    else:
                        print('None')
        else:
            _dict = {}
            print(_dict.get(key))
