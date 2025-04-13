import schedule
import time
import requests

def auto_trigger():
    print("Triggering auto report...")
    response = requests.post('http://localhost:5000/trigger_report', json={})
    print("Triggered report:", response.json())

schedule.every(1).hours.do(auto_trigger)

while True:
    schedule.run_pending()
    time.sleep(60)
