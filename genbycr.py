#!/usr/bin/env python
from sys import exit, argv
from json import loads as parse

crxp = {
    "0": "(0-10XP)",
    "1/8": "(25XP)",
    "1/4": "(50XP)",
    "1/2": "(100XP)",
    "1": "(200XP)",
    "2": "(450XP)",
    "3": "(700XP)",
    "4": "(1100XP)",
    "5": "(1800XP)",
    "6": "(2300XP)",
    "7": "(2900XP)",
    "8": "(3900XP)",
    "9": "(5000XP)",
    "10": "(5900XP)",
    "11": "(7200XP)",
    "12": "(8400XP)",
    "13": "(10000XP)",
    "14": "(11500XP)",
    "15": "(13000XP)",
    "16": "(15000XP)",
    "17": "(18000XP)",
    "18": "(20000XP)",
    "19": "(22000XP)",
    "20": "(25000XP)",
    "21": "(33000XP)",
    "22": "(41000XP)",
    "23": "(50000XP)",
    "24": "(62000XP)",
    "26": "(90000XP)",
    "30": "(155000XP)",
}

def generate_markdown(monsters):
    currentCR=-1
    for monster in sorted(monsters, key=lambda d: eval(d["cr"])):
        monster['title']=monster['title'].encode('utf-8')
        if currentCR != monster["cr"]:
            print "\n# Challenge Rating {cr} {0}\n".format(crxp[monster["cr"]], **monster)
        currentCR = monster["cr"]
        print " - {title} ({book} {page})".format(**monster)

def read_source(filePath):
    with open(filePath, "r") as sourceFile:
        return parse(sourceFile.read())
    return []

def main(proggy, sourceFile="source.json", *args):
    generate_markdown(read_source(sourceFile))
    return 0

if __name__=="__main__":
    exit(main(*argv))
