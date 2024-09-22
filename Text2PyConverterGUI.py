import os
import customtkinter as ctk
from tkinter import filedialog

# Function to perform file renaming
def rename_txt_to_py():
    # Open dialog to select folder
    parent_folder_path = filedialog.askdirectory(title="Select the parent folder")

    # Check if a folder was selected
    if not parent_folder_path:
        status_label.configure(text="No folder selected. Exiting.")
        # Refresh GUI
        app.update_idletasks()  
    else:
        # Step through all files and directories within the parent folder
        for dirpath, dirnames, filenames in os.walk(parent_folder_path):
            # Iterate over all files in the current directory
            for filename in filenames:
                # Check if file has a .txt extension
                if filename.endswith('.txt'):
                    # Define full path to current .txt file
                    txt_file_path = os.path.join(dirpath, filename)
                    # Define new file path with a .py extension
                    py_file_path = os.path.join(dirpath, filename[:-4] + '.py')
                    # Rename file from .txt to .py
                    os.rename(txt_file_path, py_file_path)

        # Update the status message at the bottom of the GUI
        status_label.configure(text="All .txt files have been renamed to .py.")
        app.update_idletasks()  # Refresh GUI to show the updated message

# Initialize customtkinter window
app = ctk.CTk()
app.title("Text to Python Converter")
app.geometry("400x200")

# Set appearance mode to 'dark'
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")  # You can choose other color themes as well

# Create button to trigger renaming operation
button = ctk.CTkButton(app, text="Select Folder and Convert", command=rename_txt_to_py)
button.pack(pady=40)

# Label to display the operation status
status_label = ctk.CTkLabel(app, text="")
status_label.pack(side="bottom", pady=20)

# Run the GUI application
app.mainloop()
