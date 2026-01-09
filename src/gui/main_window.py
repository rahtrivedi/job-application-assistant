import tkinter as tk
from tkinter import ttk
from src.core.language_loader import list_languages, load_language
import json


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Language Editor")
        self.geometry("800x600")

        self.languages = list_languages()
        self.language_map = {
            lang["code"]: lang for lang in self.languages
        }

        self._build_ui()

    def _build_ui(self):
        # Dropdown
        self.lang_var = tk.StringVar()
        codes = list(self.language_map.keys())

        self.dropdown = ttk.Combobox(
            self,
            textvariable=self.lang_var,
            values=codes,
            state="readonly"
        )
        self.dropdown.pack(padx=10, pady=10)
        self.dropdown.bind("<<ComboboxSelected>>", self.on_language_selected)

        # Editor
        self.editor = tk.Text(self, wrap="word")
        self.editor.pack(expand=True, fill="both", padx=10, pady=10)

    def on_language_selected(self, event):
        code = self.lang_var.get()
        lang_data = load_language(code)

        self.editor.delete("1.0", tk.END)
        self.editor.insert(
            tk.END,
            json.dumps(lang_data, indent=2, ensure_ascii=False)
        )
