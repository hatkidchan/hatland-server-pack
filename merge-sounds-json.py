#!/usr/bin/env python3
from json import load, dump

with open('sounds.json', 'r') as s1:
    with open('sounds_extra.json', 'r') as s2:
        with open('sounds.release.json', 'w') as jo:
            j1 = load(s1)
            j1.update(load(s2))
            dump(j1, jo, indent=4)
            print(" + Merged {} sounds".format(len(j1)))
