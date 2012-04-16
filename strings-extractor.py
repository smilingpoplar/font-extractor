#!/usr/bin/python
# author: YangLe 201204

import codecs
import sys
import re

def extractChars(stringsfile):
    def removeComments(text):
        # remove /* xxx */
        text = re.sub(r'(?s)/\*.*?\*/', '', text)
        # remove // xxx
        text = re.sub(r'//.*', '', text)
        return text
    
    def extractValue(s):
        value = s.strip(' \t;')
        # remove heading & tailing quote
        if value[0] == '"' and value[-1] == '"':
            value = value[1:-1]
        # unescape
        value = re.sub(r'\\"', '"', value)
        return value
    
    with codecs.open(stringsfile, 'r', 'utf-8') as f:
        text = f.read()
    text = removeComments(text)
    charSet = set()
    lines = [line for line in text.splitlines() if line.strip() ]
    for line in lines:
        kv = line.split('=')
        if len(kv) != 2:
            print 'skip line: %s' % line
            continue
        for char in extractValue(kv[1]):
            charSet.add(char)        
    return ''.join(charSet)


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print 'usage: ./string-extractor.py [stringsfile] [charsfile.unique]'
        exit(-1)
    stringsfile = sys.argv[1]
    chars = extractChars(stringsfile)
    print chars
    charsfile = sys.argv[2]
    with codecs.open(charsfile, 'w', 'utf-8') as f:
        f.write(chars)

    
