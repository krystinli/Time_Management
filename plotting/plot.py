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


# def plot_body_mind():
#     """
#     plot body and mind investment
#     (Sub category of of self-care)
#     save it under img/
#     """
#     # workout, meditation, nap
#     data=[["Week 1",1,1,1], # Sunday (Starting Point)
#           ["Week 2",6,2,7], # Jan 10-16, out of 7
#           ["Week 3",3,0,6], # Jan 17-23
#           ["Week 4",1,0,1]] # Jan 24-30
#
#     # convert above data into pd df
#     df=pd.DataFrame(
#         data,
#         columns=["Week of the Month","workout","meditation","nap"])
#
#     df.plot(
#         x = "Week of the Month",
#         y = ["workout", "meditation", "nap"],
#         kind = "bar",
#         figsize = (18,8),
#         title = "Self Care Breakdown Analysis",
#         stacked = True,
#         legend = True,
#         colormap = 'Pastel1'
#     )
#
#     plt.savefig("img/" + "2022_Jan_Tracking" + ".png")
#     print("Generated plot for body_mind.")
