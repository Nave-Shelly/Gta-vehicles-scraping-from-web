import requests
from bs4 import BeautifulSoup
import pandas as pd

res=requests.get('https://gtaforums.com/topic/187507-vehicle-stats/').text

soup=BeautifulSoup(res,'html.parser')

tr=soup.find_all('tr')

dataCars=[]
for t in tr[1:143]:
	items=t.find_all('td')
	if items:
		Names=items[0].text
		Money=items[1].text
		Mass=items[2].text
		tm=items[3].text
		sp=items[4].text
		drag=items[5].text
		gears=items[6].text
		dt=items[7].text
		eg=items[8].text
		dataCars+=[[Names,Money,Mass,tm,sp,drag,gears,dt,eg]]
		df=pd.DataFrame(dataCars,columns=['Vehicle','Money $','Mass (kg)','Turnmass (kg)','Speed (km)','Drag','Gears','Drivetype','Engine Type'])
		df.to_csv('gtacars.csv')
	

#bikes
dataBikes=[]
for t in tr[144:157]:
	items=t.find_all('td')
	if items:
		Names=items[0].text
		Money=items[1].text
		Mass=items[2].text
		tm=items[3].text
		whl=items[4].text
		sa=items[5].text
		tp=items[6].text
		drag=items[7].text
		gears=items[8].text
		dt=items[9].text
		eg=items[10].text
		dataBikes+=[[Names,Money,Mass,tm,whl,sa,tp,drag,gears,dt,eg]]
		df=pd.DataFrame(dataBikes,columns=['Vehicle','Money $','Mass (kg)','Turnmass (kg)','Wheelie Angle','Stoppie Angle','Speed (km)','Drag','Gears','Drivetype','Engine Type'])
		df.to_csv('gtabikes.csv')


	

#planes
dataPlanes=[]
for t in tr[158:182]:
	items=t.find_all('td')
	#yes
	if items:
		Names=items[0].text
		Money=items[1].text
		Mass=items[2].text
		tm=items[3].text
		tp=items[4].text
		gears=items[5].text
		dt=items[6].text
		eg=items[7].text
		dataPlanes+=[[Names,Money,Mass,tm,tp,gears,dt,eg]]
		df=pd.DataFrame(dataPlanes,columns=['Vehicle','Money $','Mass (kg)','Turnmass (kg)','Speed (km)','Gears','Drivetype','Engine Type'])
		df.to_csv('gtaplanes.csv')


#boats
dataBoats=[]
for t in tr[183:194]:
	items=t.find_all('td')
	if items:
		Names=items[0].text
		Money=items[1].text
		Mass=items[2].text
		tm=items[3].text
		tp=items[4].text
		drag=items[5].text
		gears=items[6].text
		eg=items[7].text
		dataBoats+=[[Names,Money,Mass,tm,tp,gears,eg]]
		df=pd.DataFrame(dataBoats,columns=['Vehicle','Money $','Mass (kg)','Turnmass (kg)','Speed (km)','Gears','Engine Type'])
		df.to_csv('gtaboats.csv')

