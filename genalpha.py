#!/usr/bin/env python
from sys import exit, argv
from json import loads as parse

def _alpha_sorted(m1, m2):
    return cmp(m1["title"], m2["title"])

def generate_markdown(monsters):
    print "\n# All Monsters Alphabetically\n"
    for monster in sorted(monsters, cmp=_alpha_sorted):
        print " - {title} ({page})".format(**monster)

def read_source(filePath):
    with open(filePath, "r") as sourceFile:
        return parse(sourceFile.read())
    return []

def main(proggy, sourceFile="source.json", *args):
    generate_markdown(read_source(sourceFile))
    return 0

if __name__=="__main__":
    exit(main(*argv))
