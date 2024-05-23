import os
import pandas as pd
from .log_utils import log_error

def excel_to_txt(excel_file, output_file):
    try:
        df = pd.read_excel(excel_file)
        with open(output_file, 'w', encoding='utf-8') as f:
            for index, row in df.iterrows():
                row_text = '\t'.join(map(str, row.values))
                f.write(row_text + '\n')
        print(f"Converted {excel_file} to {output_file}")
    except Exception as e:
        raise Exception(f"Error converting {excel_file} to text: {e}")

def process_excel_folder(input_folder, output_folder, log_path):
    for excel_file in os.listdir(input_folder):
        if excel_file.endswith('.xls') or excel_file.endswith('.xlsx'):
            input_path = os.path.join(input_folder, excel_file)
            output_path = os.path.join(output_folder, os.path.splitext(excel_file)[0] + '.txt')
            try:
                excel_to_txt(input_path, output_path)
            except Exception as e:
                log_error(log_path, input_path, str(e))
                print(f"Error processing file '{input_path}': {e}")
