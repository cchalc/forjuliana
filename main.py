# Import libraries
import os #operating system
import pandas as pd #pandas for dataframe management
import matplotlib.pyplot as plt #matplotlib for plotting
import matplotlib.dates as mdates # alias for date formatting

# Data
dataPath = './' # set data path
df = pd.read_csv(os.path.join(dataPath, 'data.csv')) # read in data
df['date'] = pd.to_datetime(df['date']) # convert column to datetime
df.set_index('date', inplace=True) # set date as the index
df_avg = df.resample('D').mean() # resample by DAY and take the mean and create a new dataframe called df_avg

#plot data
# You would need to experiment around with some of the plot settings to get the desired result
fig, ax = plt.subplots(figsize=(15,7))
df_avg.plot(ax=ax, kind='bar')
plt.show()


# #set ticks every week
# ax.xaxis.set_major_locator(mdates.WeekdayLocator())
# #set major ticks format
# ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))