# src/gui/language_editor.py
import json
from pathlib import Path
import tkinter as tk
from tkinter import messagebox

LANG_DIR = Path("src/languages")


class LanguageEditor(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack(fill="both", expand=True)
        self.build_form()

    def build_form(self):
        self.entries = {}

        fields = [
            ("code", "Language Code (EN, DE)"),
            ("name", "Language Name"),
            ("sal_male", "Salutation (Male)"),
            ("sal_female", "Salutation (Female)"),
            ("sal_none", "Salutation (None)"),
            ("formal_before", "Formal Sentence (Before)"),
            ("formal_after", "Formal Sentence (After)"),
            ("closing", "Closing"),
            ("date_format", "Date Format")
        ]

        for i, (key, label) in enumerate(fields):
            tk.Label(self, text=label).grid(row=i, column=0, sticky="w")
            entry = tk.Entry(self, width=50)
            entry.grid(row=i, column=1)
            self.entries[key] = entry

        tk.Button(self, text="Save Language", command=self.save_language)\
            .grid(row=len(fields), column=1, pady=10)

    def save_language(self):
        data = {
            "code": self.entries["code"].get().upper(),
            "name": self.entries["name"].get(),
            "salutation": {
                "male": self.entries["sal_male"].get(),
                "female": self.entries["sal_female"].get(),
                "none": self.entries["sal_none"].get()
            },
            "application_sentence": {
                "formal": {
                    "before": self.entries["formal_before"].get(),
                    "after": self.entries["formal_after"].get()
                }
            },
            "closing": self.entries["closing"].get(),
            "signature_head": "",
            "date_format": self.entries["date_format"].get()
        }

        path = LANG_DIR / f"{data['code'].lower()}.json"
        path.write_text(
            json.dumps(data, indent=2, ensure_ascii=False),
            encoding="utf-8"
        )

        messagebox.showinfo("Saved", f"Language saved to {path}")
