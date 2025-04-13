# def generate_report(report_id, store_id=None, start=None, end=None):
from shared_staet import report_status
import pandas as pd
import os
from datetime import datetime
          

    # assume 24x7 for all days

    # try:
    #     store_status_df = pd.read_csv("store_status.csv")
    #     menu_hours_df = pd.read_csv("menu_hours.csv")
    #     timezones_df = pd.read_csv("timezones.csv")


        

    #     if store_id:
    #         store_status_df = store_status_df[store_status_df['store_id'] == int(store_id)]
    #         menu_hours_df = menu_hours_df[menu_hours_df['store_id'] == int(store_id)]
    #         timezones_df = timezones_df[timezones_df['store_id'] == int(store_id)]

    #     if start and end:
    #         store_status_df['timestamp_utc'] = pd.to_datetime(store_status_df['timestamp_utc'])
    #         store_status_df = store_status_df[
    #             (store_status_df['timestamp_utc'] >= pd.to_datetime(start)) &
    #             (store_status_df['timestamp_utc'] <= pd.to_datetime(end))
    #         ]
    #     if timezones_df.empty:
    #      timezone_str = "America/Chicago"

    #     if menu_hours_df.empty:
    #      menu_hours="24/7"

    #      report_df = store_status_df.head(10)  

    #     report_path = os.path.join('reports', f"{report_id}.csv")
    #     report_df.to_csv(report_path, index=False)
    #     report_status[report_id] = 'Complete'

    # except Exception as e:
    #     print("Error:", e)
    #     report_status[report_id] = 'Failed'
def generate_report(report_id, store_id=None, start=None, end=None):
    from shared_staet import report_status
    import pandas as pd
    import os

    try:
        # Simulating report generation
        print(f"Generating report for {report_id}")
        # Assuming report generation logic here
        report_path = os.path.join('reports', f"{report_id}.csv")
        # Simulate saving a report
        report_status[report_id] = 'Complete'
        print(f"Report {report_id} status set to 'Complete'")

    except Exception as e:
        print(f"Error: {e}")
        report_status[report_id] = 'Failed'
        print(f"Report {report_id} status set to 'Failed'")
