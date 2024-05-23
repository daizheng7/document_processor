import glob
from docx import Document
from .log_utils import log_error

def process_document(doc_path):
    try:
        doc = Document(doc_path)
        output = []

        for paragraph in doc.paragraphs:
            output.append(paragraph.text + "\n")

        for table in doc.tables:
            output.append("\n[Table Start]\n")
            for row in table.rows:
                row_data = []
                for cell in row.cells:
                    cell_text = cell.text.replace('\n', ' ').strip()
                    row_data.append(cell_text)
                output.append("\t".join(row_data))
            output.append("\n[Table End]\n")

        return "\n".join(output)

    except Exception as e:
        raise Exception(f"Failed to process document: {e}")

def process_folder(input_folder, output_folder, log_path):
    for file_path in glob.glob(f"{input_folder}/*.docx"):
        try:
            output_text = process_document(file_path)
            output_file_path = os.path.join(output_folder, f"{os.path.basename(file_path)}.txt")

            with open(output_file_path, 'w', encoding='utf-8') as f:
                f.write(output_text)
            print(f"Processed and saved: {output_file_path}")

        except Exception as e:
            log_error(log_path, file_path, str(e))
            print(f"Error processing file '{file_path}': {e}")

def extract_text_from_word_97(file_path):
    import win32com.client
    word = win32com.client.Dispatch("Word.Application")
    word.Visible = False
    try:
        doc = word.Documents.Open(file_path)
        text = doc.Content.Text
        doc.Close()
        return text
    except Exception as e:
        raise Exception(f"Failed to process Word 97-2003 document: {e}")
    finally:
        word.Quit()

def process_word97_folder(input_folder, output_folder, log_path):
    for file_path in glob.glob(f"{input_folder}/*.doc"):
        try:
            output_text = extract_text_from_word_97(file_path)
            output_file_path = os.path.join(output_folder, f"{os.path.basename(file_path)}.txt")

            with open(output_file_path, 'w', encoding='utf-8') as f:
                f.write(output_text)
            print(f"Processed and saved: {output_file_path}")

        except Exception as e:
            log_error(log_path, file_path, str(e))
            print(f"Error processing file '{file_path}': {e}")
