import pandas as pd
from datetime import date, timedelta, datetime
import matplotlib.pyplot as plt

def import_data():
    """
    read data from csv
    add new data up to today
    load updated date back to csv
    """
    data = pd.read_csv("data/data2.csv")
    print("Refresh starting ...")

    # fill up new dates
    max_date = datetime.strptime(data.Date.max(), '%Y-%m-%d').date()
    today = date.today()

    while max_date < today:
        max_date = max_date + timedelta(days=1)
        data = data.append(
        {
            "Date" : max_date.strftime("%Y-%m-%d"),
            "Day" : max_date.strftime('%A'),
            "Work" : 0,
            "Development" : 0,
            "Self-Care" : 0,
        }, ignore_index=True,)
    data.to_csv("data/data2.csv", index=False)
    return data

def transform_data(input_data):
    """
    set "Date" as index column
    """
    input_data = pd.read_csv("data/data2.csv")
    input_data.index = pd.to_datetime(input_data.Date) # set date as index
    input_data.sort_index(inplace=True)
    input_data.drop('Date', axis=1, inplace=True)
    print("After tranformed:", input_data.tail(5))
    return input_data


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
        markersize = 3,)

    ax.set(xlabel = "Date",
           ylabel = "Hours",
           title = colname)

    # target line
    plt.axhline(y=target_low, color='r', linestyle='dashed')
    plt.axhline(y=target_high, color='g', linestyle='dashed')
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


def main():

    # 1) read data
    input_data = import_data()

    # 3) data transformation
    data = transform_data(input_data)

    # 4) create plot
    data_10 = data[data.index >= pd.to_datetime(date.today() - timedelta(days=10))].copy() # 10 days
    data_30 = data[data.index >= pd.to_datetime(date.today() - timedelta(days=30))].copy() # 30 days
    data_60 = data[data.index >= pd.to_datetime(date.today() - timedelta(days=60))].copy() # 60 days

    # short term view
    plot_static(data_30, "coding", "red", 0.25, 0.5, "coding")
    plot_static(data_30, "work", "green", 4, 5, "work")
    plot_static(data_30, "Project", "purple", 0.5, 1, "project")

    # long term view
    plot_static(data_10, "Total", "blue", 5, 7, "Total_10days",)
    plot_static(data_30, "Total", "green", 5, 7, "Total_30days",)
    plot_static(data_60, "Total", "red", 5, 7, "Total_60days")

    # 5) leetcode plot
#     plot_leetcode() # only run at month end to refresh leetcode plot

if __name__ == "__main__":
    main()
