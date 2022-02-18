import pandas as pd
import numpy as np
from datetime import date, timedelta, datetime
from plotting.plot import plot_static, plot_body_mind, plot_self_control
import os

# os.getcwd()
# os.chdir('../Time_Management')

def import_data():
    """
    read data from csv
    count total rows in the current dataset
    """
    # load current data
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
                            ,"     ## /
                          ,"   ##    /


    """)
    return data

def update_data(data):
    """
    add new data up to today
    load updated date back to csv
    """
    # fill up new dates up to the next day of today
    max_date = datetime.strptime(data.Date.max(), '%Y-%m-%d').date()
    today = date.today()

    if (today - max_date).days > 0:
        print("You have %d missing days." % ((today - max_date).days))

    while max_date <= today:
        max_date = max_date + timedelta(days=1)
        data = data.append(
        {
            "Date" : max_date.strftime("%Y-%m-%d"),
            "Day" : max_date.strftime('%A'),
            "Work" : 0,
            "Development" : 0,
            "Self-Care" : 0,
        }, ignore_index=True,)

    # export updated data
    data.fillna(0).to_csv("data/data2.csv", index=False)
    print("Adding new entries up to", data.Date.max())
    return data

def transform_data(
    data,
    days_count=20,
    # current benchmark setting for weekday
    weekday_work_exp=1,
    weekday_dev_exp=0.5,
    weekday_care_exp=2,
    # current benchmark setting for weekend
    weekend_work_exp=1,
    weekend_dev_exp=0.5,
    weekend_care_exp=2,
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
        (data.Date < date.today().strftime("%Y-%m-%d"))].copy()

    # set date as index
    data.Date = pd.to_datetime(data.Date)
    data.set_index("Date", inplace=True)
    return data.sort_index()

def main():
    input_data = import_data()
    updated_data = update_data(input_data)
    clean_data = transform_data(updated_data)
    updated_data

    print("-----------------------------------")
    print(clean_data[["Day", "Work", "Development", "Self-Care", "Total"]].tail(5))
    print("-----------------------------------")

    # 2) plotting performance
    plot_static(clean_data, "Work_Scaled", "blue", "work_plot", 0)
    plot_static(clean_data, "Dev_Scaled", "red", "dev_plot", 0)
    plot_static(clean_data, "Care_Scaled", "green", "care_plot", 0)
    plot_static(clean_data, "Total", "yellow", "total_plot", 2)
    plot_body_mind()
    plot_self_control()

if __name__ == "__main__":
    main()
