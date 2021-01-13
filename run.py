import pandas as pd
from datetime import date,timedelta
import matplotlib.pyplot as plt


def import_data():
    """
    read data from csv
    """
    data = pd.read_csv("data/time_sheet.csv")
    print("Refresh starting ...")
    print("The current time sheet has %d rows." % len(data))
    print(data.tail(5))
    return data 


def insert_new_row(lst, data):
    """
    append new row to existing dataframe
    """
    data = data.append(
    {
        "Date" : lst[0],
        "work" : lst[1],
        "ds_project" : lst[2],
        "coding" : lst[3],
        "planning" : lst[4] 
        
    }, ignore_index=True,)
    return data 


def transform_data(input_data):
    """
    create "Total" column
    save to csv
    set "Date" as index column
    """
    input_data["Total"] = input_data["work"] + input_data["ds_project"] + input_data["coding"] + input_data["planning"] 
    input_data.to_csv("data/time_sheet.csv", index=False)
    
    # combine ds_project and planning
    input_data["Project"] = input_data["ds_project"] + input_data["planning"]
    
    
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
    
    # 2) add new data
#     input_data = insert_new_row(
#         ["2021-01-12", 
#          4.5, # work
#          0.5, # ds_project
#          0, # coding
#          0], # planning 
#         input_data,)
    
#     input_data.loc[
#         (input_data["Date"] == "2021-01-05") & (input_data["ds_project"] == 0), 
#     "ds_project"] = 1 # update col

    # 3) data transformation
    data = transform_data(input_data)
    
    # 4) create plot 
    data_short = data[data.index >= pd.to_datetime(date.today() - timedelta(days=10))].copy() # 10 days
    data_long = data[data.index >= pd.to_datetime(date.today() - timedelta(days=60))].copy() # 60 days 
    
    # short term view 
    plot_static(data_short, "Total", "blue", 5, 7, "Total",)
    plot_static(data_short, "coding", "red", 0.25, 0.5, "coding")
    plot_static(data_short, "Project", "purple", 0.25, 0.5, "project")
    plot_static(data_short, "work", "green", 4, 5, "work")
    
    # long term view
    plot_static(data_long, "Total", "yellow", 5, 7, "Total_60days")
    
    # 5) leetcode plot
#     plot_leetcode() # only run at month end to refresh leetcode plot
    
if __name__ == "__main__":
    main()



    