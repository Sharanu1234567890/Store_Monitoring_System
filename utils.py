from datetime import datetime, timedelta
import pytz
from shared_staet import report_status
def parse_time_local_to_utc(business_hours_df, timezone_str, range_start, range_end):
    local_timezone = pytz.timezone(timezone_str)
    intervals = []
    
    
    day = range_start
    while day <= range_end:
        weekday = day.weekday()
        hours_today = business_hours_df[business_hours_df['dayOfWeek'] == weekday]
        
        for _, row in hours_today.iterrows():
            start_time = datetime.strptime(row['start_time_local'], "%H:%M:%S").replace(
                year=day.year, month=day.month, day=day.day)
            end_time = datetime.strptime(row['end_time_local'], "%H:%M:%S").replace(
                year=day.year, month=day.month, day=day.day)

            start_utc = local_timezone.localize(start_time).astimezone(pytz.utc)
            end_utc = local_timezone.localize(end_time).astimezone(pytz.utc)

            # check if the interval overlaps with given range
            if end_utc > range_start and start_utc < range_end:
                intervals.append((max(start_utc, range_start), min(end_utc, range_end)))

        day += timedelta(days=1)
    
    return intervals

def interpolate_statuses(status_df, intervals):
    up_minutes = 0
    down_minutes = 0

    for start, end in intervals:
        curr_time = start
        prev_status = 'inactive'

        while curr_time < end:
            next_time = curr_time + timedelta(minutes=1)
            status_in_min = status_df[(status_df['timestamp_utc'] >= curr_time) & 
                                      (status_df['timestamp_utc'] < next_time)]
            
            if not status_in_min.empty:
                prev_status = status_in_min.iloc[0]['status']
            
            if prev_status == 'active':
                up_minutes += 1
            else:
                down_minutes += 1

            curr_time = next_time
    
    return up_minutes, down_minutes
