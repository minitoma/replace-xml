#!/usr/bin/python
# Created by CALATAYUD Thomas -- 2018
import sys
import argparse
import xml.etree.ElementTree as ET

parser = argparse.ArgumentParser(description="Parse xml files and replace a text from a specific tag")
parser.add_argument('files', metavar='F', nargs='+', help='xml file(s) to modify')
parser.add_argument('-t', nargs=1, type=str, required=True, help='tag to search ; for exemple : trends or history')
parser.add_argument('-r', nargs=1, required=True, type=str, help='text to replace ; this text would be between the tag T')
args = parser.parse_args()
print('List of xml files to modify : '+ str(args.files))
print('Tag to modifiy in those files : '+ args.t[0])
print('Substitute text : '+ args.r[0])
print('-----')
for filename in args.files:
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        print('Modifying '+filename)
        for tag in root.iter(args.t[0]):
            tag.text = str(args.r[0])
        tree.write(filename)
    except:
        print("** ERROR !!! **")
        print(filename+" is not a valid xml file")
