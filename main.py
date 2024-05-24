from config import settings
from utils.file_utils import move_files
from utils.pdf_utils import batch_convert_pdf_to_text
from utils.word_utils import process_folder, process_word97_folder
from utils.excel_utils import process_excel_folder
from utils.ocr_utils import process_ocr_folder
from utils.images_utils import process_images_folder
from utils.debug_missing_files import debug_missing_files
import argparse

def main(run_debug=False):
    move_files(settings.source_folder)
    
    print("Starting to process Word files...")
    process_folder(settings.word_folder, settings.output_folder, settings.log_csv_path)
    print("Finished processing Word files.")
    
    print("Starting to process Excel files...")
    process_excel_folder(settings.excel_folder, settings.output_folder, settings.log_csv_path)
    print("Finished processing Excel files.")
    
    print("Starting to process PDF files...")
    batch_convert_pdf_to_text(settings.pdf_folder, settings.output_folder, settings.log_csv_path)
    print("Finished processing PDF files.")
    
    print("Starting to process OCR PDF files with Tesseract...")
    process_ocr_folder(settings.ocr_folder, settings.output_folder, settings.log_csv_path)
    print("Finished processing OCR PDF files.")
    
    print("Starting to process Word 97 files...")
    process_word97_folder(settings.word97_folder, settings.output_folder, settings.log_csv_path)
    print("Finished processing Word 97 files.")
    
    print("Starting to process Images with Keras-OCR")
    process_images_folder(settings.images_folder, settings.output_folder, settings.log_csv_path)
    print("Finished processing Images.")

    if run_debug:
        print("Running debug_missing_files...")
        debug_missing_files()
        print("Finished running debug_missing_files.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process documents and optionally run debug_missing_files.')
    parser.add_argument('--run_debug', action='store_true', help='Run the debug_missing_files script if specified')
    
    args = parser.parse_args()
    main(args.run_debug)
