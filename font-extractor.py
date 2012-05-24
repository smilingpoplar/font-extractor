#!/usr/bin/python
# author: YangLe 201204

import sys
import os

def run(cmd):
    print cmd
    os.system(cmd)

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print 'usage: ./font-extractor.py [stringsfile|textfile] [inputfile.ttf] [outputfile.ttf]]'
        exit(-1)
    stringsFile, inputFile, outputFile = sys.argv[1:]
    suffix = '.ttf'
    fontName = os.path.basename(outputFile)
    if fontName.endswith(suffix):
        fontName = fontName[:-len(suffix)]
    else:
        outputFile = outputFile + suffix

    currentDir = os.path.dirname(os.path.realpath(sys.argv[0]))
    if not os.path.dirname(outputFile):
        outputFile = os.path.join(os.getcwd(), outputFile)

    tmpDir = '/var/tmp/font-extractor/'
    os.system('mkdir -p %s' % tmpDir)

    # generate charsfile
    tmpCharsFile = tmpDir + 'tmp.charsfile'
    cmdExtractStrings = '''
    %(currentDir)s/unique-chars-extractor.py %(inputFile)s %(outputFile)s
    ''' % {
        'currentDir' : currentDir,
        'inputFile' : stringsFile,
        'outputFile' : tmpCharsFile
        }
    run(cmdExtractStrings)

    # generate a subset of font
    tmpTtf = tmpDir + 'tmp.ttf'
    cmdSubset = '''
    (cd %(currentDir)s/font-optimizer &&
    ./subset.pl --charsfile=%(charsFile)s %(inputFile)s %(outputFile)s)
    ''' % {
        'currentDir' : currentDir,
        'charsFile' : tmpCharsFile,
        'inputFile' : inputFile,
        'outputFile': tmpTtf
        }
    run(cmdSubset)
    
    cmdModifyNames = '''
    (cd %(currentDir)s/font-optimizer &&
    ./modify-names.pl --set family %(fontName)s %(inputFile)s %(outputFile)s)
    ''' % {
        'currentDir' : currentDir,
        'fontName' : fontName,
        'inputFile' : tmpTtf,
        'outputFile' : outputFile
        }
    run(cmdModifyNames)
    
