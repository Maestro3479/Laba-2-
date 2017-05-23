import re

#------------------------------------------------------------------------------------
                                                                                    #findal
def yaUstal(daiText):
    zabiraiText = ''
    splitText = daiText.split(' ')
    for i in range(len(splitText)):
        zabiraiText = re.findall('[A-Z]{1}[a-z]+\d{4}|[A-Z]{1}[a-z]+\d{2}',splitText[i])
        print(zabiraiText)
#------------------------------------------------------------------------------------
                                                                                    #Input
moyaLyoubimayaStrokaNaMnogoSimvolov = input('Brat, vvedi pojalusta stroky - > ')
yaUstal(moyaLyoubimayaStrokaNaMnogoSimvolov)