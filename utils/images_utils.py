import os
import keras_ocr
from PIL import Image
import pytesseract

def process_images_folder(source_folder):
    # Define the images folder path
    images_folder = os.path.join(source_folder, 'docs_images')

    # Initialize the keras-ocr pipeline
    pipeline = keras_ocr.pipeline.Pipeline()

    for filename in os.listdir(images_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            file_path = os.path.join(images_folder, filename)
            image = keras_ocr.tools.read(file_path)
            
            # Perform OCR using keras-ocr
            prediction_groups = pipeline.recognize([image])
            
            # Extract text from the predictions
            extracted_text = "\n".join(
                [word for prediction in prediction_groups for box, word in prediction]
            )
            
            # Save or process the extracted text
            text_file_path = os.path.splitext(file_path)[0] + '.txt'
            with open(text_file_path, 'w') as text_file:
                text_file.write(extracted_text)
        elif filename.lower().endswith('.pdf'):
            file_path = os.path.join(images_folder, filename)
            # Process PDF with pytesseract (assuming images are extracted from PDF pages)
            pdf_document = fitz.open(file_path)
            for page_num in range(len(pdf_document)):
                page = pdf_document.load_page(page_num)
                pix = page.get_pixmap()
                img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
                text = pytesseract.image_to_string(img)
                # Save or process the extracted text
                text_file_path = os.path.splitext(file_path)[0] + f'_page_{page_num}.txt'
                with open(text_file_path, 'w') as text_file:
                    text_file.write(text)