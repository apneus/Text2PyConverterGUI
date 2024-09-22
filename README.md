## Text2PyConverter
Converts text files to Python files

I have a load of sample python code to use as exercises for learning Python and for some reason, they were all .txt files (100s of them)

Perhaps this was in case of an overly zealous security software, who knows, but to change them all was going to take hours. 

So, light bulb moment. And, enter my first real Python script.

Initial code, after much debugging worked fine and converted all the text files to Python files. Then came all the additional functionality.

- Added ability to scan sub folders
- Added a terminal prompt to input path to parent directory
- Added a Gui prompt to enter the parent directory
- Finally, added a confirmation dialogue box for operation completed
- Compiled to executable, just for good measure

Now I know this is simple stuff to most of you, but this is a huge milestone for me and....

You have to start somewhere!

## GUI Added

Key Changes:

- Replaced tkinter with customtkinter (ctk) to change from CLI to GUI.
- A simple window with a button is added, which triggers the folder selection and renaming process when clicked.
- Removed the message box that pops up after the operation.
- Added a status_label at the bottom of the GUI window to display a message like "All .txt files have been renamed to .py." or "No  folder selected. Exiting." after the operation.



