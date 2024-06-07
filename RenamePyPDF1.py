import PyPDF2
import os


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


def rename_pdf_file(pdf_path, new_name):
    """
    Rename the given PDF file.

    :param pdf_path: Path to the PDF file
    :param new_name: New name for the PDF file (without extension)
    """
    directory, old_file_name = os.path.split(pdf_path)
    file_extension = os.path.splitext(old_file_name)[1]
    new_file_path = os.path.join(directory, f"{new_name}{file_extension}")
    try:
        os.rename(pdf_path, new_file_path)
        print(f"File renamed to: {new_file_path}")
    except Exception as e:
        print(f"Error renaming file: {e}")


def main():
    pdf_path = 'example.pdf'  # Path to your PDF file
    extracted_text = extract_text_from_first_page(pdf_path)
    if extracted_text:
        # Use first line and limit to 50 characters
        new_name = extracted_text.strip().split('\n')[0][:50]
        rename_pdf_file(pdf_path, new_name)
    else:
        print("Failed to extract text from the PDF.")


if __name__ == "__main__":
    main()
