#!/usr/bin/env python3
from zipfile import ZipFile
from pathlib import Path
from sys import argv
from os import walk
from json import dumps

if len(argv) < 3:
    print("Usage: {} [project root] [output.zip]".format(argv[0]))
    exit(2)

project_root = Path(argv[1])
project_files = project_root / "project_files"
extras_directory = project_root / "extra_files"
custom_sounds = project_root / "custom_sounds"
custom_languages = project_root / "custom_languages"

def add_file(zipf, path_from, path_to):
    zipf.write(path_from, path_to)
    print(" + {}".format(path_to))

def add_tree(zipf, path_from, path_to=""):
    for (dpath, _, fnames) in walk(path_from):
        for fname in fnames:
            realpath = Path(dpath, fname)
            relpath = realpath.relative_to(path_from)
            add_file(zipf, realpath, Path(path_to, relpath))

with ZipFile(argv[2], "w") as zipf:
    add_tree(zipf, custom_sounds, "assets/minecraft/sounds")
    add_tree(zipf, custom_languages, "assets/minecraft/lang")
    if (project_root / 'sounds.release.json'):
        add_file(zipf, project_root / "sounds.release.json", "assets/minecraft/sounds.json")
    else:
        add_file(zipf, project_root / "sounds.json", "assets/minecraft/sounds.json")
    zipf.writestr("pack.mcmeta", dumps({
        "pack": {
            "description": argv[2] if len(argv) >= 4 else '',
            "pack_format": 7,
        }
    }, indent=2))
    add_tree(zipf, project_files)
    add_tree(zipf, extras_directory)
    add_file(zipf, project_root / "pack.png", "pack.png")
