import csv
from datetime import datetime

def log_error(log_path, file_path, error_message):
    with open(log_path, 'a', newline='', encoding='utf-8') as log_file:
        writer = csv.writer(log_file)
        writer.writerow([datetime.now(), file_path, error_message])
