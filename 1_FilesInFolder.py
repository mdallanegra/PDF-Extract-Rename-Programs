import os


def list_files_in_folder():
    """
    List all files in the given folder. 
    """
    pdf_path = input("Enter the path to the folder: ")
    try:
        files = os.listdir(pdf_path)
        for i, file in enumerate(files, start=1):
            print(f"{i}. {file}")
    except Exception as e:
        print(f"Error listing files: {e}")
        return None

if __name__ == "__main__":
    list_files_in_folder()
