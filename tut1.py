from tkinter import *
ar_root = Tk()

# widthxheight
ar_root.geometry("644x426")
# width, height
ar_root.minsize(300,200)
ar_root.maxsize(1000,900)
#label
lb = Label(text="LABEL IS TEXT WHICH IS DISPLAY ON THE SCREEN OF THE WINDOW")
lb1= Label(text="HELLO EVERYONE THIS IS ARUN AND I LEARN PYTHON GUI TO MAKE A USER INTERFACE WINDOW TO "
                "INTERACT WITH THE WINDOW AND THIS IS COOL ENOUGH FOR DOING THIS ")
lb.pack()
lb1.pack()


ar_root.mainloop()