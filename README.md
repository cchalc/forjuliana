# Demand Data Analysis
1. Install python3 and git (if not installed already)
2. Clone repo
```console
git clone https://github.com/cchalc/forjuliana.git
```
3. Change directory
```console
cd forjuliana
```
4. Install requirements
```console
pip install -r requirements.txt
```
5. Run script
```console
python main.py
```

## Notes
### 2020-11-25
Given the data provided I just took the average for the day and then plotted. It seems like a pretty straitforward task and you can work on the plotting for months and years. If you provide me the years worth of data I can do it for you. But you can just create a plotting function and stick it into a loop to generate the plots you want for months and years.

Hopefully this is what you want ..but there is a possibility that I did not understand the complexity of the task and just took the easy out approach. :) 

GL.

### 2020-11-30
I could not figure out how to pull all the data you required...so I just generated some synthetic data based on the sample that you provided to me. I just created a timeseries called `ts` using the interval provided. I then calculated the dailys and monthlys. Finally for the plotting I just set up a for loop to loop over months and create a demand bar chart using the daily averages. If you want the actual values you can just use the `ts_daily` and `ts_monthly` which I output to `daily_average.csv` and `monthly_average.csv` respectively. 

The idea is now that once you have your dataset you can modify this script as you see fit. Also if you want to play around with the plotting as well as I just quickly pushed something out.