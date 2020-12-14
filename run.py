import pandas as pd
import datetime

import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import matplotlib.dates as mdates


def import_data():
    data = pd.read_csv("data/time_sheet.csv")
    print("Refresh starting ...")
    print("The current time sheet has %d rows." % len(data))
    return data 
    
def insert_new_row(lst, data):
    data = data.append(
    {
        "Date" : lst[0],
        "work" : lst[1],
        "ds_project" : lst[2],
        "coding" : lst[3],
        "planning" : lst[4] 
        
    }, ignore_index=True,)
    return data 

def main():
    
    # 1) read data
    input_data = import_data() 
    print(input_data.tail(5))
    
    # 2) add new data
#     input_data = insert_new_row(
#         ["2020-12-11", 5.5, 0, 0, 0], # work, ds_proj, coding, planning 
#         input_data,)
    
    # 2) update data
#     input_data.loc[data["Date"] == "2020-12-07", "work"] = 5

    print(input_data.tail(5))

    # 3) save data 
    input_data["Total"] = input_data["work"] + input_data["ds_project"] + input_data["coding"] + input_data["planning"] 
    print(input_data.tail(5))
    input_data.to_csv("data/time_sheet.csv", index=False)
    
    # 4) create plot 
    data = input_data.copy()
    
    # Initiate the plot 
    fig, ax = plt.subplots()
    ax.plot("Date", "ds_project", data=data)
    ax.plot("Date", "work", data=data)
    ax.plot("Date", "coding", data=data)
    ax.plot("Date", "planning", data=data)
    ax.plot("Date", "Total", data=data)

    # labels and legend 
    ax.set(xlabel='Date', ylabel='Hours', title='Productivity')
    plt.legend()

    # rotate x-axis and set max num of ticks displayed 
    plt.xticks(data.index, rotation=50)
    ax.xaxis.set_major_locator(plt.MaxNLocator(20)) 

    # resize img 
    fig.set_size_inches(18, 5)
    plt.savefig('time_sheet.png')
    

if __name__ == "__main__":
    main()