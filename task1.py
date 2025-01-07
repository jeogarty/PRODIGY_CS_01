import tkinter as tk
from tkinter import messagebox, font


def caesar_cipher(text, shift, mode='encrypt'):

    if mode == 'decrypt':
        shift = -shift

    result = ''

    for char in text:
        if char.isalpha():
            # Determine ASCII offset based on uppercase or lowercase
            ascii_offset = 65 if char.isupper() else 97
            # Perform the shift and wrap around using modulo 26
            shifted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            result += shifted_char
        else:
            # Non-alphabetic characters remain unchanged
            result += char

    return result


def handle_cipher():
    text = text_memo.get("1.0", tk.END).strip()
    try:
        shift = int(entry_shift.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Shift value must be an integer.")
        return

    mode = mode_var.get()
    result = caesar_cipher(text, shift, mode)
    result_memo.delete("1.0", tk.END)
    result_memo.insert("1.0", result)


def copy_to_clipboard():
    result_text = result_memo.get("1.0", tk.END).strip()
    root.clipboard_clear()
    root.clipboard_append(result_text)
    root.update()  # Keeps the clipboard data available after the app is closed
    messagebox.showinfo("Copied", "Result copied to clipboard!")


def adjust_font():
    selected_font = font_family_var.get()
    selected_size = font_size_var.get()
    try:
        selected_size = int(selected_size)
    except ValueError:
        messagebox.showerror("Invalid Input", "Font size must be an integer.")
        return

    new_font = font.Font(family=selected_font, size=selected_size)
    text_memo.configure(font=new_font)
    result_memo.configure(font=new_font)


def create_gui():
    global root
    root = tk.Tk()
    root.title("Caesar Cipher Encrypt/Decrypt")

    # Configure row and column weights
    root.rowconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)

    # Input text label and memo
    tk.Label(root, text="Enter the message:").grid(row=0, column=0, padx=10, pady=5, sticky="nw")
    global text_memo
    text_memo = tk.Text(root, width=40, height=5)
    text_memo.grid(row=0, column=1, padx=10, pady=5, sticky="nsew")

    # Shift value label and entry
    tk.Label(root, text="Enter the shift value:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
    global entry_shift
    entry_shift = tk.Entry(root, width=10)
    entry_shift.grid(row=1, column=1, padx=10, pady=5, sticky="w")

    # Mode selection
    global mode_var
    mode_var = tk.StringVar(value="encrypt")
    tk.Radiobutton(root, text="Encrypt", variable=mode_var, value="encrypt").grid(row=2, column=0, padx=10, pady=5,
                                                                                  sticky="w")
    tk.Radiobutton(root, text="Decrypt", variable=mode_var, value="decrypt").grid(row=2, column=1, padx=10, pady=5,
                                                                                  sticky="w")

    # Cipher button
    tk.Button(root, text="Run", command=handle_cipher).grid(row=3, column=0, columnspan=2, pady=10, sticky="ew")

    # Output memo
    tk.Label(root, text="Result:").grid(row=4, column=0, padx=10, pady=5, sticky="nw")
    global result_memo
    result_memo = tk.Text(root, width=40, height=5, state="normal")
    result_memo.grid(row=4, column=1, padx=10, pady=5, sticky="nsew")

    # Add scrollbar to the result memo
    result_scrollbar = tk.Scrollbar(root, command=result_memo.yview)
    result_scrollbar.grid(row=4, column=2, sticky="ns")
    result_memo.configure(yscrollcommand=result_scrollbar.set)

    # Copy button
    tk.Button(root, text="Copy Result", command=copy_to_clipboard).grid(row=5, column=0, columnspan=2, pady=10,
                                                                        sticky="ew")

    # Font adjustment options
    tk.Label(root, text="Font Family:").grid(row=6, column=0, padx=10, pady=5, sticky="w")
    global font_family_var
    font_family_var = tk.StringVar(value="Arial")
    font_family_menu = tk.OptionMenu(root, font_family_var, "Arial", "Courier", "Helvetica", "Times", "Verdana")
    font_family_menu.grid(row=6, column=1, padx=10, pady=5, sticky="w")

    tk.Label(root, text="Font Size:").grid(row=7, column=0, padx=10, pady=5, sticky="w")
    global font_size_var
    font_size_var = tk.StringVar(value="12")
    font_size_entry = tk.Entry(root, textvariable=font_size_var, width=10)
    font_size_entry.grid(row=7, column=1, padx=10, pady=5, sticky="w")

    tk.Button(root, text="Apply Font", command=adjust_font).grid(row=8, column=0, columnspan=2, pady=10, sticky="ew")

    root.mainloop()


if __name__ == "__main__":
    create_gui()
