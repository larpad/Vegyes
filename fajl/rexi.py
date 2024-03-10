import re

def Rexi():
    txt_word = 'Martint a szülei minden évben elvitték a nagymamájához a nyári szünetben.'  # txt
    txt_word = re.sub("e", "", txt_word)
    print(txt_word)

    # key = {0:'test', 1:'replace'}
    #
    # regx = re.compile('e')
    #
    # lines = ["that's a line",
    #          'another line',
    #          'a line to $$test$$',
    #          '123456',
    #          'here $$test$$ again',
    #          'closing line']
    #
    # for line in lines:
    #     line =  re.sub('_e_',line)
    #     print (line)