import os
import tkinter as tk

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


def display_files_in_folder():
    """
    Display the list of files in a GUI window using tkinter.
    """
    pdf_path = input("Enter the path to the folder: ")
    try:
        files = os.listdir(pdf_path)
        root = tk.Tk()
        root.title("Files in Folder")
        for i, file in enumerate(files, start=1):
            label = tk.Label(root, text=f"{i}. {file}")
            label.pack()
        root.mainloop()
    except Exception as e:
        print(f"Error listing files: {e}")
        return None


if __name__ == "__main__":
    display_files_in_folder()
