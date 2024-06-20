'''Look for PDFs in Folder and list them in order
    to select one name or all of them'''

import PyPDF2
import os
import tkinter as tk
from tkinter import filedialog, messagebox
import webbrowser


def list_pdfs_in_folder(folder_path):
    """
    List all PDF files in the given folder.

    :param folder_path: Path to the folder
    :return: List of PDF files in the folder
    """
    pdf_files = [file for file in os.listdir(
        folder_path) if file.lower().endswith('.pdf')]
    return pdf_files


class PDFSelector:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Selector")

        self.folder_path = tk.StringVar()

        tk.Label(root, text="Folder Path:").pack(pady=5)
        tk.Entry(root, textvariable=self.folder_path, width=50).pack(pady=5)
        tk.Button(root, text="Browse", command=self.browse_folder).pack(pady=5)
        tk.Button(root, text="List PDFs", command=self.list_pdfs).pack(pady=5)

        self.listbox = tk.Listbox(
            root, selectmode=tk.MULTIPLE, width=50, height=15)
        self.listbox.pack(pady=10)

        tk.Button(root, text="Open Selected",
                  command=self.open_selected).pack(pady=5)
        tk.Button(root, text="Open All", command=self.open_all).pack(pady=5)

    def browse_folder(self):
        folder_selected = filedialog.askdirectory()
        self.folder_path.set(folder_selected)

    def list_pdfs(self):
        self.listbox.delete(0, tk.END)
        folder = self.folder_path.get()

        if not os.path.isdir(folder):
            messagebox.showerror(
                "Error", "The selected folder does not exist.")
            return

        pdf_files = [f for f in os.listdir(
            folder) if f.lower().endswith('.pdf')]

        for pdf in pdf_files:
            self.listbox.insert(tk.END, pdf)

        if not pdf_files:
            messagebox.showinfo(
                "Info", "No PDF files found in the selected folder.")

    def open_selected(self):
        selected_indices = self.listbox.curselection()
        folder = self.folder_path.get()

        if not selected_indices:
            messagebox.showwarning("Warning", "No PDF files selected.")
            return

        for index in selected_indices:
            pdf_file = self.listbox.get(index)
            pdf_path = os.path.join(folder, pdf_file)
            webbrowser.open(pdf_path)

    def open_all(self):
        folder = self.folder_path.get()
        pdf_files = [self.listbox.get(i) for i in range(self.listbox.size())]

        if not pdf_files:
            messagebox.showwarning("Warning", "No PDF files to open.")
            return

        for pdf_file in pdf_files:
            pdf_path = os.path.join(folder, pdf_file)
            webbrowser.open(pdf_path)


if __name__ == "__main__":
    root = tk.Tk()
    app = PDFSelector(root)
    root.mainloop()
