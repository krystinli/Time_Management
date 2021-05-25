import os
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date, timedelta, datetime

def transform_data(data, days_count):
    """
    set "Date" as index column
    cut date into relevant range
    """
    last_month = date.today() - timedelta(days=days_count)
    data = data[data.Date >= last_month.strftime("%Y-%m-%d")]

    data.Date = pd.to_datetime(data.Date)
    data.set_index("Date", inplace=True)
    return data.sort_index()

def plot_static(data, colname, color, target_low, target_high, img_name):
    """
    plot column
    save it under img/
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
           ylabel = "Hours",
           title = colname)

    # target line
    plt.axhline(y=target_low, color='r', linestyle='dashed')
    plt.axhline(y=target_high, color='g', linestyle='dashed')
    plt.legend()

    plt.savefig("img/" + img_name + ".png")
    print("Generated plot for", colname)

# def plot_leetcode():
#     """
#     plot leetcode progress
#     save it under img/
#     """
#     x = ["2020-12", "2021-01", "2021-02", "2021-03",]
#     z = [27, 29, 0, 0] # total by month end
#     y = [9, 2, 0, 0] # difference
#
#     fig, ax = plt.subplots()
#     fig.set_size_inches(18, 5) # img size
#
#     plt.bar(x, y,
#             color="pink",
#             edgecolor="yellow",
#             linewidth=2,)
#
#     ax.set(xlabel = "Month",
#            ylabel = "Number of Questions",
#            title = "Leetcode Questions completed",)
#
#     plt.savefig("img/" + "leetcode" + ".png")
#     print("Generated plot for leetcode.")
