import os
import shutil
import csv
from .log_utils import log_error

def move_files(source_folder):
    dest_folders = {
        'pdf': os.path.join(source_folder, 'docs_pdf'),
        'doc': os.path.join(source_folder, 'docs_word97'),
        'docx': os.path.join(source_folder, 'docs_word'),
        'ocr': os.path.join(source_folder, 'docs_ocr'),
        'error': os.path.join(source_folder, 'pdf_errors'),
        'excel': os.path.join(source_folder, 'docs_excel'),
        'images': os.path.join(source_folder, 'docs_images'),
        'others': os.path.join(source_folder, 'others')
    }

    error_log_path = os.path.join(source_folder, 'error_log.csv')

    if not os.path.exists(error_log_path):
        with open(error_log_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Timestamp', 'File Path', 'Error Message'])

    for folder in dest_folders.values():
        os.makedirs(folder, exist_ok=True)

    for root, dirs, files in os.walk(source_folder):
        for filename in files:
            file_path = os.path.join(root, filename)
            actual_type = filename.split('.')[-1].lower()
            dest_file_path = ''

            try:
                if actual_type == 'pdf':
                    pdf_type = is_pdf_image_based(file_path)
                    if pdf_type is None:
                        dest_file_path = os.path.join(dest_folders['error'], os.path.basename(file_path))
                    elif pdf_type:
                        dest_file_path = os.path.join(dest_folders['ocr'], os.path.basename(file_path))
                    else:
                        dest_file_path = os.path.join(dest_folders['pdf'], os.path.basename(file_path))
                elif actual_type in ['xls', 'xlsx', 'csv']:
                    dest_file_path = os.path.join(dest_folders['excel'], os.path.basename(file_path))
                elif actual_type in ['jpg', 'jpeg', 'png', 'gif']:
                    dest_file_path = os.path.join(dest_folders['images'], os.path.basename(file_path))
                elif actual_type in dest_folders:
                    dest_file_path = os.path.join(dest_folders[actual_type], os.path.basename(file_path))
                else:
                    dest_file_path = os.path.join(dest_folders['others'], os.path.basename(file_path))

                if not os.path.exists(dest_file_path):
                    shutil.move(file_path, dest_file_path)
                    print(f'Moved: {file_path} to {dest_file_path}')
                else:
                    print(f'File already exists, skipping: {dest_file_path}')
            except Exception as e:
                error_message = f"Failed to process file: {file_path}. Error: {e}"
                print(error_message)
                log_error(error_log_path, file_path, str(e))
                error_file_path = os.path.join(dest_folders['error'], os.path.basename(file_path))
                if not os.path.exists(error_file_path):
                    shutil.move(file_path, error_file_path)
                    print(f'Moved: {file_path} to {dest_folders["error"]} due to processing error.')
                else:
                    print(f'Error file already exists, skipping move: {error_file_path}')
