import os

#add folders source and output
source_folder = r'D:\data\CGIAR\UNFCCC\gef_docs'
output_folder = r'D:\data\CGIAR\UNFCCC\gef_txt_final'
log_csv_path = r'D:\data\CGIAR\UNFCCC\conversion_log_final.csv'


word_folder = os.path.join(source_folder, 'docs_word')
word97_folder = os.path.join(source_folder, 'docs_word97')
pdf_folder = os.path.join(source_folder, 'docs_pdf')
ocr_folder = os.path.join(source_folder, 'docs_ocr')
excel_folder = os.path.join(source_folder, 'docs_excel')