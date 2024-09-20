from tkinter import *
from tkinter import filedialog

# Initialize root window
root = Tk()
root.geometry("600x600")
root.title("Notepad")
root.config(bg='lightblue')
root.resizable(False, False)

# Function to save file
def save_file():
    open_file = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    if open_file is None:
        return
    text = str(entry.get(1.0, END))
    open_file.write(text)
    open_file.close()

# Function to open file
def open_file():
    file = filedialog.askopenfile(mode='r', filetypes=[('Text Files', '*.txt')])
    if file is not None:
        content = file.read()
        entry.delete(1.0, END)  # Clear previous text
        entry.insert(INSERT, content)

# Save button
b1 = Button(root, width=20, height=2, bg='#fff', text="Save File", command=save_file)
b1.place(x=100, y=5)

# Open button
b2 = Button(root, width=20, height=2, bg='#fff', text="Open File", command=open_file)
b2.place(x=300, y=5)

# Text entry box
entry = Text(root, height=33, width=72, wrap=WORD)
entry.place(x=10, y=60)

root.mainloop()