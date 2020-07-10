'''
Code written by Jerin Rajan on 09th Jul 2020
Please refer to README.md file for more information before running the script
'''

# required libraries:
# ------------------
import json
import pandas as pd
import matplotlib.pyplot as plt

# variables - initialisation :
# --------------------------
fname = 'weather.json'
data_list = list()

# parse json file:
# ----------------
with open(fname) as f:
    for i in f:
        res = json.loads(i)
        # filter the data for country - SZ
        if (res['city']['country'] == 'SZ'):
            # define the source data to be captured to the new list
            data_source = [res['city']['name'],res['main']['temp']]
            # extract the required data into a new list
            data_list.append(data_source)
            # convert into a data frame
            df_sz = pd.DataFrame(data=data_list,columns=['city','temp'])
        else:
            continue
   
# Report the extracted data:
# --------------------------
print(df_sz)

# data visualisation - plot:
# --------------------------

# initialising plot with datasets and label
plt.plot(df_sz['city'],df_sz['temp'], label='temperature')
# grid = active
plt.grid('on')
# title for the plot
plt.title ('Temperature readings of cities in country: SZ')
# label for x-axis
plt.xlabel('City')
# orientation & font size for x label items - city names
plt.xticks(rotation='vertical', fontsize=8)
# label for y-axis
plt.ylabel('Temperature')
# legend = active and location - upper right 
plt.legend(loc=1)

# Save plot as png
plt.savefig('weather_readings_cities_SZ.png', bbox_inches='tight')
# show plot on figure
plt.show()


