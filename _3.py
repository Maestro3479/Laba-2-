#TODO: lower reg
#1. открыть тхт, по строчно, только для чтения
#2. Обработать строку, выделить из неё название файла
#3. найти в среди файлов что то с таким же названием
#4. переименовать
import os
import re
import shutil
#path = "E:\GitHub\PythonLabs\LR2\Task#3\\3\\3\MusDir"
#print(path)
basepath = os.path.abspath(os.path.dirname('MusDir'))
#print(basepath)
path = os.path.join(basepath, 'MusDir')
#-------------------------------------------------------
                                                       #Open txt, read-only, step-by-step
songList = open('MusDir\SongList.txt','r')
formatedList = songList.readlines()
dict = {}

for line in range(len(formatedList)):
    temp = formatedList[line]
    temp2 = formatedList[line]
    temp2 = str(temp2)
    temp2 = re.sub('\n',' ', temp2)
    print(temp2)
    temp = temp.split(' ')
    dict[temp[1]+'.mp3'] = str(temp2)
    
#temp = formatedList[2]
#temp = temp.split(' ') 

#print(temp)
#print(temp[1])
list = []
for top, dirs, files in os.walk(path):
    for nm in files:
        fname =  os.path.join(top, nm)   
        fname = str(fname)#.encode('utf-8') 
        print(fname)
        list.append(fname)
        if nm in dict.keys():
            os.rename(fname,top+"\\"+dict[nm]+'.mp3')
            #print('PATH TO MOVE ',top+"\\"+dict[nm]+'.mp3')
            #shutil.move('','')


#for i, filename in enumerate(os.listdir(basepath)):
#    os.chdir(basepath)
#    os.rename(filename, 'air{0}.png'.format(i+1))
 