import pandas as pd
from datetime import date, timedelta, datetime
from plotting.plot import transform_data, plot_static
import os

# os.getcwd()
# os.chdir('../Time_Management')

def import_data():
    """
    read data from csv
    add new data up to today
    load updated date back to csv
    """
    # load current data
    data = pd.read_csv("data/data2.csv")
    print("Loaded csv with %d rows. Refresh starting ..." % (len(data)))

    # fill up new dates
    max_date = datetime.strptime(data.Date.max(), '%Y-%m-%d').date()
    today = date.today()
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

def main():

    # 1) read and transform data
    input_data = import_data()
    clean_data = transform_data(input_data, 30)

    # 2) plotting
    plot_static(clean_data, "Work", "blue", 3, 6, "work_plot")
    plot_static(clean_data, "Development", "red", 0.5, 2, "dev_plot")
    plot_static(clean_data, "Self-Care", "green", 0, 3, "care_plot")

    # 5) leetcode plot
#     plot_leetcode() # only run at month end to refresh leetcode plot

if __name__ == "__main__":
    main()
