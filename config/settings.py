import os

#add folders source and output
source_folder = r'C:\Users\david\OneDrive\Desktop\CSSS'
output_folder = r'C:\Users\david\OneDrive\Desktop\CSSS\text'
log_csv_path = r'C:\Users\david\OneDrive\Desktop\CSSS\conversion_log_final.csv'


word_folder = os.path.join(source_folder, 'docs_word')
word97_folder = os.path.join(source_folder, 'docs_word97')
pdf_folder = os.path.join(source_folder, 'docs_pdf')
ocr_folder = os.path.join(source_folder, 'docs_ocr')
excel_folder = os.path.join(source_folder, 'docs_excel')