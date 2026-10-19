#!/usr/bin/env python3
"""Listet MGD-Aufrufe oder erzeugt einen kopierfertigen Prompt, ohne Ausführung."""
import argparse
import sys
sys.dont_write_bytecode = True
from command_catalog import DEFAULTS,load_catalog,render_prompt,resolve


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action',choices=['list','show'])
    parser.add_argument('command',nargs='?')
    for key in DEFAULTS:parser.add_argument('--'+key)
    args=parser.parse_args()
    try:
        if args.action=='list':
            for item in load_catalog()['commands']:
                print('/'+item['command']+'  →  $'+item['skill']+'  ·  '+item['title'])
        else:
            if not args.command:parser.error('show braucht einen Aufruf, z. B. /MGD-Reel')
            values={key:getattr(args,key) for key in DEFAULTS if getattr(args,key) is not None}
            print(render_prompt(resolve(args.command),values))
    except (ValueError,OSError) as error:parser.exit(1,str(error)+'\n')

if __name__=='__main__':main()
