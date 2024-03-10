from datetime import datetime
from datetime import date
from datetime import timedelta
def Ido():

    dateszul = datetime(1972,4,8)
    now = datetime.now()
    kul = now - dateszul
    print(kul )
    print(datetime.min+kul)
    eletkor_out = datetime.min+kul + timedelta(days = (-365))

    szul_time = dateszul.strftime("%Y.%m.%d %H:%M:%S")
    now_time = now.strftime("%Y.%m.%d %H:%M:%S")
    eletkor_time = eletkor_out.strftime("%Y.%m.%d %H:%M:%S")
    print("Szul dat =", szul_time)
    print("Current Time =", now_time)
    print("Életkor =", eletkor_time)

    # seconds = 86399
    # print(td)
    # dt = datetime.datetime.strptime(str(td), "%H:%M:%S")
    # print(dt)