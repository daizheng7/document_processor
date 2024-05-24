# 📄 Document Processor

## 🚀 Overview

This project automates the organization and text extraction from various document formats to speed up processing. It handles PDFs, Word docs, Excel files, and image-based PDFs requiring OCR.

## ✨ Features

- 📂 **Organizes Files**: Moves files into subfolders based on type.
- 📑 **PDF Processing**: Extracts text from text-based and image-based PDFs.
- 📝 **Word Processing**: Extracts text from .docx and .doc files, including tables.
- 📊 **Excel Processing**: Converts Excel files to text.
- 🔍 **OCR Processing**: Uses OCR to extract text from image-based PDFs.
- 🖼️ **Image Processing**: Processes images using Keras-OCR.
- 🛠️ **Error Logging**: Logs errors for easy debugging.
- 🐞 **Debugging**: Identifies and processes missing files.

## 🌟 Project Rationale

In many projects, there's a need to process and extract text from a variety of document types, such as `.docx`, `.doc`, `.pdf`, and `.xlsx` files. While different libraries exist for handling each format individually, there isn't a comprehensive solution that integrates all these functionalities into a single, streamlined pipeline. This project provides a unified approach to organizing and extracting text from diverse document formats.

## 🔍 Use Cases

### 💡 NLP and Text Mining
For Natural Language Processing (NLP) and text mining applications, this project provides a consistent and automated method for extracting text from various document formats. This enables data scientists and analysts to preprocess large text corpora efficiently, facilitating tasks like topic modeling, sentiment analysis, entity recognition, and more.

### 🎓 Academic Research
Researchers often work with a variety of document formats when compiling literature reviews, analyzing data, or organizing references. This project can streamline the process by organizing data and extracting text from different file types, allowing researchers to focus on analysis rather than manual text extraction.

### ⚖️ Legal Document Management
Law firms deal with a plethora of documents in different formats, such as contracts, case files, and court rulings. Automating the text extraction process can significantly reduce the time spent on document review and preparation, enabling legal professionals to work more efficiently.

### 📊 Data Analysis and Reporting
Organizations that handle large volumes of reports, meeting minutes, and other documents can use this project to automate the extraction of relevant data. This facilitates quicker compilation of reports and analysis, leading to more timely and informed decision-making.

### 🗃️ Digital Archiving
Archivists and librarians can use this project to digitize and catalog documents in various formats, making it easier to search and retrieve information from large collections. This is particularly useful for historical documents and records that need to be preserved in digital formats.

## 🛠️ Setup

### Prerequisites

1. Install Python libraries:

    ```bash
    pip install pymupdf python-docx pandas pytesseract pillow pywin32 keras-ocr
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
    images_folder = os.path.join(source_folder, 'docs_images')
    missing_files_txt = os.path.join(source_folder, 'missing_files_txt')
    ```

## ▶️ What the Script Does

1. **Move Files**: Organizes files into subfolders within the source directory based on their type (e.g., PDF, Word, Excel).

2. **Process Documents**:
    - **Word Docs**: Extracts text from .docx and .doc files, including tables, and saves them as text files.
    - **Excel Files**: Converts Excel files (.xls, .xlsx) to text files.
    - **PDFs**: Extracts text from text-based PDFs and uses OCR for image-based PDFs.
    - **Images**: Processes images using Keras-OCR.

3. **Batch Processing**: Processes all documents in the specified folders in batches, making it efficient for large numbers of files.

4. **Error Logging**: Logs any errors encountered during processing to a CSV file for easy troubleshooting.

5. **Debugging**: Identifies and processes missing files to ensure all files are accounted for.

## 🔧 Functions

### `main.py`

- `move_files`: Organizes files into subfolders.
- `process_folder`: Processes .docx files.
- `process_excel_folder`: Processes Excel files.
- `batch_convert_pdf_to_text`: Processes PDFs.
- `process_ocr_folder`: Processes image-based PDFs.
- `process_word97_folder`: Processes .doc files.
- `process_images_folder`: Processes images using Keras-OCR.
- `debug_missing_files`: Identifies and processes missing files.

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

### `utils/images_utils.py`

- `process_images_folder`: Processes images using Keras-OCR.

### `utils/log_utils.py`

- `log_error`: Logs errors to a CSV file.

### `utils/debug_missing_files.py`

- `debug_missing_files`: Identifies and processes missing files to ensure all files are accounted for.

## 🛠️ Contributing

This project is designed with modularity in mind, making it easy to extend and maintain. If you're interested in contributing, here are some ways you can get involved:

1. **Improve OCR for PDF Files**: Enhance the OCR processing to better handle complex PDF layouts and improve text extraction accuracy.
2. **Support for Additional File Types**: Extend support to other file types such as images, HTML, and more.
3. **Metadata Extraction**: Add functionality to extract and process metadata from documents.
4. **Misnamed file types**: Add support for mislabelled file types so that a .pdf file that is actually a .jpeg file will still be processed correctly.
5. **Database Ingestion Pipeline**: Add a pipeline for ingesting the extracted text into a PostgreSQL database to facilitate more advanced querying and analysis of the extracted data.
6. **AWS Integration**: Add integration with AWS services, such as S3 for storage and Lambda for serverless processing, to provide a scalable and cloud-based solution for document processing and text extraction.
