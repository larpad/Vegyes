# import argparse
import getopt
import sys
# import os
import pathlib
from main_webserver import *
from bl_vicc import *
from bl_excel import *
from bl_pdf import *

txt_help = """
Ez a prog leírása.
Nem tudom, hogy ide még mit kéne írni
"""

start_command = False
start_gui = False
start_web = False
doc_type = ''
path_pdf = ''
path_excel = ''
start_excel_tetel = False
start_vicc = False
try:
    opts, args = getopt.getopt(sys.argv[1:], "gwkmwp:e:tv", ["gui","web","kozoskolteg","menza","pdf=","excel=","tetel","vicc"])
except getopt.GetoptError:
    print(txt_help)
    sys.exit(2)

print(opts)

#start_web = True
start_gui = True

for opt,arg in opts:
    if opt in ('-g', '--gui'):
        start_command = False
        start_gui = True
    elif opt in ('-w', '--web'):
        start_command = False
        start_web = True
    elif opt in ('-k', '--kozoskolteg'):
        start_command = True
        doc_type = 'KOZOSKOLTSEG'
    elif opt in ('-m', '--menza'):
        start_command = True
        doc_type = 'MENZA'
    elif opt in ('-p', '--pdf'):
        path_pdf = arg
    elif opt in ('-e', '--excel'):
        path_excel = arg
    elif opt in ('-t', '--tetel'):
        start_command = True
        start_excel_tetel = True
    elif opt in ('-v', '--vicc'):
        start_vicc = True

if start_command:
    print('CMD')
    print('PDF',path_pdf)
    print('EXCEL',path_excel)
    print('Megtekintés',start_excel_tetel)

    path_pdf_valid = False
    if path_pdf != '':
        path_pdf_valid = os.path.isfile(path_pdf)
        if path_pdf_valid:
            path_pdf_valid = (pathlib.Path(path_pdf).suffix.upper() == '.PDF')



    path_excel_valid = False
    if path_excel != '':
        path_excel_valid = os.path.isfile(path_excel)
        if path_excel_valid:
            path_excel_valid = (pathlib.Path(path_excel).suffix.upper() in ('.XLS','.XLSX'))

    l_befizetes = get_befizetes(path_excel)
#    crete_watermark(l_befizetes)

    if (start_excel_tetel and path_excel_valid):
        print('Tétel')
        for item in l_befizetes:
            print(item)

    if  doc_type == 'KOZOSKOLTSEG':
        print('Közösköltség')
#        pecseteles(path_excel, path_pdf)
    sys.exit(0)


elif start_gui:
    print('GUI')
    sys.exit('A GUI lefutott')

elif start_web:
    print('Webserver indítás')
    vs = Webserver()
    vs.run()
    sys.exit(0)

elif start_vicc:
    print('Jönnek a viccek:')
    viccek = [ {'type': 'dad', 'setup': 'Why do fathers take an extra pair of socks when they go golfing?', 'punchline': 'In case they get a hole in one!', 'id': 385}
              ,{'type': 'general', 'setup': 'What musical instrument is found in the bathroom?', 'punchline': 'A tuba toothpaste.', 'id': 264}
              ,{'type': 'general', 'setup': 'Well...', 'punchline': 'That’s a deep subject.', 'id': 65}
              ,{'type': 'general', 'setup': 'Do you know where you can get chicken broth in bulk?', 'punchline': 'The stock market.', 'id': 107}
              ,{'type': 'general', 'setup': 'Why do bees have sticky hair?', 'punchline': 'Because they use honey combs!', 'id': 348}
              ,{'type': 'general', 'setup': 'What does the mermaid wear to math class?', 'punchline': 'Algae-bra.', 'id': 401}
              ,{'type': 'general', 'setup': "What do you call a bee that can't make up its mind?", 'punchline': 'A maybe.', 'id': 379}
              ,{'type': 'general', 'setup': 'Did you hear about the kidnapping at school?', 'punchline': "It's ok, he woke up.", 'id': 91}
              ,{'type': 'general', 'setup': 'Did you hear the one about the guy with the broken hearing aid?', 'punchline': 'Neither did he.', 'id': 101}
              ,{'type': 'general', 'setup': 'What did the Zen Buddist say to the hotdog vendor?', 'punchline': 'Make me one with everything.', 'id': 188}
            ]
    #viccek = jokes()
    for vicc in viccek:
        #print(vicc)
        print('- ',vicc.get('setup'))
        print('  ',vicc.get('punchline'))
    sys.exit(0)

else:
    print('No akkor mi legyen?!')
    sys.exit('Start NONE')




######################################

