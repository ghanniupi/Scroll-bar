from tkinter import *

root = Tk()

# Create horizontal and vertical scroll bars
x_scrollbar = Scrollbar(root, orient=HORIZONTAL)
y_scrollbar = Scrollbar(root)

# Create a text box with the xscrollcommand property set to the set() method of x_scrollbar and the yscrollcommand property to the set() method of y_scrollbar
text_box = Text(root, wrap=NONE, xscrollcommand=x_scrollbar.set, yscrollcommand=y_scrollbar.set)

# Set the command properties of x_scrollbar and y_scrollbar to the xview() and yview() methods of the text box, respectively
x_scrollbar.config(command=text_box.xview)
y_scrollbar.config(command=text_box.yview)

# Place horizontal scroll bars and text boxes in the main window
x_scrollbar.pack(side=BOTTOM, fill=X)
text_box.pack(side=LEFT, fill=BOTH, expand=True)

# 将纵向滚动条放置在主窗口中的右侧
y_scrollbar.pack(side=RIGHT, fill=Y)

root.mainloop()