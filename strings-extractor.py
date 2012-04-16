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
    
    with open(stringsfile) as f:
        text = f.read()
    # convert plain Python string to Unicode: "decode"
    text = unicode(text, 'utf-8')
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
    chars = ''.join(charSet)
    # convert Unicode to plain Python string: "encode"
    chars = chars.encode("utf-8")
    return chars


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print 'usage: ./string-extractor.py [stringsfile.strings] [charsfile.unique]'
        exit(-1)
    stringsfile, charsfile = sys.argv[1:]
    chars = extractChars(stringsfile)
    print chars

    with open(charsfile, 'w') as f:
        f.write(chars)

    
