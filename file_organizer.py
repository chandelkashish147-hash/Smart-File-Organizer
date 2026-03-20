import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

# File categories
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".avi"]
}

folder_path = ""

# Select folder function
def select_folder():
    global folder_path
    folder_path = filedialog.askdirectory()
    folder_label.config(text=f"Selected Folder:\n{folder_path}")

# Organize files function
def organize_files():

    if folder_path == "":
        messagebox.showwarning("Warning", "Please select a folder first!")
        return

    files = os.listdir(folder_path)

    # Create folders
    for category in file_types.keys():
        category_folder = os.path.join(folder_path, category)
        os.makedirs(category_folder, exist_ok=True)

    # Move files
    for file in files:

        file_path = os.path.join(folder_path, file)

        if os.path.isdir(file_path):
            continue

        file_extension = os.path.splitext(file)[1].lower()

        for category, extensions in file_types.items():
            if file_extension in extensions:

                destination = os.path.join(folder_path, category, file)

                shutil.move(file_path, destination)

    messagebox.showinfo("Success", "All files organized successfully!")

# GUI Window
window = tk.Tk()
window.title("File Organizer Tool")
window.geometry("400x250")
window.config(bg="#f2f2f2")

title = tk.Label(window, text="📂 File Organizer Tool", font=("Arial", 16, "bold"), bg="#f2f2f2")
title.pack(pady=10)

select_btn = tk.Button(window, text="Select Folder", command=select_folder, bg="#4CAF50", fg="white", width=20)
select_btn.pack(pady=10)

folder_label = tk.Label(window, text="No folder selected", bg="#f2f2f2")
folder_label.pack(pady=5)

organize_btn = tk.Button(window, text="Organize Files", command=organize_files, bg="#2196F3", fg="white", width=20)
organize_btn.pack(pady=20)

window.mainloop()