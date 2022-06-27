import os
import pandas as pd
import numpy as np
from datetime import date, timedelta, datetime as dt
from plotting.plot import (
        plot_month_trend,
        plot_day_trend,
        plot_weekly_stacked_bar,
        plot_weight_trend,
    )

def import_data():
    """Read data from csv. Prints summary stats of the current dataset and a
    cute giraffe ascii art.

    Parameters
    ----------

    Returns
    -------
    data : DataFrame
        Current data before the new update
    """
    data = pd.read_csv("data/data2.csv")

    print("This repo started on:", min(data.Date))
    print("Loaded csv with %d days of data." % (len(data)))
    print("This process been maintained for %d months. Good job!" % (len(data)/30))
    print("Refresh starting ...")
    print("""\
                                       ._ o o
                                       \_`-)|_
                                    ,""       "\"
                                  ,"  ## |   ಠ ಠ.
                                ," ##   ,-\__    `.
                              ,"       /     `--._;)
    """)
    return data

def update_data(data):
    """Add new data up to today and load updated date back to csv.

    Parameters
    ----------
    data : DataFrame
        Current data before the new update

    Returns
    -------
    data : DataFrame
        Updated data with the new entires up to the run date (today)
    """
    # fill up new dates up to the next day of today
    max_date = dt.strptime(data.Date.max(), '%Y-%m-%d').date()
    today = date.today()

    if (today - max_date).days > 0:
        print("You have %d missing days." % ((today - max_date).days))

    while max_date <= today:
        max_date = max_date + timedelta(days=1)
        data = pd.concat([
            data,
            pd.DataFrame([{
                        "Date" : max_date.strftime("%Y-%m-%d"),
                        "Day" : max_date.strftime('%A'), # day of the week
                        "Work" : 0,
                        "Development" : 0,
                        "Self-Care" : 0,}])
            ])

    # export updated data
    data.fillna(0).to_csv("data/data2.csv", index=False)
    print("Adding new entries up to", data.Date.max())
    return data

def transform_data(
    data,
    # current benchmark setting for weekday
    weekday_work_exp=0.5,
    weekday_dev_exp=0.5,
    weekday_care_exp=0.5,
    # current benchmark setting for weekend
    weekend_work_exp=0.5,
    weekend_dev_exp=0.5,
    weekend_care_exp=0.5,
    ):
    """Transform the Y-axis value from hours to a performance scale:
    performance = expected hours - actual hours

    Parameters
    ----------
    data : DataFrame
        Updated data with the new entires

    Returns
    -------
    data : DataFrame
        Updated data with 4 new columns:
        Work_Scaled, Dev_Scaled, Care_Scaled, Total
    """
    data["Total"] = data["Work"] + data["Development"] + data["Self-Care"]

    # scaled metrics
    data["Work_Scaled"] = np.where(
        (data["Day"] == "Saturday") | (data["Day"] == "Sunday"),
    data["Work"] - weekend_work_exp,
    data["Work"] - weekday_work_exp,
    )

    data["Dev_Scaled"] = np.where(
        (data["Day"] == "Saturday") | (data["Day"] == "Sunday"),
    data["Development"] - weekend_dev_exp,
    data["Development"] - weekday_dev_exp,
    )

    data["Care_Scaled"] = np.where(
        (data["Day"] == "Saturday") | (data["Day"] == "Sunday"),
    data["Self-Care"] - weekend_care_exp,
    data["Self-Care"] - weekday_care_exp,
    )

    # set date as datetime obj
    data.Date = pd.to_datetime(data.Date)
    data = data[data.Date < pd.to_datetime(date.today())].copy()
    return data

def main():
    input_data = import_data()
    updated_data = update_data(input_data)
    clean_data = transform_data(updated_data)

    print("-----------------------------------")
    print(clean_data[
            ["Date", "Day", "Work", "Development", "Self-Care", "Total"]
        ].tail(5))
    print("-----------------------------------")

    # 2) plotting
    # colours: https://matplotlib.org/3.5.0/_images/sphx_glr_named_colors_003_2_0x.png

    # Work
    plot_day_trend(clean_data, "Work_Scaled", "blue", "work_plot", 0)
    plot_month_trend(clean_data, "Work", "steelblue", "deepskyblue", "work_plot_monthly")

    # Dev
    plot_day_trend(clean_data, "Dev_Scaled", "red", "dev_plot", 0)
    plot_month_trend(clean_data, "Development", "darkseagreen", "palegreen", "dev_plot_monthly")

    # Care
    plot_day_trend(clean_data, "Care_Scaled", "green", "care_plot", 0)
    plot_month_trend(clean_data, "Self-Care", "palevioletred", "deeppink", "care_plot_monthly")

    # Total
    plot_day_trend(clean_data, "Total", "yellow", "total_plot", 1.5) # fix num
    plot_month_trend(clean_data, "Total", "goldenrod", "gold", "total_plot_monthly")

    # Others
    plot_weekly_stacked_bar()
    plot_weight_trend()

if __name__ == "__main__":
    main()
