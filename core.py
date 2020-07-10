# Code written by Jerin Rajan on 09th Jul 2020

# required libraries
import json
import pandas as pd
import matplotlib.pyplot as plt

# variables - initialisation 
fname = 'weather.json'
data_list = list()

# parse json file
with open(fname) as f:
    for i in f:
        res = json.loads(i)
        # filter the data for country - SZ
        if (res['city']['country'] == 'SZ'):
            # extract the required data into a new list
            data_list.append([res['city']['name'],res['main']['temp']])
            # convert into a data frame
            df_sz = pd.DataFrame(data=data_list,columns=['city','temp'])
        else:
            continue
   
# data visualisation - plot 
plt.plot(df_sz['city'],df_sz['temp'])
plt.grid('on')
plt.title ('Weather readings of cities in country: SZ')
plt.xlabel('City')
plt.xticks(rotation='vertical', fontsize=8)
plt.ylabel('Temp')

# Save plot as png
plt.savefig('weather_readings_cities_SZ.png', bbox_inches='tight')
plt.show()

   
   
   
   
    # country = res['city']['country'])

    # print(res['main'])
    # print(res['wind'])
    # print(res['clouds'])
    # print(res['weather'])


# filter data for one country - 'MG' or 'SZ'



# Data visualisation
#   


