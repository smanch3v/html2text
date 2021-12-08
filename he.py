from __future__ import division, unicode_literals
from bs4 import BeautifulSoup
from os import O_SEQUENTIAL, listdir
from os.path import isfile, join
from pathlib import Path


def get_plain_text(filename):
    f = open(filename, "r")
    document = BeautifulSoup(f.read()).get_text()
    return document


mypath = "C:\Code\he\doc_test\\"
files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
for filename in files:
    print(mypath + filename)
    text = get_plain_text(mypath + filename)
    with open("doc_test/" + filename + ".txt", "w") as f:
        f.write(text)
