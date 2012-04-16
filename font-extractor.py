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
    stringsfile, inputfile, outputfile = sys.argv[1:]
    suffix = '.ttf'
    if outputfile.endswith(suffix):
        fontName = outputfile[:-len(suffix)]
    else:
        fontName = outputfile
        outputfile = outputfile + suffix

    tmpDir = '/var/tmp/font-extractor/'
    os.system('mkdir -p %s' % tmpDir)

    # generate charsfile
    tmpCharsfile = tmpDir + 'tmp.charsfile'
    cmdExtractStrings = '''
    ./unique-chars-extractor.py %(inputfile)s %(outputfile)s
    ''' % {
        'inputfile' : stringsfile,
        'outputfile' : tmpCharsfile
        }
    run(cmdExtractStrings)

    # generate a subset of font
    tmpTtf = tmpDir + 'tmp.ttf'
    cmdSubset = '''
    cd font-optimizer
    ./subset.pl --charsfile=%(charsfile)s %(inputfile)s %(outputfile)s
    ''' % {
        'charsfile' : tmpCharsfile,
        'inputfile' : inputfile,
        'outputfile': tmpTtf
        }
    run(cmdSubset)
    
    cmdModifyNames = '''
    cd font-optimizer
    ./modify-names.pl --set family %(fontName)s %(inputfile)s %(outputfile)s
     mv %(outputfile)s ..
    ''' % {
        'fontName' : fontName,
        'inputfile' : tmpTtf,
        'outputfile' : outputfile
        }
    run(cmdModifyNames)
    
