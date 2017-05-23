my_file = open('text.txt','r')       #Open file in readonly mode

#print(my_file.read())               #Printing all symbols
my_string = my_file.read()
my_string = my_string.lower()        #lower reg
noSymb = []                          #array for letters without symbols(#!^&*$...)
for i in range(len(my_string)):
    if my_string[i].isalpha():
        noSymb.append( my_string[i] )

#------------------------------------
dict = {}                            #Frequensy of letter
for i in range(len(noSymb)):
    counter = 0
    for j in noSymb:
        if noSymb[i] == j:
            counter = counter + 1
            dict[noSymb[i]] = counter
 #-----------------------------------
                                     #Sorting by freq
#SortedValues = dict.values()
#SortedValues = list(SortedValues)
#SortedValues.sort(reverse = True)
#print(SortedValues)
#print( sorted(dict.items(), reverse=True))     
l = lambda x: x[1]
SortedValues = sorted(dict.items(), key=l, reverse=True) 
#-----------------------------------
                                    #Output
print ('Unsorted: \n',dict,"\n\n",'Sorted: \n',SortedValues)
#print (SortedValues)
#TODO: Sort by param
my_file.close()