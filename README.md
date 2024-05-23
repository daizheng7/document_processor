# 📄 Document Processor

## 🚀 Overview

This project automates the organization and text extraction from various document formats to speed up processing. It handles PDFs, Word docs, Excel files, and image-based PDFs requiring OCR.

## ✨ Features

- 📂 **Organizes Files**: Moves files into subfolders based on type.
- 📑 **PDF Processing**: Extracts text from text-based and image-based PDFs.
- 📝 **Word Processing**: Extracts text from .docx and .doc files, including tables.
- 📊 **Excel Processing**: Converts Excel files to text.
- 🔍 **OCR Processing**: Uses OCR to extract text from image-based PDFs.
- 🛠️ **Error Logging**: Logs errors for easy debugging.

## 🛠️ Setup

### Prerequisites

1. Install Python libraries:

    ```bash
    pip install pymupdf python-docx pandas pytesseract pillow pywin32
    ```

2. Install Tesseract OCR from [here](https://github.com/tesseract-ocr/tesseract).

### Configuration

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/daizheng7/document_processor.git
    cd document_processor
    ```

2. **Update Configuration**:

    Edit `config/settings.py` to set your `source_folder` and `output_folder`. This will tell the script where to find the documents and where to save the processed text files.

    ```python
    import os

    source_folder = r'C:\Users\messy_docs'
    output_folder = r'C:\Users\messy_docs_txt'
    log_csv_path = r'C:\Users\messy_docs\conversion_log.csv'

    # Define subfolder paths
    word_folder = os.path.join(source_folder, 'docs_word')
    word97_folder = os.path.join(source_folder, 'docs_word97')
    pdf_folder = os.path.join(source_folder, 'docs_pdf')
    ocr_folder = os.path.join(source_folder, 'docs_ocr')
    excel_folder = os.path.join(source_folder, 'docs_excel')
    ```

## ▶️ What the Script Does

1. **Move Files**: Organizes files into subfolders within the source directory based on their type (e.g., PDF, Word, Excel).

2. **Process Documents**:
    - **Word Docs**: Extracts text from .docx and .doc files, including tables, and saves them as text files.
    - **Excel Files**: Converts Excel files (.xls, .xlsx) to text files.
    - **PDFs**: Extracts text from text-based PDFs and uses OCR for image-based PDFs.

3. **Batch Processing**: Processes all documents in the specified folders in batches, making it efficient for large numbers of files.

4. **Error Logging**: Logs any errors encountered during processing to a CSV file for easy troubleshooting.

## 🔧 Functions

### `main.py`

- `move_files`: Organizes files into subfolders.
- `process_folder`: Processes .docx files.
- `process_excel_folder`: Processes Excel files.
- `batch_convert_pdf_to_text`: Processes PDFs.
- `process_ocr_folder`: Processes image-based PDFs.
- `process_word97_folder`: Processes .doc files.

### `utils/file_utils.py`

- `move_files`: Moves files to subfolders.
- `is_pdf_image_based`: Checks if a PDF is image-based.

### `utils/pdf_utils.py`

- `extract_text_from_pdf`: Extracts text from PDFs.
- `convert_pdf_to_text`: Converts PDFs to text.
- `batch_convert_pdf_to_text`: Batch processes PDFs.

### `utils/word_utils.py`

- `process_document`: Extracts text from .docx files.
- `save_text`: Saves text to a file.
- `process_folder`: Processes all .docx files.
- `extract_text_from_word_97`: Extracts text from .doc files.
- `process_word97_folder`: Batch processes .doc files.

### `utils/excel_utils.py`

- `excel_to_txt`: Converts Excel files to text.
- `process_excel_folder`: Batch processes Excel files.

### `utils/ocr_utils.py`

- `pdf_to_text`: Uses OCR to extract text from PDFs.
- `process_ocr_folder`: Batch processes image-based PDFs.

### `utils/log_utils.py`

- `log_error`: Logs errors to a CSV file.

## 🛠️ Modular Design

The project is designed to be modular, with each type of document processing handled by a specific utility module. This makes it easy to maintain and extend. You can add new processing functions or modify existing ones without affecting the rest of the project.

## 🔮 Future Plans

1. **Improve OCR for PDF Files**: Enhance the OCR processing to better handle complex PDF layouts and improve text extraction accuracy.
2. **Support for Additional File Types**: Extend support to other file types such as images, HTML, and more.
3. **Metadata Extraction**: Add functionality to extract and process metadata from documents.
4. **Misnamed file types**: Add support for mislabelled files to rename and convert. 
