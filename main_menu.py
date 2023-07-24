from tkinter import *
import sys
import mysql.connector
from PIL import Image, ImageTk

myDb = mysql.connector.connect(user='root', password='ashu3797', host='localhost',port=3306,database='helper',auth_plugin='mysql_native_password')
cur = myDb.cursor();
cur.execute("use Scores")

def main_menu():
    root1 =Tk()
    root1.geometry("800x400")
    def run_gci():
        root1.destroy()
        import game

    def show_hs():
        root2 = Tk()
        Label(root2, text="High Scores:",font="Arial 30 italic", padx=220).grid(row = 0, column= 3);
        cur.execute("SELECT * from scores order by score_value desc limit 10")
        root2.geometry("800x400")
        k = 2
        for i in cur.fetchall():
            Label(root2, text=f"{i[0]} - {i[1]}",font="Arial 20 italic", padx=220).grid(row = k, column= 3);
            k += 1;
    def show_about():
        root2 = Tk()
        Label(root2, text="Developed by Ayush Jindal").grid(row=1, column=4)
        Label(root2, text="Programming Language and Libraries - Python, Pygame, Tkinter").grid(row=2, column=4)
        Label(root2, text="Database Used - MySQL").grid(row=3, column=4)
        Label(root2, text="Thanks for Playing!").grid(row=4, column=4)

    gci = Button(text="Play Gotham City Invaders",font="Arial 30",fg="white", bg="black" ,command=run_gci).grid(row = 2, column = 6, padx=50)
    high = Button(text="High Scores", font="Arial 30",fg="white", bg="black" , command=show_hs).grid(row = 3, column = 6,padx=50)
    about = Button(text="About",font="Arial 30", fg="white", bg="black" ,command=show_about).grid(row = 4, column = 6,padx=50)
    root1.mainloop()

main_menu()