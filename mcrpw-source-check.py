#!/usr/bin/env python3
from re import compile as regexp
from pathlib import Path
from glob import glob

SOURCE_FILE_LINE_REGEX = regexp(r'^([\w+\.\_]+) *= *(.*)$')
PROJECT_FILES = Path('./project_files')
RED, YELLOW, GREEN, RESET = '\033[31m', '\033[33m', '\033[32m', '\033[0m'

def resolve_asset(name: str):
    parts = name.split('.')
    root, modname, asset_type, *folders, name = parts
    path = PROJECT_FILES / root / modname / asset_type
    for folder in folders:
        path /= folder
    try:
        return next(path.glob(f'{name}.*'))
    except:
        return None

with open('sources_files.cfg', 'r') as src_file:
    available, unavailable = [], []
    for line in src_file:
        name, source = SOURCE_FILE_LINE_REGEX.findall(line.strip())[0]
        asset = resolve_asset(name)
        if asset:
            print(f'[{GREEN} OK {RESET}] {name}')
            available.append((name, source))
        elif source == '*silence*':
            print(f'[{YELLOW}IGNR{RESET}] {name}')
            available.append((name, source))
        else:
            print(f'[{RED}FAIL{RESET}] {name}')
            unavailable.append((name, source))
            
    print()
    print(f'Assets found: {len(available)}/{len(available) + len(unavailable)}')
    print()
    if unavailable:
        print(f'{RED}Failed to find {len(unavailable)} assets:{RESET}')
        for (name, source) in unavailable:
            print(f'{name} from {source}')
        exit(1)
