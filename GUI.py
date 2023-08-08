import tkinter as tk
from tkinter import filedialog

def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        file_label.config(text="Selected file: " + file_path)
    else:
        file_label.config(text="No file selected")

# Create the main window
root = tk.Tk()
root.title("File Input Example")

# Create a button to open a file dialog
open_button = tk.Button(root, text="Open File", command=open_file)
open_button.pack(pady=10)

# Create a label to display the selected file path
file_label = tk.Label(root, text="No file selected")
file_label.pack()

# Run the main loop
root.mainloop()
