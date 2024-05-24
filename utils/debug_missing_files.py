# utils/debug_missing_files.py

import pandas as pd
import os
import urllib.parse
import shutil
from config.settings import ocr_folder, output_folder, missing_files_txt

# Function to get all file paths in a directory recursively
def get_all_file_paths(directory):
    file_paths = []
    for root, _, files in os.walk(directory):
        for file in files:
            file_paths.append(os.path.join(root, file))
    return file_paths

def debug_missing_files():
    # Create the missing_files_txt directory if it does not exist
    os.makedirs(missing_files_txt, exist_ok=True)

    # Get all file paths in docs_folder
    all_docs_file_paths = get_all_file_paths(docs_folder)

    # Get all .md and .txt files in txt_final_folder and strip the .md/.txt extension
    txt_final_files = get_all_file_paths(txt_final_folder)
    txt_final_files_no_ext = [os.path.splitext(f)[0] for f in txt_final_files if f.endswith('.md') or f.endswith('.txt')]

    # Decode URL-encoded characters for accurate comparison
    docs_files_no_ext = [urllib.parse.unquote(os.path.splitext(os.path.basename(f))[0]) for f in all_docs_file_paths]
    txt_final_files_no_ext_decoded = [urllib.parse.unquote(os.path.basename(f)) for f in txt_final_files_no_ext]

    # Known file extensions to strip
    known_extensions = ['.doc', '.docx', '.pdf', '.md', '.txt']

    # Function to strip known extensions from filenames
    def strip_known_extensions(filename, extensions):
        for ext in extensions:
            if filename.endswith(ext):
                return filename[:-len(ext)]
        return filename

    # Strip known extensions from docs filenames
    stripped_docs_files = [strip_known_extensions(f, known_extensions) for f in docs_files_no_ext]

    # Find files in docs_folder that are not in txt_final_folder
    missing_files = [f for f in stripped_docs_files if f not in txt_final_files_no_ext_decoded]

    # Create a list to store the results
    results = []

    # Find and match missing files with their full paths
    for missing_file in missing_files:
        for file_path in all_docs_file_paths:
            decoded_file_path = urllib.parse.unquote(os.path.basename(file_path))
            stripped_file_path = strip_known_extensions(decoded_file_path, known_extensions)
            if stripped_file_path == missing_file:
                results.append({'file_name': missing_file, 'full_path': file_path})

    # Add potential matches to results
    for file in missing_files:
        potential_matches = [f for f in all_docs_file_paths if file in urllib.parse.unquote(f)]
        for match in potential_matches:
            results.append({'file_name': file, 'full_path': match})

    # Convert the results list to a DataFrame
    result_df = pd.DataFrame(results)

    # Save the DataFrame to a CSV file
    result_df.to_csv('missing_files_paths.csv', index=False)

    # Copy files to the missing_files_txt directory
    for index, row in result_df.iterrows():
        src_file_path = row['full_path']
        dst_file_path = os.path.join(missing_files_txt, os.path.basename(src_file_path))
        shutil.copy(src_file_path, dst_file_path)

    print(f"Copied {len(result_df)} files to {missing_files_txt}")
