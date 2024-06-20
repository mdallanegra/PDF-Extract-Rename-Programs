import os
import tkinter as tk
from tkinter import filedialog, messagebox
import webbrowser

'''Buscar PDFs en una carpeta y listarlos en orden
    para seleccionar uno o todos'''

# import PyPDF2


def listar_pdfs_en_carpeta(ruta_carpeta):
    """
    Lista todos los archivos PDF en la carpeta dada.

    :param ruta_carpeta: Ruta de la carpeta
    :return: Lista de archivos PDF en la carpeta
    """
    archivos_pdf = [archivo for archivo in os.listdir(
        ruta_carpeta) if archivo.lower().endswith('.pdf')]
    return archivos_pdf


class SelectorPDF:
    """
    Una clase que representa un Selector de PDF.

    Atributos:
        root (tk.Tk): La ventana principal de la aplicación.
        ruta_carpeta (tk.StringVar): La variable para almacenar la ruta de la carpeta seleccionada.
        listbox (tk.Listbox): El widget de listbox para mostrar los archivos PDF.

    Métodos:
        __init__(self, root): Inicializa el objeto SelectorPDF.
        buscar_carpeta(self): Abre un cuadro de diálogo para seleccionar una carpeta.
        listar_pdfs(self): Lista los archivos PDF en la carpeta seleccionada.
        abrir_seleccionados(self): Abre los archivos PDF seleccionados.
        abrir_todos(self): Abre todos los archivos PDF en la carpeta seleccionada.
    """

    def __init__(self, root):
        """
        Inicializa el objeto SelectorPDF.

        Args:
            root (tk.Tk): La ventana principal de la aplicación.
        """
        self.root = root
        self.root.title("Selector de PDF")

        self.ruta_carpeta = tk.StringVar()

        tk.Label(root, text="Ruta de la Carpeta:").pack(pady=5)
        tk.Entry(root, textvariable=self.ruta_carpeta, width=50).pack(pady=5)
        tk.Button(root, text="Buscar", command=self.buscar_carpeta).pack(pady=5)
        tk.Button(root, text="Listar PDFs", command=self.listar_pdfs).pack(pady=5)

        self.listbox = tk.Listbox(
            root, selectmode=tk.MULTIPLE, width=50, height=15)
        self.listbox.pack(pady=10)

        tk.Button(root, text="Abrir Seleccionados",
                  command=self.abrir_seleccionados).pack(pady=5)
        tk.Button(root, text="Abrir Todos", command=self.abrir_todos).pack(pady=5)

    def buscar_carpeta(self):
        """
        Abre un cuadro de diálogo para seleccionar una carpeta.
        """
        carpeta_seleccionada = filedialog.askdirectory()
        self.ruta_carpeta.set(carpeta_seleccionada)

    def listar_pdfs(self):
        """
        Lista los archivos PDF en la carpeta seleccionada.
        """
        self.listbox.delete(0, tk.END)
        carpeta = self.ruta_carpeta.get()

        if not os.path.isdir(carpeta):
            messagebox.showerror(
                "Error", "La carpeta seleccionada no existe.")
            return

        archivos_pdf = [f for f in os.listdir(
            carpeta) if f.lower().endswith('.pdf')]

        for pdf in archivos_pdf:
            self.listbox.insert(tk.END, pdf)

        if not archivos_pdf:
            messagebox.showinfo(
                "Información", "No se encontraron archivos PDF en la carpeta seleccionada.")

    def abrir_seleccionados(self):
        """
        Abre los archivos PDF seleccionados.
        """
        indices_seleccionados = self.listbox.curselection()
        carpeta = self.ruta_carpeta.get()

        if not indices_seleccionados:
            messagebox.showwarning("Advertencia", "No se han seleccionado archivos PDF.")
            return

        for indice in indices_seleccionados:
            archivo_pdf = self.listbox.get(indice)
            ruta_pdf = os.path.join(carpeta, archivo_pdf)
            webbrowser.open(ruta_pdf)

    def abrir_todos(self):
        """
        Abre todos los archivos PDF en la carpeta seleccionada.
        """
        carpeta = self.ruta_carpeta.get()
        archivos_pdf = [self.listbox.get(i) for i in range(self.listbox.size())]

        if not archivos_pdf:
            messagebox.showwarning("Advertencia", "No hay archivos PDF para abrir.")
            return

        for archivo_pdf in archivos_pdf:
            ruta_pdf = os.path.join(carpeta, archivo_pdf)
            webbrowser.open(ruta_pdf)


if __name__ == "__main__":
    root = tk.Tk()
    app = SelectorPDF(root)
    root.mainloop()
