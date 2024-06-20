import os
import tkinter as tk
from tkinter import filedialog, messagebox

def list_files_in_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        try:
            files = os.listdir(folder_selected)
            listbox.delete(0, tk.END)  # Clear any existing items in the listbox
            for i, file in enumerate(files, start=1):
                listbox.insert(tk.END, f"{i}. {file}")
        except Exception as e:
            messagebox.showerror("Error", f"Error listing files: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("File Lister")

    frame = tk.Frame(root)
    frame.pack(pady=20)

    list_files_button = tk.Button(frame, text="Select Folder", command=list_files_in_folder)
    list_files_button.pack()

    listbox = tk.Listbox(frame, width=50, height=20)
    listbox.pack(pady=10)

    root.mainloop()
