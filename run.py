import os
import pandas as pd
import numpy as np
from datetime import date, timedelta, datetime as dt
from plotting.plot import (
    plot_month_trend,
    plot_day_trend,
    plot_stacked_bar,
)


def import_data():
    """
    Read data from a CSV file. Prints summary stats of the current dataset and a
    cute giraffe ASCII art.

    Returns
    -------
    pd.DataFrame
        Current data before the new update.
    """
    file_path = os.getenv("DATA_FILE_PATH", "data/data2.csv")

    try:
        data = pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return pd.DataFrame()
    except pd.errors.EmptyDataError:
        print(f"Error: The file '{file_path}' is empty.")
        return pd.DataFrame()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return pd.DataFrame()

    total_days = len(data)
    years, remaining_days = divmod(total_days, 365)
    months, days = divmod(remaining_days, 30)

    print("This repo started on:", min(data.Date))
    print(f"Loaded CSV with {years} years, {months} months, and {days} days of data.")
    print(f"This process has been maintained for {total_days // 30} months. Good job!")
    print("Refresh starting ...")
    print(
        """\
                                       ._ o o
                                       \\_`-)|_
                                    ,""       "\\"
                                  ,"  ## |   ಠ ಠ.
                                ," ##   ,-\__    `.
                              ,"       /     `--._;)
        """
    )
    return data


def update_data(data):
    """
    Add new data up to today and load updated data back to the CSV file.

    Parameters
    ----------
    data : pd.DataFrame
        Current data before the new update.

    Returns
    -------
    pd.DataFrame
        Updated data with the new entries up to the run date (today).
    """
    max_date = dt.strptime(data.Date.max(), "%Y-%m-%d").date()
    today = date.today()

    if (today - max_date).days > 0:
        print(f"You have {(today - max_date).days} missing days.")

        new_dates = pd.date_range(start=max_date + timedelta(days=1), end=today)
        new_entries = pd.DataFrame({
            "Date": new_dates.strftime("%Y-%m-%d"),
            "Day": new_dates.strftime("%A"),
            "Work": 0,
            "Development": 0,
            "Self-Care": 0,
        })
        data = pd.concat([data, new_entries], ignore_index=True)

    data.fillna(0).to_csv("data/data2.csv", index=False)
    print("Adding new entries up to", data.Date.max())
    return data


def transform_data(
        data,
        weekday_work_exp=5,
        weekday_dev_exp=0.5,
        weekday_care_exp=0.5,
        weekend_work_exp=0.5,
        weekend_dev_exp=0.5,
        weekend_care_exp=2,
):
    """
    Transform the Y-axis value from hours to a performance scale:
    performance = expected hours - actual hours.

    Parameters
    ----------
    data : pd.DataFrame
        Updated data with the new entries.

    Returns
    -------
    pd.DataFrame
        Updated data with 4 new columns:
        Work_Scaled, Dev_Scaled, Care_Scaled, Total.
    """
    data["Total"] = data["Work"] + data["Development"] + data["Self-Care"]

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

    data.Date = pd.to_datetime(data.Date)
    return data

def main():
    input_data = import_data()
    updated_data = update_data(input_data)
    clean_data = transform_data(updated_data)

    print("-----------------------------------")
    print(clean_data[["Date", "Day", "Work", "Development", "Self-Care", "Total"]].tail(5))
    print("-----------------------------------")

    plot_day_trend(clean_data, "Work_Scaled", "blue", "work_plot", 0)
    plot_month_trend(clean_data, "Work", "steelblue", "deepskyblue", "work_plot_monthly")

    plot_day_trend(clean_data, "Dev_Scaled", "red", "dev_plot", 0)
    plot_month_trend(clean_data, "Development", "darkseagreen", "palegreen", "dev_plot_monthly")

    plot_day_trend(clean_data, "Care_Scaled", "green", "care_plot", 0)
    plot_month_trend(clean_data, "Self-Care", "palevioletred", "deeppink", "care_plot_monthly")

    plot_day_trend(clean_data, "Total", "yellow", "total_plot", 5)
    plot_month_trend(clean_data, "Total", "goldenrod", "gold", "total_plot_monthly")

    plot_stacked_bar()


if __name__ == "__main__":
    main()
