# from tkinter import *

# root = Tk()
# root.title("Games");
# # width x height
# root.geometry("800x600")
# # width, height
# root.minsize(200, 200)
# Label(text="Welcome!").pack()
# Label(text="Select game you want to play:", pady=10).pack()
# Label(text="Gotham City Invaders", pady=10, relief=RAISED).pack()
# Label(text="Tic Tac Toe", pady=10, relief=RAISED).pack()


# root.mainloop()

# from tkinter import *
# import sys

# root =Tk()
# root.geometry("655x333")

# gci_username = ""

# def run_gci():
#     import menu
#     sys.exit()
#     # print("Hello tkinter Buttons")

# def run_ttc():
#     print("Tic Tac Toe does not exists yet lol")

# frame = Frame(root)
# frame.pack()

# gci = Button(frame, text="Print now", command=run_gci).pack();
# ttc = Button(frame, text="Print dhdiw", command=run_ttc).pack()

# root.mainloop()


# from tkinter import *

# root = Tk()

# def getvals():
#     print("Submitting form")

#     print(f"{namevalue.get(), phonevalue.get(), gendervalue.get(), emergencyvalue.get(), paymentmodevalue.get(), foodservicevalue.get()} ")



#     with open("records.txt", "a") as f:
#         f.write(f"{namevalue.get(), phonevalue.get(), gendervalue.get(), emergencyvalue.get(), paymentmodevalue.get(), foodservicevalue.get()}\n ")



# root.geometry("644x344")
# #Heading
# Label(root, text="Welcome to Harry Travels", font="comicsansms 13 bold", pady=15).grid(row=0, column=3)

# #Text for our form
# name = Label(root, text="Name")
# phone = Label(root, text="Phone")
# gender = Label(root, text="Gender")
# emergency = Label(root, text="Emergency Contact")
# paymentmode = Label(root, text="Payment Mode")

# #Pack text for our form
# name.grid(row=1, column=2)
# phone.grid(row=2, column=2)
# gender.grid(row=3, column=2)
# emergency.grid(row=4, column=2)
# paymentmode.grid(row=5, column=2)

# # Tkinter variable for storing entries
# namevalue = StringVar()
# phonevalue = StringVar()
# gendervalue = StringVar()
# emergencyvalue = StringVar()
# paymentmodevalue = StringVar()
# foodservicevalue = IntVar()


# #Entries for our form
# nameentry = Entry(root, textvariable=namevalue)
# phoneentry = Entry(root, textvariable=phonevalue)
# genderentry = Entry(root, textvariable=gendervalue)
# emergencyentry = Entry(root, textvariable=emergencyvalue)
# paymentmodeentry = Entry(root, textvariable=paymentmodevalue)

# # Packing the Entries
# nameentry.grid(row=1, column=3)
# phoneentry.grid(row=2, column=3)
# genderentry.grid(row=3, column=3)
# emergencyentry.grid(row=4, column=3)
# paymentmodeentry.grid(row=5, column=3)

# #Checkbox & Packing it
# foodservice = Checkbutton(text="Want to prebook your meals?", variable = foodservicevalue)
# foodservice.grid(row=6, column=3)

# #Button & packing it and assigning it a command
# Button(text="Submit to Harry Travels", command=getvals).grid(row=7, column=3)



# root.mainloop()

# xyz = 10;
# i = 10
# while(i >= 7):
#     def mdos():
#         print(xyz)
#     i-=1
#     mdos()


# from tkinter import *
# def key_pressed(event):
#  print(event.char, type(event.char))
#  ch = event.char
#  if(ch.isalpha() == False and ch.isdigit() == FALSE):
#   print("weird key")
#  w=Label(root,text="Key Pressed:"+event.char)
#  w.place(x=70,y=90)

# name =Label(root, text="Enter your Name" , font="Helvetica 16 bold")

# name.grid(row=5, column=2)

# namevalue = StringVar()

# nameentry = Entry(root, textvariable=namevalue)
# nameentry.grid(row=5, column=3)

# root.bind("<Key>",key_pressed)
# root.mainloop()
from tkinter import *
from PIL import Image, ImageTk

mahmudul_root = Tk()

mahmudul_root.geometry("1255x944")
# photo = PhotoImage(file="1.png")

# For Jpg Images

image = Image.open("joker.png")
photo = ImageTk.PhotoImage(image)

varun_label = Label(image=photo)
varun_label.pack()

mahmudul_root.mainloop()