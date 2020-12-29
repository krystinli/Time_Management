import pandas as pd
import datetime
import matplotlib.pyplot as plt

def import_data():
    """
    read data from csv
    """
    data = pd.read_csv("data/time_sheet.csv")
    print("Refresh starting ...")
    print("The current time sheet has %d rows." % len(data))
    print(input_data.tail(5))
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
    
    input_data.index = pd.to_datetime(input_data.Date) # set date as index
    input_data.sort_index(inplace=True)
    input_data.drop('Date', axis=1, inplace=True)
    print("After tranformed:", input_data.tail(5))
    return input_data

def plot_static(data, colname, color):
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
    plt.legend()
    plt.savefig("img/" + colname + ".png") 
    print("Generated plot for", colname)

def main():
    
    # 1) read data
    input_data = import_data() 
    
    # 2) add new data
#     input_data = insert_new_row(
#         ["2020-12-28", 0, 0, 0, 0], # work, ds_proj, coding, planning 
#         input_data,)
    
    # input_data.loc[data["Date"] == "2020-12-07", "work"] = 5 # update data

    # 3) data transformation
    data = transform_data(input_data)
    
    # 4) create plot 
    plot_static(data, "Total", "blue")
    plot_static(data, "coding", "red")
    plot_static(data, "ds_project", "yellow")
    plot_static(data, "planning", "purple")
    plot_static(data, "work", "green")
    
if __name__ == "__main__":
    main()



    