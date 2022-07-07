from tkinter import *
import random 

root = Tk()
root.title("Picnic")
root.geometry("600x600")

label1=Label(root)
label2=Label(root)

list = ["Bottle", "Tiffin", "ID Card", "Chocolates", "Chips", "Tickets", "Hanky"]

label1["text"] = "Listed Items: " + str(list)

def list():
    random_no = random.sample(range(0,6),1)
    label2["text"] = "Put Item Number " + str(random_no) + " in Bag"


btn = Button(root, text="Which Item should I put in the Bag", command = list)
btn.place(relx=0.5, rely = 0.5 , anchor=CENTER)
label1.place(relx=0.5, rely = 0.4 , anchor=CENTER)
label2.place(relx=0.5, rely = 0.6 , anchor=CENTER)


root.mainloop()

