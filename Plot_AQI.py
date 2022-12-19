import pandas as pd
import matplotlib.pyplot as plt
import re
import os

def avg_data_in_year(year):
        average = []
        for rows in pd.read_csv(f'Data/AQI/aqi{year}.csv',chunksize=24):
            df=pd.DataFrame(rows) 
            pm2_values=[]
            var=0
            avg=0
            for index,row in df.iterrows():
                pm2_values.append(row['PM2.5'])
            for value in pm2_values:
                if type(value) is float or type(value) is int:
                    var+=value
                elif type(value) is str:
                    if value!='NoData' and value!='PwrFail' and value!='---' and value!='InVld':
                        var+=float(value)
            avg=var/24
            average.append(avg)
        return average



if __name__=="__main__":

    plt.plot(range(0,365),avg_data_in_year(2013),label="2013 data")
    plt.plot(range(0,364),avg_data_in_year(2014),label="2014 data")
    plt.plot(range(0,365),avg_data_in_year(2015),label="2015 data")
    plt.plot(range(0,365),avg_data_in_year(2016),label="2016 data")
    plt.xlabel('Day')
    plt.ylabel('PM 2.5')
    plt.legend(loc='upper right')
    plt.show()
