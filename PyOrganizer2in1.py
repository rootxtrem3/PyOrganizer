import os
import shutil
import platform
from tkinter import Tk, filedialog, Button, Label, messagebox

FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp"],
    "Documents": [".doc", ".docx", ".txt", ".odt", ".rtf", ".epub"],
    "Presentations": [".ppt", ".pptx"],
    "Spreadsheet": [".xls", ".xlsx", ".csv"],
    "PDFs": [".pdf"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv", ".flv", ".wmv"],
    "Audio": [".mp3", ".wav", ".aac", ".flac", ".ogg", ".m4a", ".amr"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2"],
    "Scripts": [".py", ".js", ".jsx", ".html", ".mhtml", ".css", ".java", ".c", ".cpp", ".sh", ".pl", ".rb"],
    "Packages": [".deb", ".rpm", ".pkg", ".appimage", ".exe", ".msi"],
    "OS-Images": [".iso", ".dmg"],
    "Databases": [".db", ".json"],
    "Leavethemtogetf.cked': [".bin"]
    "Others": []
}

def categorize_file(file_name):
    ext = os.path.splitext(file_name)[1].lower()
    for category, extensions in FILE_TYPES.items():
        if ext in extensions:
            return category
    return "Others"

def organize_files(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if not os.path.isfile(file_path):
                continue
            category = categorize_file(file)
            target_folder = os.path.join(directory, category)
            os.makedirs(target_folder, exist_ok=True)
            target_path = os.path.join(target_folder, file)
            counter = 1
            while os.path.exists(target_path):
                base, ext = os.path.splitext(file)
                target_path = os.path.join(target_folder, f"{base}_{counter}{ext}")
                counter += 1
            try:
                shutil.move(file_path, target_path)
            except Exception:
                pass

def select_directory():
    folder = filedialog.askdirectory()
    if folder:
        organize_files(folder)
        messagebox.showinfo("Success", f"Files in '{folder}' have been organized!")

system_name = platform.system()
root = Tk()
root.title(f"{system_name} File Organizer")
root.geometry("400x150")

Label(root, text=f"Organize your files into folders by type ({system_name})", font=("Arial", 12)).pack(pady=10)
Button(root, text="Select Folder", command=select_directory, width=20).pack(pady=20)

root.mainloop()
