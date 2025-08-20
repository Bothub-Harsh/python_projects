import numpy as np

data=np.loadtxt("weather_data.csv",delimiter=",",skiprows=1,usecols=(2,3,4))

#average
tem_avg=np.mean(data[:,0])
hum_avg=np.mean(data[:,1])
rain_avg=np.mean(data[:,2])

#minimum
tem_min=np.min(data[:,0])
hum_min=np.min(data[:,1])
rain_min=np.min(data[:,2])

#maximum
tem_max=np.max(data[:,0])
hum_max=np.max(data[:,1])
rain_max=np.max(data[:,2])

#print session
print("Average Temperature:", tem_avg)
print("Average Humidity:", hum_avg)
print("Average Rainfall:", rain_avg)
print("\nMin Temp:", tem_min, " | Max Temp:",tem_max )
print("Min Humidity:", hum_min, " | Max Humidity:",hum_max )
print("Min Rainfall:", rain_max, " | Max Rainfall:",rain_max )

#find hottest day
day=np.loadtxt("weather_data.csv",delimiter=",",skiprows=1,usecols=(0),dtype=str)
hottest_day=day[np.argmax(data[:,0])]
wettest_day=day[np.argmax(data[:,1])]
rainmost_day=day[np.argmax(data[:,2])]

#result save
results =[
 ["Average Temp",tem_avg ],
 ["Average Humidity", hum_avg],
 ["Average Rainfall", rain_avg],
 ["Max Temp Day", hottest_day],
 ["Max Humidity Day", wettest_day],
 ["Max Rainfall Day", rainmost_day]
]

np.savetxt("weather_result.csv",results,delimiter=",",fmt="%s")
