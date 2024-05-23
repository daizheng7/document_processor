import fitz  # PyMuPDF
from .log_utils import log_error

def extract_text_from_pdf(pdf_path, log_path):
    try:
        doc = fitz.open(pdf_path)
        texts = [page.get_text().strip() for page in doc]
        doc.close()
        return '\n\n'.join(texts)
    except Exception as e:
        log_error(log_path, pdf_path, str(e))
        return ""

def convert_pdf_to_text(pdf_path, output_path, log_path):
    try:
        full_text = extract_text_from_pdf(pdf_path, log_path)
        with open(output_path, 'w', encoding='utf-8') as output_file:
            output_file.write(full_text)
        print(f"Successfully wrote file: {output_path}")
    except Exception as e:
        log_error(log_path, pdf_path, str(e))
        print(f"Failed to write file: {output_path} due to {str(e)}")

def batch_convert_pdf_to_text(pdf_folder, output_folder, log_path):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    with open(log_path, 'w', newline='', encoding='utf-8') as log_file:
        writer = csv.writer(log_file)
        writer.writerow(["Timestamp", "PDF File", "Error Message"])

    for pdf_file in os.listdir(pdf_folder):
        if pdf_file.lower().endswith('.pdf'):
            pdf_path = os.path.join(pdf_folder, pdf_file)
            txt_filename = os.path.splitext(pdf_file)[0] + '.md'
            output_path = os.path.join(output_folder, txt_filename)

            if os.path.exists(output_path):
                print(f"Skipping already converted file '{pdf_file}'.")
                continue

            convert_pdf_to_text(pdf_path, output_path, log_path)
            print(f"Converted '{pdf_file}' to text format as '{txt_filename}'.")
