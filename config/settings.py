import os

#add folders source and output
source_folder = r'C:\Users\messy_docs'
output_folder = r'C:\Users\messy_docs_txt'
log_csv_path = r'C:\Users\messy_docs\conversion_log.csv'
missing_files_txt = r'C:\Users\messy_docs\missing_files_txt'


word_folder = os.path.join(source_folder, 'docs_word')
word97_folder = os.path.join(source_folder, 'docs_word97')
pdf_folder = os.path.join(source_folder, 'docs_pdf')
ocr_folder = os.path.join(source_folder, 'docs_ocr')
excel_folder = os.path.join(source_folder, 'docs_excel')
others_folder = os.path.join(source_folder,'docs_others')
images_folder = os.path.join(source_folder,'docs_images')
pdf_errors_folder = os.path.join(source_folder,'docs_pdf_errors')

