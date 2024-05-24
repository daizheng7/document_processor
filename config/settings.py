import os

#add folders source and output
source_folder = r'D:\data\CGIAR\UNFCCC\gef_docs\gef_docs\docs_word97'
output_folder = r'D:\data\CGIAR\UNFCCC\gef_txt_old_word'
log_csv_path = r'C:\Users\david\OneDrive\Desktop\CSSS\conversion_log_final.csv'


word_folder = os.path.join(source_folder, 'docs_word')
word97_folder = os.path.join(source_folder, 'docs_word97')
pdf_folder = os.path.join(source_folder, 'docs_pdf')
ocr_folder = os.path.join(source_folder, 'docs_ocr')
excel_folder = os.path.join(source_folder, 'docs_excel')
others_folder = os.path.join(source_folder,'docs_others')
images_folder = os.path.join(source_folder,'docs_images')
pdf_errors_folder = os.path.join(source_folder,'docs_pdf_errors')

