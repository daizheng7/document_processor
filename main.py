from config import settings
from utils.file_utils import move_files
from utils.pdf_utils import batch_convert_pdf_to_text
from utils.word_utils import process_folder, process_word97_folder
from utils.excel_utils import process_excel_folder
from utils.ocr_utils import process_ocr_folder

def main():
    move_files(settings.source_folder)
    
    print("Starting to process Word files...")
    process_folder(settings.word_folder, settings.output_folder)
    print("Finished processing Word files.")
    
    print("Starting to process Excel files...")
    process_excel_folder(settings.excel_folder, settings.output_folder)
    print("Finished processing Excel files.")
    
    print("Starting to process PDF files...")
    batch_convert_pdf_to_text(settings.pdf_folder, settings.output_folder, settings.log_csv_path)
    print("Finished processing PDF files.")
    
    print("Starting to process OCR PDF files...")
    process_ocr_folder(settings.ocr_folder, settings.output_folder)
    print("Finished processing OCR PDF files.")
    
    print("Starting to process Word 97 files...")
    process_word97_folder(settings.word97_folder, settings.output_folder)
    print("Finished processing Word 97 files.")

if __name__ == "__main__":
    main()