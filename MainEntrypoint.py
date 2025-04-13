from flask import Flask, jsonify, request, send_file
import uuid
import threading
import os
from report_generators import generate_report
from shared_staet import report_status  

app = Flask(__name__)

REPORTS_DIR = 'reports'
os.makedirs(REPORTS_DIR, exist_ok=True)

@app.route('/')
def first():
    return "hello world"


# @app.route('/trigger_report', methods=['POST'])
# def trigger_report():
#     report_id = str(uuid.uuid4())
#     report_status[report_id] = 'Running'

#     thread = threading.Thread(target=generate_report, args=(report_id,))
#     thread.start()

#     return jsonify({'report_id': report_id})
@app.route('/trigger_report', methods=['POST'])
def trigger_report():
    report_id = str(uuid.uuid4())
    report_status[report_id] = 'Running'
    print(f"Report triggered with ID: {report_id}")
    print(f"Current report status: {report_status}")  # Log the status to see if it's being set correctly

    thread = threading.Thread(target=generate_report, args=(report_id,))
    thread.start()

    return jsonify({'report_id': report_id})




# @app.route('/get_report', methods=['GET'])
# def get_report():
#     report_id = request.args.get('report_id')
#     print(f"Requested Report ID: {report_id}") 

    
#     print("Available report IDs:", report_status.keys())
#     print("Requested Report ID:", report_id)
     
#     if not report_id:
#         return jsonify({'error': 'Missing report_id'}), 400

#     status = report_status.get(report_id)

#     print(f"Report Status for {report_id}: {status}")

#     if not status:
#         return jsonify({'error': 'Invalid report_id'}), 404

#     if status != 'Complete':
#      return jsonify({'status': status})


#     report_path = os.path.join(REPORTS_DIR, f'{report_id}.csv')
#     print(f"Report file path: {report_path}")  

#     if not os.path.exists(report_path):
#         return jsonify({'error': 'Report file not found'}), 404

#     return send_file(report_path, as_attachment=True)

@app.route('/get_report', methods=['GET'])
def get_report():
    report_id = request.args.get('report_id')
    print(f"Requested Report ID: {report_id}")
    
    if not report_id:
        return jsonify({'error': 'Missing report_id'}), 400
    
    # Check if the report_id is in the status
    status = report_status.get(report_id)
    print(f"Available report_ids: {list(report_status.keys())}")
    print(f"Report Status for {report_id}: {status}")

    if not status:
        return jsonify({'error': 'Invalid report_id'}), 404

    if status == 'Running':
        return jsonify({'status': 'Running'})

    report_path = os.path.join(REPORTS_DIR, f'{report_id}.csv')
    print(f"Report file path: {report_path}")

    if not os.path.exists(report_path):
        return jsonify({'error': 'Report file not found'}), 404

    return send_file(report_path, as_attachment=True)



if __name__ == '__main__':
    app.run(debug=True)
