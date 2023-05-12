from tkinter import *

root = Tk()

# Create a vertical scroll bar
scrollbar = Scrollbar(root)

# Create a text box and set the yscrollcommand property to the set() method of the scrollbar
text_box = Text(root, wrap=WORD, yscrollcommand=scrollbar.set)

# Set the command property of the scrollbar to the yview() method of the text box
scrollbar.config(command=text_box.yview)

# Place scroll bars and text boxes in the main window
scrollbar.pack(side=RIGHT, fill=Y)
text_box.pack(side=LEFT, fill=BOTH, expand=True)

root.mainloop()