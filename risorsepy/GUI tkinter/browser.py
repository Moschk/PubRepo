from tkinter import *
 
root = Tk()
root.geometry("1060x600")
frame = Frame(root, background="yellow")
frame.pack()
 
leftframe = Frame(root, background='red')
leftframe.pack(side=LEFT)
topframe = Frame(root, background='blue')
topframe.pack(side=TOP)

button1 = Button(leftframe, text = "Button1")
button1.pack(padx = 3, pady = 3)

text_bar = Text(topframe)
text_bar.pack(padx=3, pady=3)

root.title("Browser")
root.mainloop()