import PyPDF2
import os
from datetime import datetime


def extract_text_from_first_page(pdf_path):
    """
    Extract text from the first page of the given PDF file.

    :param pdf_path: Path to the PDF file
    :return: Extracted text from the first page
    """
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            first_page = reader.pages[0]
            text = first_page.extract_text()
            return text
    except Exception as e:
        print(f"Error extracting text: {e}")
        return None


def find_text_after_keyword(text, keyword):
    """
    Find and return text that appears after the specified keyword in the given text.

    :param text: The complete text to search within
    :param keyword: The keyword to search for
    :return: Text following the keyword
    """
    lines = text.split('\n')
    for i, line in enumerate(lines):
        if keyword in line:
            # Check if the keyword is followed by text on the same line
            keyword_index = line.find(keyword) + len(keyword)
            if keyword_index < len(line):
                return line[keyword_index:].strip()
            # Check the next line if the keyword is at the end of the line
            if i + 1 < len(lines):
                return lines[i + 1].strip()
    return None


def find_text_in_same_line(text, keyword):
    """
    Find and return text that appears in the same line after the specified keyword.

    :param text: The complete text to search within
    :param keyword: The keyword to search for
    :return: Text in the same line following the keyword
    """
    lines = text.split('\n')
    for line in lines:
        if keyword in line:
            # Check if the keyword is followed by text on the same line
            keyword_index = line.find(keyword) + len(keyword)
            if keyword_index < len(line):
                return line[keyword_index:].strip()
    return None


def process_extracted_text(extracted_text):
    """
    Process the extracted text to replace slashes with dashes and remove the time part.

    :param extracted_text: The text to process
    :return: Processed text
    """
    # Extract date part and convert it to YYYY-MM-DD format
    date_str = extracted_text.split(' ')[0]
    date_obj = datetime.strptime(date_str, '%d/%m/%Y')
    formatted_date = date_obj.strftime('%Y-%m-%d')
    return formatted_date


def rename_pdf_file(pdf_path, new_name):
    """
    Rename the given PDF file and move it to the 'renombrados' folder.

    :param pdf_path: Path to the PDF file
    :param new_name: New name for the PDF file (without extension)
    """
    directory, old_file_name = os.path.split(pdf_path)
    new_file_name = f"{new_name}.pdf"
    new_file_path = os.path.join(directory, "renombrados", new_file_name)
    try:
        os.makedirs(os.path.join(directory, "renombrados"), exist_ok=True)
        os.rename(pdf_path, new_file_path)
        print(f"File renamed to: {new_file_path}")
    except Exception as e:
        print(f"Error renaming file: {e}")


def process_pdf_files_in_folder(folder_path):
    """
    Process all PDF files in the given folder.

    :param folder_path: Path to the folder containing PDF files
    """
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.pdf'):
            pdf_path = os.path.join(folder_path, file_name)
            extracted_text = extract_text_from_first_page(pdf_path)
            if extracted_text:
                # Find the text following "Fecha de Ejecución"
                date_keyword = "Fecha de Ejecución"
                date_text = find_text_after_keyword(
                    extracted_text, date_keyword)

                # Find the text in the same line as "Referencia Destino"
                ref_keyword = "Referencia Destino: "
                ref_text = find_text_in_same_line(extracted_text, ref_keyword)

                if date_text and ref_text:
                    # Process the extracted date text to format the date
                    formatted_date = process_extracted_text(date_text)
                    # Add prefix and reference to the new name
                    new_name = f"Transferencia_entre_cuentas_{formatted_date}.{ref_text}"
                    rename_pdf_file(pdf_path, new_name)
                else:
                    if not date_text:
                        print(
                            f"Keyword '{date_keyword}' not found in the text of file {file_name}.")
                    if not ref_text:
                        print(
                            f"Keyword '{ref_keyword}' not found in the text of file {file_name}.")
            else:
                print(f"Failed to extract text from the PDF file {file_name}.")


def main():
    folder_path = '.'  # Path to the folder containing PDF files
    process_pdf_files_in_folder(folder_path)


if __name__ == "__main__":
    main()
