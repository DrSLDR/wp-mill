#!/usr/bin/python3

# wp-mill
# Copyright (c) 2015 Jonas A. Hultén
# Usage regulated by the MIT license (see LICENSE file)

import os, sys

if not len(sys.argv) == 2:
    print("Full path to xml-file needed")
    exit(1)

grouping = 10

cdir = os.path.dirname(os.path.realpath(__file__))
xmlfilepath = os.path.realpath(sys.argv[1])

print("Opening source file")
xmlfile = open(xmlfilepath,'r')

print("Processing header data")
header = ""
while True:
    l = xmlfile.readline()
    if not "<item>" in l:
        header += l
    else:
        break

pos = xmlfile.tell() - len(l)
print("Position of first item is at " + str(pos))

print("Skipping to footer")
while True:
    l = xmlfile.readline()
    if not "</channel>" in l:
        continue
    else:
        break

print("Got footer at position " + str(xmlfile.tell() - len(l)))
print("Processing footer data")
footer = ""
while l is not "":
    footer += l
    l = xmlfile.readline()

print("Reversing and exporting items in groups of " + str(grouping))
xmlfile.seek(pos)
fnum = 0
inum = 0
while True:
    fname = str(fnum).zfill(4) + ".xml"
    print("Creating " + fname)
    f = open(cdir + "/" + fname,'w')
    fnum += 1
    f.write(header)
    buf = ""
    i = 0
    while i < grouping:
        l = xmlfile.readline()
        if "<item>" in l:
            i += 1
                        inum += 1
            print("Writing item " + str(i))
            buf += l
            while True:
                l = xmlfile.readline()
                buf += l
                if "</item>" in l:
                    break
        else:
            break
    f.write(buf)
    f.write(footer)
    if i < grouping:
        print("End of all items") 
                print("got total of " + str(inum) + " items in " + str(fnum) + " files")
        break
