# import argparse
import getopt
import sys
import pathlib





def get_cmd_params():
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

    #print(opts)

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
    #app.run()
    sys.exit(0)

elif start_vicc:
    print('Jönnek a viccek:')
    viccek = jokes()
    for vicc in viccek:
        print(vicc)
    sys.exit(0)

else:
    print('No akkor mi legyen?!')
    sys.exit('Start NONE')




######################################

