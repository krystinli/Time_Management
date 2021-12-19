import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import date, timedelta, datetime

def transform_data(
    data,
    days_count=30,
    # current benchmark setting for weekday
    weekday_work_exp=2,
    weekday_dev_exp=0.5,
    weekday_care_exp=1,
    # current benchmark setting for weekend
    weekend_work_exp=0,
    weekend_dev_exp=0.5,
    weekend_care_exp=1.5,
    ):
    """
    set "Date" as index column
    cut date into relevant range
    Transform the Y-axis value from hours to performance

    performance = expected hours - actual hours
    """
    # transform y-axis from hours to performance
    data["Work_Scaled"] = np.where(
        (data["Day"]=="Saturday") | (data["Day"]=="Sunday"),
        data["Work"] - weekend_work_exp,
        data["Work"] - weekday_work_exp,)

    data["Dev_Scaled"] = np.where(
        (data["Day"]=="Saturday") | (data["Day"]=="Sunday"),
        data["Development"] - weekend_dev_exp,
        data["Development"] - weekday_dev_exp,)

    data["Care_Scaled"] = np.where(
        (data["Day"]=="Saturday") | (data["Day"]=="Sunday"),
        data["Self-Care"] - weekend_care_exp,
        data["Self-Care"] - weekday_care_exp,)

    data["Total"] = data["Work"] + data["Development"] + data["Self-Care"]

    # calculate the time period to plot
    last_month = date.today() - timedelta(days=days_count)
    data = data[
        (data.Date >= last_month.strftime("%Y-%m-%d")) &
        (data.Date <= date.today().strftime("%Y-%m-%d"))]

    # set date as index
    data.Date = pd.to_datetime(data.Date)
    data.set_index("Date", inplace=True)
    return data.sort_index()

def plot_static(
        data,
        colname,
        color,
        img_name,
        target_low, # benchmark
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
    plt.axhline(y=target_low, c='black', linestyle='--', linewidth=2)
    # plt.axhline(y=target_high, c='g', linestyle='--')
    plt.legend()

    plt.savefig("img/" + img_name + ".png")
    print("Generated plot for", colname)

def plot_leetcode():
    """
    plot leetcode progress
    save it under img/
    """
    x = ["2021-09", "2021-10", "2021-11", "2021-12",]
    z = [0, 0, 0, 0] # total by month end
    y = [0, 0, 0, 0] # difference

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
