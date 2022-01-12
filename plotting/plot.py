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
        markersize = 8,)

    ax.set(xlabel = "Date",
           ylabel = "Performance",
           title = colname)

    # target line
    plt.axhline(y=target_low, c='black', linestyle='--', linewidth=2)
    # plt.axhline(y=target_high, c='g', linestyle='--')
    plt.legend()

    plt.savefig("img/" + img_name + ".png")
    print("Generated plot for", colname)


def plot_body_mind():
    """
    plot body and mind investment
    (Sub category of of self-care)
    save it under img/
    """
    # workout, meditation, nap
    data=[["Week 1",1,1,1], # Sunday (Starting Point)
          ["Week 2",0,1,2], # Jan 10-16
          ["Week 3",0,0,0],
          ["Week 4",0,0,0]]

    df=pd.DataFrame(data,
        columns=["Week of the Month","workout","meditation","nap"])

    df.plot(
        x="Week of the Month",
        y=["workout", "meditation", "nap"],
        kind="bar",
        figsize=(18,5)
    )

    plt.savefig("img/" + "2022_Jan_Tracking" + ".png")
    print("Generated plot for body_mind.")
