import os

#add folders source and output
source_folder = '/path/to/source'
output_folder = '/path/to/output'
log_csv_path = '/path/to/conversion_log.csv'
missing_files_txt = '/path/to/missing_files_txt'

word_folder = os.path.join(source_folder, 'docs_word')
word97_folder = os.path.join(source_folder, 'docs_word97')
pdf_folder = os.path.join(source_folder, 'docs_pdf')
ocr_folder = os.path.join(source_folder, 'docs_ocr')
excel_folder = os.path.join(source_folder, 'docs_excel')
others_folder = os.path.join(source_folder,'docs_others')
images_folder = os.path.join(source_folder,'docs_images')
pdf_errors_folder = os.path.join(source_folder,'docs_pdf_errors')
missing_files_txt = os.path.join(source_folder, 'missing_files_txt')

