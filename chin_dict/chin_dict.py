# TODO can see traditional/simplified form

from .chindict import ChinDict 
import argparse

__version__ = "0.1.2"

parser = argparse.ArgumentParser(description='Lookup character or word')
parser.add_argument('character', type=str, help='Character to search')
group = parser.add_mutually_exclusive_group()
group.add_argument('-w', '--word', action='store_true', help='lookup word')
group.add_argument('-t', '--tree', action='store_true', help='show tree')
group.add_argument('-c', '--comp', action='store_true', help='show components')
group.add_argument('-cm', '--compmean', action='store_true', help='show component meanings')
group.add_argument('-cr', '--comprad', action='store_true', help='show component radicals')
group.add_argument('-r', '--rad', action='store_true', help='show components')

args = parser.parse_args()


def main():
        
    hd = ChinDict(charset='simplified')

    if args.word:
        res = hd.lookup_word(args.character)
        print("-----------------------------")
        for word in res:
            print(word)
    else:
        res = hd.lookup_char(args.character)
        print("-----------------------------")

        if args.tree:
            res.tree()
        elif args.comp:
            try:
                print(res.components)
            except AttributeError:
                print(res.character + " has no components.")
        elif args.rad:
            try: 
                print(res.radical)
            except AttributeError:
                print(res.character + " has no radical.")
        elif args.compmean:
            try:
                for comp in res.components:
                    print(comp.character + " meaning(s):")
                    print(comp.meaning)
                    print()
            except AttributeError:
                print(res.character + " has no components.")
        elif args.comprad:
            try:
                for comp in res.components:
                    print(comp.character + " radical:")
                    try:
                        print(comp.radical)
                    except AttributeError:
                        print(comp.character + " has no radical")
                    print()
            except AttributeError:
                print(res.character + " has no components.")
        else:
            print("Character:", res.character)
            print("Pinyin:", res.pinyin)
            print("Meaning:", res.meaning)
