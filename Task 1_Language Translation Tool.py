# Muhammad Owais Raza Qadri
# Language Translation Tools
import tkinter as tk
from tkinter import ttk, messagebox
from googletrans import Translator
import pyttsx3

# Language dictionary
LANGUAGES = {
    "Auto-Detect": "auto",
    "English": "en",
    "Urdu": "ur",
    "Arabic": "ar",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Chinese": "zh-cn"
}

def translate_text():
    text = input_text.get("1.0", tk.END).strip()
    if not text:
        messagebox.showwarning("Input Error", "Please enter text to translate.")
        return

    source = LANGUAGES[source_lang.get()]
    target = LANGUAGES[target_lang.get()]
    try:
        translator = Translator()
        result = translator.translate(text, src=source, dest=target)
        output_text.config(state=tk.NORMAL)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, result.text)
        output_text.config(state=tk.DISABLED)
    except Exception as e:
        messagebox.showerror("Translation Error", f"Failed to translate:\n{e}")

def copy_to_clipboard():
    translated = output_text.get("1.0", tk.END).strip()
    if translated:
        root.clipboard_clear()
        root.clipboard_append(translated)
        messagebox.showinfo("Copied", "Translated text copied to clipboard!")

def speak_translation():
    translated = output_text.get("1.0", tk.END).strip()
    if translated:
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)
        engine.say(translated)
        engine.runAndWait()

# GUI
root = tk.Tk()
root.title("Free Google Translator (Unofficial)")

tk.Label(root, text="Enter text:").grid(row=0, column=0, sticky="w", padx=10)
input_text = tk.Text(root, height=4, width=50)
input_text.grid(row=1, column=0, columnspan=4, padx=10, pady=5)

tk.Label(root, text="From:").grid(row=2, column=0, sticky="e", padx=10)
source_lang = ttk.Combobox(root, values=list(LANGUAGES.keys()), state="readonly", width=18)
source_lang.current(0)
source_lang.grid(row=2, column=1, sticky="w", padx=5)

tk.Label(root, text="To:").grid(row=2, column=2, sticky="e", padx=10)
target_lang = ttk.Combobox(root, values=list(LANGUAGES.keys())[1:], state="readonly", width=18)
target_lang.current(0)
target_lang.grid(row=2, column=3, sticky="w", padx=5)

translate_btn = tk.Button(root, text="Translate", command=translate_text, width=20, bg="#4CAF50", fg="white")
translate_btn.grid(row=3, column=0, columnspan=4, pady=10)

tk.Label(root, text="Translated text:").grid(row=4, column=0, sticky="w", padx=10)
output_text = tk.Text(root, height=4, width=50, state=tk.DISABLED)
output_text.grid(row=5, column=0, columnspan=4, padx=10, pady=5)

copy_btn = tk.Button(root, text="Copy", command=copy_to_clipboard, width=15)
copy_btn.grid(row=6, column=1, pady=5)

speak_btn = tk.Button(root, text="🔊 Speak", command=speak_translation, width=15)
speak_btn.grid(row=6, column=2, pady=5)

root.mainloop()
