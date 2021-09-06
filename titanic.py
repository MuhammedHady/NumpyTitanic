import csv
import numpy as np
import pandas as pd

### Read CSV file
with open('titanic.csv', newline='\n') as csvfile:
    my_list = list(csv.reader(csvfile))
data = np.array(my_list)       ### Converting list to array
List=data[0]
Males=[]
Females=[]
Survivors=[]
LostChild=[]

num_of_arrays=data.shape[0]
print(num_of_arrays)

Males.append(List)             ### Adding indicators for Males file
Females.append(List)		   ### Adding indicators for Females file
Survivors.append(List)		   ### Adding indicators for Survivors file
LostChild.append(List)		   ### Adding indicators for LostChild file

### Getting all males formated as excel sheet 
for x in range (1,num_of_arrays):
	z = data[x,4]
	if z == 'male':
		y = data[x]
		Y = y.tolist()
		Males.append(Y)
print(Males)
pd.DataFrame(Males).to_csv("Males.csv")

### Getting all females formated as excel sheet
for x in range (1,num_of_arrays):
	z = data[x,4]
	if z == 'female':
		y = data[x]
		Y = y.tolist()
		Females.append(Y)
print(Females)
pd.DataFrame(Females).to_csv("Females.csv")

### Getting all survivors formated as excel sheet
for x in range (1,num_of_arrays):
	z = data[x,1]
	if z == '1':
		y = data[x]
		Y = y.tolist()
		Survivors.append(Y)
print(Survivors)
pd.DataFrame(Survivors).to_csv("Survivors.csv")

### Getting all LostChild formated as excel sheet
for x in range (1,num_of_arrays):
	z = data[x,5]
	if z <= '17':
		y = data[x]
		Y = y.tolist()
		LostChild.append(Y)
print(LostChild)
pd.DataFrame(LostChild).to_csv("LostChild.csv")

### Getting the Persentage of Survivors
Num_of_Survivors=len(Survivors)
print("\n Survivors : ",Num_of_Survivors)

Num_of_Passengers=len(my_list)-1
print("\n All Titanic Passengers : ",Num_of_Passengers)

Persentage = ( Num_of_Survivors / Num_of_Passengers ) * 100
print ("\n Survivors Persentage : %.2f"%Persentage,"%")
