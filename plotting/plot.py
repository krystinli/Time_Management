import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import date, timedelta, datetime

def transform_data(
    data,
    days_count=30,
    # current benchmark setting
    weekday_work_exp=3,
    weekday_oth_exp=0.25,
    weekend_work_exp=0.5,
    weekend_oth_exp=1,
    ):
    """
    set "Date" as index column
    cut date into relevant range
    Transform the Y-axis value from hours to performance

    performance = expected hours - actual hours

    weekday expecation:
        work = 4 hr
        development = 0.5 hr
        self-care = 0.5 hr

    weekend expecation:
        work = 1 hr
        development = 1 hr
        self-care = 1 hr
    """
    # transform y-axis from hours to performance
    data["Work_Scaled"] = np.where(
        (data["Day"]=="Saturday") | (data["Day"]=="Sunday"),
        data["Work"] - weekend_work_exp,
        data["Work"] - weekday_work_exp,)

    data["Dev_Scaled"] = np.where(
        (data["Day"]=="Saturday") | (data["Day"]=="Sunday"),
        data["Development"] - weekend_oth_exp,
        data["Development"] - weekday_oth_exp,)

    data["Care_Scaled"] = np.where(
        (data["Day"]=="Saturday") | (data["Day"]=="Sunday"),
        data["Self-Care"] - weekend_oth_exp,
        data["Self-Care"] - weekday_oth_exp,)

    # calculate the time period to plot
    last_month = date.today() - timedelta(days=days_count)
    data = data[data.Date >= last_month.strftime("%Y-%m-%d")]

    # set date as index
    data.Date = pd.to_datetime(data.Date)
    data.set_index("Date", inplace=True)
    return data.sort_index()

def plot_static(
        data,
        colname,
        color,
        img_name,
        target_low=0,
        target_high=0
    ):
    """
    plot column
    save it under img
    """
    fig, ax = plt.subplots()
    fig.set_size_inches(18, 5) # img size

    ax.plot(colname,
        data = data,
        color = "black",
        linewidth = 1,
        marker = 'o',
        markeredgecolor = color,
        markersize = 5,)

    ax.set(xlabel = "Date",
           ylabel = "Performance",
           title = colname)

    # target line
    # plt.axhline(y=target_low, c='r', linestyle='--')
    plt.axhline(y=0, c='black', linestyle='--', linewidth=2)
    # plt.axhline(y=target_high, c='g', linestyle='--')
    plt.legend()

    plt.savefig("img/" + img_name + ".png")
    print("Generated plot for", colname)

def plot_leetcode():
    """
    plot leetcode progress
    save it under img/
    """
    x = ["2020-12", "2021-01", "2021-02", "2021-03",]
    z = [27, 29, 0, 0] # total by month end
    y = [9, 2, 0, 0] # difference

    fig, ax = plt.subplots()
    fig.set_size_inches(18, 5) # img size

    plt.bar(x, y,
            color="pink",
            edgecolor="yellow",
            linewidth=2,)

    ax.set(xlabel = "Month",
           ylabel = "Number of Questions",
           title = "Leetcode Questions completed",)

    plt.savefig("img/" + "leetcode" + ".png")
    print("Generated plot for leetcode.")
