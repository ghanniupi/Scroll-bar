from tkinter import *

root = Tk()

# Create a horizontal scroll bar
scrollbar = Scrollbar(root, orient=HORIZONTAL)

# Create a text box and set the yscrollcommand property to the set() method of the scrollbar
text_box = Text(root, wrap=NONE, xscrollcommand=scrollbar.set)

# Set the command property of the scrollbar to the xview() method of the text box
scrollbar.config(command=text_box.xview)

# Place scroll bars and text boxes in the main window
scrollbar.pack(side=BOTTOM, fill=X)
text_box.pack(fill=BOTH)

root.mainloop()