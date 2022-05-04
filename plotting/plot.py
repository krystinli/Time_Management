import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import date, timedelta, datetime as dt

def plot_month_trend(
        data,
        colname,
        color,
        img_name,
        months_count = 8,
    ):
    """Plot bar chart that represents monthly trends of a specific column.

    Parameters
    ----------
    data : DataFrame
        Updated data with the new entires
    colname : str
        Name of the column in data being plotted
    color : str
        Colour of the bars
    img_name : str
        File name of the img saved under img/
    months_count : str
        Number of months included in the plot

    Returns
    -------
    plot : matplotlib
        bar chart
    """
    # create Year-Month column
    data["Year-Month"] = data["Date"].apply(lambda x: x.strftime("%Y-%m"))

    # tramsform df into a monthly aggregate
    monthly_data = data[["Year-Month", colname]].groupby(
        ["Year-Month"]).sum().reset_index().sort_values(["Year-Month"])

    # filter out most recent months
    monthly_data_recent = monthly_data.tail(months_count)

    # plot bar chart
    fig, ax = plt.subplots()
    fig.set_size_inches(18, 5) # img size

    bars = ax.bar(
        monthly_data_recent["Year-Month"], # x-axis
        monthly_data_recent[colname], # y-axis
        color = color,
    )
    ax.set(
        xlabel = "Year-Month",
        ylabel = "Total Monthly Hours",
        title = img_name,
    )
    ax.bar_label(
        bars,
        fontsize = 14,
    )
    plt.savefig("img/" + img_name + ".png")
    print("Generated plot for", img_name)

def plot_day_trend(
        data,
        colname,
        color,
        img_name,
        target_low, # benchmark
        target_high = 0,
        days_count = 20,
    ):
    """Plot line chart that represents daily trends of a specific column.

    Parameters
    ----------
    data : DataFrame
        Updated data with the new entires
    colname : str
        Name of the column in data being plotted
    color : str
        Colour of the dots
    img_name : str
        File name of the img saved under img/
    target_low : int
        Benchmark repesented by a dotted line
    target_high : int
        Benchmark repesented by a dotted line
    days_count : str
        Number of days included in the plot

    Returns
    -------
    plot : matplotlib
        line chart
    """
    # filter out recent days data
    data = data[
        data.Date >= (date.today() - timedelta(days=days_count)).strftime("%Y-%m-%d")].copy()
    data.set_index("Date", inplace=True)

    # create a static plot with matplotlib
    fig, ax = plt.subplots()
    fig.set_size_inches(18, 5) # img size

    ax.plot(
        colname,
        data = data,
        color = "black",
        linewidth = 1,
        marker = 'o',
        markeredgecolor = color,
        markersize = 8,
    )

    ax.set(
        xlabel = "Date",
        ylabel = "Performance",
        title = colname,
    )

    # target line
    plt.axhline(y=target_low, c='black', linestyle='--', linewidth=2)
    # plt.axhline(y=target_high, c='g', linestyle='--')
    plt.legend()

    plt.savefig("img/" + img_name + ".png")
    print("Generated plot for", colname)


def plot_exercise():
    """
    plot body and mind investment
    (Sub category of of self-care)
    save it under img/
    This month theme: exercise!
    """
    # day of the week
    data=[["Week 1",0,1,2,0,1,0,1,],
          ["Week 2",0,0,1,2,1,0,1,],
          ["Week 3",0,1,0,1,0,1,0,],
          ["Week 4",1,0,1,0,1,0,1,], # this week
          ["Week 5",0,0,0,0,0,0,0,],
          ]

    # # day of the week
    # data=[["Week 1",0,0,0,0,0,0,0,], # this week
    #       ["Week 2",0,0,0,0,0,0,0,],
    #       ["Week 3",0,0,0,0,0,0,0,],
    #       ["Week 4",0,0,0,0,0,0,0,],
    #       ["Week 5",0,0,0,0,0,0,0,],
    #       ]

    # convert above data into pd df
    df=pd.DataFrame(
        data,
        columns=["Week of the Month","Mon","Tue","Wed","Thu","Fri","Sat","Sun"])

    df.plot(
        x = "Week of the Month",
        y = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"],
        kind = "bar",
        figsize = (18,8),
        title = "Apr Workout Breakdown Analysis",
        stacked = True,
        legend = True,
        colormap = "spring" # https://matplotlib.org/stable/tutorials/colors/colormaps.html
    )

    plt.savefig("img/" + "2022_Apr_Tracking" + ".png")
    print("Generated plot for body_mind.")

def plot_self_control():
    """
    plot self_control times
    save it under img/
    This month theme:
        1) Get back to work
        2) Control eating
    """
    # day of the week
    data=[["Week 1",0,0,0,0,0,0,0,], # this week
          ["Week 2",0,0,0,0,0,0,0,],
          ["Week 3",0,0,0,0,0,0,0,],
          ["Week 4",0,0,0,0,0,0,0,],
          ["Week 5",0,0,0,0,0,0,0,],
         ]

    # convert above data into pd df
    df=pd.DataFrame(
        data,
        columns=["Week of the Month","Mon","Tue","Wed","Thu","Fri","Sat","Sun"])

    df.plot(
        x = "Week of the Month",
        y = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"],
        kind = "bar",
        figsize = (18,8),
        title = "Mar Self-Control Tracking",
        stacked = True,
        legend = True,
        colormap = "coolwarm" # https://matplotlib.org/stable/tutorials/colors/colormaps.html
    )

    plt.savefig("img/" + "2022_Mar_Tracking2" + ".png")
    print("Generated plot for self_control.")
