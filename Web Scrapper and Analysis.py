import requests
import pandas as pd
import re
from bs4 import BeautifulSoup
url=requests.get("http://www.worldometers.info/world-population/india-population/")
t=url.text
so=BeautifulSoup(t,'html.parser')
all_t=so.findAll('table', class_="table table-striped table-bordered table-hover table-condensed table-list")#Use to find stats tabl
d1=pd.DataFrame([])
i=0
j=0
b=[]
d1=pd.DataFrame()
for j in all_t[0].findAll('td'):
    b.append(j.text)
while(i<=(208-13)):
    d1=d1.append(pd.DataFrame([b[i:i+13]]) )
    i=i+13
d1.apply(pd.to_numeric, errors='ignore')

listq=pd.Series.tolist(d1[0:16][0])
list1=pd.Series.tolist(d1[0:16][1])
list2=pd.Series.tolist(d1[0:16][2])
list3=pd.Series.tolist(d1[0:16][3])
list4=pd.Series.tolist(d1[0:16][4])
list5=pd.Series.tolist(d1[0:16][5])
list6=pd.Series.tolist(d1[0:16][6])
list7=pd.Series.tolist(d1[0:16][7])
list8=pd.Series.tolist(d1[0:16][8])
list9=pd.Series.tolist(d1[0:16][9])
list10=pd.Series.tolist(d1[0:16][10])

#forecast table
c=[]
for j in all_t[1].findAll('td'):
    c.append(j.text)
bv=pd.DataFrame()
i=0
while(i<=(91-13)):
    bv=bv.append(pd.DataFrame([c[i:i+13]]) )
    i=i+13 
listq1=pd.Series.tolist(bv[0:7][0])
list11=pd.Series.tolist(bv[0:7][1])
list21=pd.Series.tolist(bv[0:7][2])
list31=pd.Series.tolist(bv[0:7][3])
list41=pd.Series.tolist(bv[0:7][4])
list51=pd.Series.tolist(bv[0:7][5])
list61=pd.Series.tolist(bv[0:7][6])
list71=pd.Series.tolist(bv[0:7][7])
list81=pd.Series.tolist(bv[0:7][8])
list91=pd.Series.tolist(bv[0:7][9])
list101=pd.Series.tolist(bv[0:7][10])    
    
    
    

#Current population
DataFrame=pd.DataFrame({"Year":listq,"Population":list1,"Yearly % Change":list2,"YearlyChange":list3,"Migrants (net)":list4,"Median Age":list5,"Fertility Rate	Density (P/Km²)	UrbanPop ":list6,"Urban Population":list7,"Gross domestic product % growth":list8,"World Population":list9,"India Global Rank":list10})
DataFrame1=pd.DataFrame({"Year":listq1,"Population":list11,"Yearly % Change":list21,"YearlyChange":list31,"Migrants (net)":list41,"Median Age":list51,"Fertility Rate	Density (P/Km²)	UrbanPop ":list61,"Urban Population":list71,"Gross domestic product % growth":list81,"World Population":list91,"India Global Rank":list101})
print("Current Population")
print(DataFrame)
print("Future Popultion")
print(DataFrame1)
listf=[]
listf1=[]
for i in range(0,16):
    r = re.sub(",", "", list1[15-i])
    listf.append(int(r))
for m in range(0,7):
    r = re.sub(",", "", list11[6-m])
    listf1.append(int(r))    
    
    
import matplotlib.pyplot as plt
d2=pd.to_numeric(listq, errors='ignore')
dl=pd.to_numeric(listq1, errors='ignore')
listq=pd.to_numeric(d2)
listdf=pd.to_numeric(dl)
plt.figure(1)


plt.subplot(221)
plt.plot(listq[::-1],listf, color='green', linestyle='dashed', linewidth = 3,
         marker='o', markerfacecolor='blue', markersize=10)
plt.ylabel(" Current Population")
plt.xlabel("Year")

plt.subplot(224)
plt.plot(listdf[::-1],listf1, color='green', linestyle='dashed', linewidth = 3,
         marker='o', markerfacecolor='blue', markersize=10)
plt.ylabel("Predicted Population")
plt.xlabel("Year")
plt.grid(True,color="g")
plt.show()
