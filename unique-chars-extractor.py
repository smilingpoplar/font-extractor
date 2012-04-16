#!/usr/bin/python
# author: YangLe 201204

import codecs
import sys
import re

def extractValuesFromStringsText(text):
    def removeComments(text):
        # remove /* xxx */
        text = re.sub(r'(?s)/\*.*?\*/', '', text)
        # remove // xxx
        text = re.sub(r'//.*', '', text)
        return text
    
    def extractValueFromLine(line):
        if not line.strip():
            return ''
        kv = line.split('=')
        if len(kv) != 2:
            print 'skip line: %s' % line
            return ''

        value = kv[1]
        value = value.strip(' \t;')
        # remove heading & tailing quote
        if value[0] == '"' and value[-1] == '"':
            value = value[1:-1]
        # unescape "
        value = re.sub(r'\\"', '"', value)
        return value
    
    text = removeComments(text)
    lines = [extractValueFromLine(line) for line in text.splitlines()]
    text = ''.join(lines)
    return text

def uniqueCharsFromText(text):
    charSet = set()
    for char in text:
        charSet.add(char)
    return ''.join(charSet)

def uniqueCharsFromStringsText(text):
    text = extractValuesFromStringsText(text)
    text = uniqueCharsFromText(text)
    return text

def doSthWithFile(inputfile, block, outputfile):
    with open(inputfile) as f:
        text = f.read()
    # convert plain Python string to Unicode: "decode"
    text = unicode(text, 'utf-8')

    # do something
    text = block(text)

    # convert Unicode to plain Python string: "encode"
    text = text.encode("utf-8")
    print text
    with open(outputfile, 'w') as f:
        f.write(text)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print 'usage: ./unique-chars-extractor.py inputfile outputfile'
        exit(-1)
    inputfile, outputfile = sys.argv[1:]
    suffix = '.strings'
    if inputfile.endswith(suffix):
        doSthWithFile(inputfile, uniqueCharsFromStringsText, outputfile)
    else:
        doSthWithFile(inputfile, uniqueCharsFromText, outputfile)

    
