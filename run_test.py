import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import date, timedelta, datetime as dt
import os

# os.chdir('../Time_Management')
data = pd.read_csv("data/data2.csv")
data.Date = pd.to_datetime(data.Date)
data.set_index("Date", inplace=True)
data.head()

data.columns
data.index

# matplotlib
fig, ax = plt.subplots()
fig.set_size_inches(18, 5) # img size

ax.plot(
    x = data.index,
    y = [data.Work, data.Development, data["Self-Care"]],
    kind = "bar",
    linewidth = 1,
    marker = 'o',
    markersize = 8,
    stacked = True,
)

ax.set(
    xlabel = "Date",
    ylabel = "Work",
)
