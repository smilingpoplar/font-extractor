# Font-Extractor for iPhone Apps

A script to:

1. extract unique chars from *Localizable.strings* or any text file
2. extract a *font subset* using *[font-optimizer][1]* 
3. set its *font family* as the *outputfile* name

### Usage:
    ./font-extractor.py [stringsfile|textfile] [inputfile.ttf] [outputfile.ttf]

Then you can [add the custom font][2] to your app

XXX: If you use xcode for editing, verify the .strings content in *Source Code* mode (find the file in Project Navigator: Right Click->Open As->Source Code).

[1]: https://bitbucket.org/philip/font-optimizer/src/
[2]: http://stackoverflow.com/a/2616101/1263403




