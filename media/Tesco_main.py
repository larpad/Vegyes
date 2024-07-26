import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline

df = pd.read_csv(r"C:\Users\Apu\Desktop\DataSet_Tesco5000_withDaynum.csv")
df["year"] = df["visit_date"].apply(lambda x: int(x[:4]))
df["month"] = df["visit_date"].apply(lambda x: int(x[5:7]))
df["day"] = df["visit_date"].apply(lambda x: int(x[8:10]))

df["week_day"] = df["daynum"].apply(lambda x: (x+3) % 7)
print(df.head())

stat_year = df.groupby(["year"], as_index= False).agg(koltes = ("visit_spend","sum"))
stat_month = df.groupby(["month"], as_index= False).agg(koltes = ("visit_spend","sum"))
stat_day = df.groupby(["day"], as_index= False).agg(koltes = ("visit_spend","sum"))
stat_week_day = df.groupby(["week_day"], as_index= False).agg(koltes = ("visit_spend","sum"))

stat_customer = df.groupby(["customer_id"], as_index= False).agg(koltes = ("visit_spend","sum"))

print(stat_customer)

#plt.plot(df["visit_spend"],marker = "o")
#plt.plot(stat_year["year"],stat_year["koltes"], marker='o', linestyle='dashed', linewidth=2, markersize=12)
#plt.show()
#plt.plot(stat_month["month"],stat_month["koltes"], marker='o', linestyle='dashed', linewidth=2, markersize=12)
#plt.show()
#plt.plot(stat_day["day"],stat_day["koltes"], marker='o', linestyle='dashed', linewidth=2, markersize=12)
#plt.show()
#plt.plot(stat_week_day["week_day"],stat_week_day["koltes"], marker='o', linestyle='dashed', linewidth=2, markersize=12)
#plt.show()

plt.plot(stat_customer["customer_id"],stat_customer["koltes"], marker='o', linestyle='dashed', linewidth=2, markersize=12)
plt.show()
