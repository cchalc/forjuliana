# Import libraries
import os #operating system
import pandas as pd #pandas for dataframe management
import matplotlib.pyplot as plt #matplotlib for plotting
import matplotlib.dates as mdates # alias for date formatting
import numpy as np # for generating synthetic data

# Data
dataPath = './' # set data path
df = pd.read_csv(os.path.join(dataPath, 'data.csv')) # read in data
df['date'] = pd.to_datetime(df['date']) # convert column to datetime
df.set_index('date', inplace=True) # set date as the index
df_avg = df.resample('D').mean() # resample by DAY and take the mean and create a new dataframe called df_avg


############################ NEW #############################

# Moving on .. synthetic data
# This extracts the data as an array, creates a sythetic interval, samples the data based on provided data, and creates a new time series
data = df['demand'].values
interval = pd.date_range('2018-11-01', '2020-10-30', freq='15min')
synthetic_data = np.random.choice(data, len(interval))
ts = pd.DataFrame({'demand': synthetic_data}, index=interval)
ts.index.name = 'date'

# resampling analysis 
ts_daily = ts.resample('D').mean()
days = ts_daily.index.strftime("%Y-%m-%d")
ts_monthly = ts.resample('M').mean()
months = ts_monthly.index.strftime("%Y-%m")

# Here we can just loop over what months we want to generate plots for
for month in months[2:5]:
    fig, ax = plt.subplots(figsize=(15,7))
    ts_daily[month].plot(ax=ax, kind='bar')

    # display
    plt.title("Monthly demand for {}".format(month))
    plt.xlabel("day of month")
    plt.ylabel('demand')

    # #set ticks every week
    ax.xaxis.set_major_locator(mdates.WeekdayLocator())
    #set major ticks format
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%d'))

    # plt.show()
    plt.savefig('figures/{}'.format(month))

    # Output the daily data
    ts_daily.to_csv("daily_average.csv", index=True)
    ts_monthly.to_csv("monthly_average.csv", index=True)