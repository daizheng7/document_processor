import os
import pytesseract
from pdf2image import convert_from_path
from .log_utils import log_error

def pdf_to_text(pdf_file):
    try:
        images = convert_from_path(pdf_file)
        text = []
        for image in images:
            text.append(pytesseract.image_to_string(image))
        return "\n\n".join(text)
    except Exception as e:
        raise Exception(f"Error during OCR of {pdf_file}: {e}")

def process_ocr_folder(input_folder, output_folder, log_path):
    for pdf_file in os.listdir(input_folder):
        if pdf_file.endswith('.pdf'):
            input_path = os.path.join(input_folder, pdf_file)
            output_path = os.path.join(output_folder, os.path.splitext(pdf_file)[0] + '.txt')
            try:
                text = pdf_to_text(input_path)
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(text)
                print(f"Converted {input_path} to text.")
            except Exception as e:
                log_error(log_path, input_path, str(e))
                print(f"Error processing file '{input_path}': {e}")
