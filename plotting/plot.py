import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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
    # day of the week
    data=[["Week 1",0,0,0,1,0,0,1,],
          ["Week 2",2,1,1,2,1,1,1,],
          ["Week 3",1,0,1,2,2,2,3,],
          ["Week 4",0,0,0,0,0,0,0,]] # this week

    # convert above data into pd df
    df=pd.DataFrame(
        data,
        columns=["Week of the Month","Mon","Tue","Wed","Thu","Fri","Sat","Sun"])

    df.plot(
        x = "Week of the Month",
        y = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"],
        kind = "bar",
        figsize = (18,8),
        title = "Feb Workout Breakdown Analysis",
        stacked = True,
        legend = True,
        colormap = "cool" # https://matplotlib.org/stable/tutorials/colors/colormaps.html
    )

    plt.savefig("img/" + "2022_Feb_Tracking" + ".png")
    print("Generated plot for body_mind.")

def plot_self_control():
    """
    plot self_control times
    save it under img/
    """
    # day of the week
    data=[["Week 1",0,0,0,0,0,0,0,],
          ["Week 2",0,0,0,0,0,0,0,],
          ["Week 3",0,0,0,0,1,2,2,], # this week
          ["Week 4",0,0,0,0,0,0,0,]]

    # convert above data into pd df
    df=pd.DataFrame(
        data,
        columns=["Week of the Month","Mon","Tue","Wed","Thu","Fri","Sat","Sun"])

    df.plot(
        x = "Week of the Month",
        y = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"],
        kind = "bar",
        figsize = (18,8),
        title = "Feb Self-Control Tracking",
        stacked = True,
        legend = True,
        colormap = "coolwarm" # https://matplotlib.org/stable/tutorials/colors/colormaps.html
    )

    plt.savefig("img/" + "2022_Feb_Tracking2" + ".png")
    print("Generated plot for self_control.")
