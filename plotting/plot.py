import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import date, timedelta, datetime as dt
import os

def plot_stacked_bar():
    """Plot bar chart that represents weekly exercise record of the month.

    Parameters
    ----------

    Returns
    -------
    plot : matplotlib
        stacked bar chart
    """
    # day of the week
    data = [
        ["Week 1",0,0,1,1,0,0,0,],
        ["Week 2",0,1,0,1,0,1,1,],
        ["Week 3",0,1,0,0,0,0,0,], # this week
        ["Week 4",0,0,0,0,0,0,0,],
        ["Week 5",0,0,0,0,0,0,0,],
    ]

    # convert above data into pd df
    df = pd.DataFrame(
        data,
        columns = [
            "Week of the Month",
            "Mon",
            "Tue",
            "Wed",
            "Thu",
            "Fri",
            "Sat",
            "Sun"],
        )

    data_leetcode = [
        ["June_2022",62,15,0],
        ["July_2022",63,15,0], # this month
        ["Aug_2022",0,0,0,],
        ["Sep_2022",0,0,0,],
        ["Oct_2022",0,0,0,],
        ["Nov_2022",0,0,0,],
    ]

    df_leetcode = pd.DataFrame(
        data_leetcode,
        columns = ["Month", "Easy", "Medium", "Hard"],)

    # plot exercise
    df.plot(
        x = "Week of the Month",
        y = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"],
        kind = "bar",
        figsize = (18,8),
        title = "Workout Breakdown Analysis",
        stacked = True,
        legend = True,
        colormap = "Pastel1" # https://matplotlib.org/stable/tutorials/colors/colormaps.html
    )
    plt.savefig("img/" + "2022_July_Tracking" + ".png")

    # plot leetcode
    df_leetcode.plot(
        x = "Month",
        y = ["Easy", "Medium", "Hard"],
        kind = "bar",
        figsize = (18,8),
        title = "Leetcode Progress",
        stacked = True,
        legend = True,
        colormap = "Pastel2" # https://matplotlib.org/stable/tutorials/colors/colormaps.html
    )
    plt.savefig("img/" + "2022_Leetcode_Tracking" + ".png")
    print("Generated plot for exercising and leetcode.")

def plot_month_trend(
        data,
        colname,
        color1,
        color2,
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
    color1 : str
        Colour of the bars before equal 2022-02
    color2 : str
        Colour of the bars after 2022-02
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

    # conditional colour
    x = monthly_data_recent["Year-Month"]
    y = monthly_data_recent[colname]

    # colour change in plots
    mask1 = x <= "2025-05"
    mask2 = x > "2025-05" # change month

    # plt.bar
    bars1 = ax.bar(
        x[mask1],
        y[mask1],
        color = color1,
    )
    bars2 = ax.bar(
        x[mask2],
        y[mask2],
        color = color2,
    )

    # labels
    ax.set(
        xlabel = "Year-Month",
        ylabel = "Total Monthly Hours",
        title = img_name,
    )
    ax.bar_label(
        bars1,
        fontsize = 14,
    )
    ax.bar_label(
        bars2,
        fontsize = 14,
    )
    plt.savefig("img/" + img_name + ".png")
    print("Generated plot for", img_name)

def plot_week_trend(
        data,
        colname,
        color1,
        color2,
        img_name,
        weeks_count = 8,
    ):
    """Plot bar chart that represents monthly trends of a specific column.

    Parameters
    ----------
    data : DataFrame
        Updated data with the new entires
    colname : str
        Name of the column in data being plotted
    color1 : str
        Colour of the bars before equal 2022-02
    color2 : str
        Colour of the bars after 2022-02
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
    # data["Year-Month"] = data["Date"].apply(lambda x: x.strftime("%Y-%m"))
    data["Year-Month-Week"] = data["Date"].apply(lambda x: x.strftime("%Y-%m") + f"-W{x.isocalendar()[1]}")

    # tramsform df into a monthly aggregate
    weekly_data = data[["Year-Month-Week", colname]].groupby(
        ["Year-Month-Week"]).sum().reset_index().sort_values(["Year-Month-Week"])

    # filter out most recent months
    weekly_data_recent = weekly_data.tail(weeks_count)

    # plot bar chart
    fig, ax = plt.subplots()
    fig.set_size_inches(18, 5) # img size

    # conditional colour
    x = weekly_data_recent["Year-Month-Week"]
    y = weekly_data_recent[colname]

    # colour change in plots
    mask1 = x <= "2025-10"
    mask2 = x > "2025-10"  # change month

    # plt.bar
    bars1 = ax.bar(
        x[mask1],
        y[mask1],
        color = color1,
    )
    bars2 = ax.bar(
        x[mask2],
        y[mask2],
        color = color2,
    )

    # labels
    ax.set(
        xlabel = "Year-Month-Week",
        ylabel = "Total Weekly Hours",
        title = img_name,
    )
    ax.bar_label(
        bars1,
        fontsize = 14,
    )
    ax.bar_label(
        bars2,
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
