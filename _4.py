import re
import string

#------------------------------------------------------------------------------------
                                                                                    # searching in text from the file for mathes
def searching(text):
    #text = text.lower
    for i in range(len(text)):
        result = re.findall('int\s+\w+\s=\s\d{0,10}|short\s+\w+\s=\s\d{0,10}.\d{0,10}|byte\s+\w+\s=\s\d[01]{0,10}',text[i])
        searchForResult = re.search('int\s+\w+\s=\s\d{0,10}|short\s+\w+\s=\s\d{0,10}.\d{0,10}|byte\s+\w+\s=\s\d[01]{0,10}',text[i])
        if searchForResult != None:
            print('Line - ',i,' Position - ',searchForResult.span(),' : ',result)
#------------------------------------------------------------------------------------
                                                                                    # working with file here
def workWithFile(pathToFile):
    rfile = open(pathToFile)
    #fileString = rfile.read()
    fileString = rfile.readlines()   
    searching(fileString)
    

#------------------------------------------------------------------------------------
                                                                                    # somekind of normal input with exc.
finish_it = False
while finish_it !=True:
    try:
        _pathToFile = input('ENTER PATH TO THE FILE (C:\\FOLDER\\FILE.txt)\n')
        workWithFile(_pathToFile)
        finish_it = True    
    except(FileNotFoundError,OSError):
        print('FILE NOT FOUND!')
    
        