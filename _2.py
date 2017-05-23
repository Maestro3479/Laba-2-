import subprocess
import os
import hashlib
#print(hashlib.sha224(b"?").hexdigest())
#-------------------------------------------------------
                                                        #Exception for input
def printPath():
    try:
        PATH = input('ENTER THE PATH -> ')
        print(os.listdir(PATH))
        subprocess.Popen('explorer "%s"'%(PATH))
        return PATH
    except(FileNotFoundError,OSError,UnicodeEncodeError):
        print('ENTER CORRECT PATH! RUS NOT ALLOWED!')
        printPath()

PATH = printPath()
filez = os.listdir(PATH)
#-------------------------------------------------------
                                                        #md5 calc
def getMD5sum(fileName):
    m = hashlib.md5()
    
    fd = open(fileName, 'r')
    b = fd.read()
    m.update(b.encode('utf-8'))
    fd.close()
    return m.hexdigest()

#-------------------------------------------------------
                                                        #Checking subfolders
dict = {}
dictDublicates = {}
for top, dirs, files in os.walk(PATH):
    for nm in files:
        fname =  os.path.join(top, nm)   
        fname = str(fname)
        #print (fname)
        #print(hashlib.sha224(fname.encode('utf-8')).hexdigest())
        #dict[hashlib.md5(fname.encode('utf-8')).hexdigest()] = fname.encode('utf-8')
        md5sum = getMD5sum(fname)
        #print(md5sum)
        if md5sum  in dict.keys():
            dictDublicates[md5sum] = str(fname+';  '+dict[md5sum])
        dict[md5sum] = fname
#-------------------------------------------------------
                                                        #Output
print(dict,'\n')
print('GROUP OF DUBLICATED FILES: \n',dictDublicates)
              


