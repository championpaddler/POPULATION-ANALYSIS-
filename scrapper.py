import requests
url=requests.get("http://wdi.worldbank.org/table/WV.1")
t=url.text
from bs4 import BeautifulSoup
so=BeautifulSoup(t,'html.parser')

all_t=so.findAll('div',{ "class":"spacer"})#Use to find stats table
l=[]
for i in range(34,2304):
    l.append(all_t[i].text)
i=0
p1=pd.DataFrame([])
while (i<len(l)-10):
    p1=p1.append(pd.DataFrame(l[i:i+10]).T)
    i=i+10 

x=p1[0:277][0]
y=p1[0:277][1]


listq=pd.Series.tolist(p1[0:277][0])
list1=pd.Series.tolist(p1[0:277][1])
list2=pd.Series.tolist(p1[0:277][2])
list3=pd.Series.tolist(p1[0:277][3])
list4=pd.Series.tolist(p1[0:277][4])
list5=pd.Series.tolist(p1[0:277][5])
list6=pd.Series.tolist(p1[0:277][6])
list7=pd.Series.tolist(p1[0:277][7])
list8=pd.Series.tolist(p1[0:277][8])
list9=pd.Series.tolist(p1[0:277][9])





DataFrame=pd.DataFrame({"Country":listq,"Population":list1,"Surface area":list2,"Population density":list3,"Gross national income, Atlas method":list4,"Gross national income per capita, Atlas method":list5,"Purchasing power parity gross national income":list6,"Purchasing power parity gross national income":list7,"Gross domestic product % growth":list8,"Gross domestic product per capita":list9})

DataFrame

