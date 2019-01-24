import random

from tkinter import *

def Lotto_No():
    
    q = random.randint(1,49);
    w = random.randint(1,49);
    e = random.randint(1,49);
    r = random.randint(1,49);
    t = random.randint(1,49);
    x = random.randint(1,49);
    num1.set(q)
    num2.set(w)
    num3.set(e)
    num4.set(r)
    num5.set(t)
    num6.set(x)
    return


Lottery = Tk()
Lottery.geometry('800x360')
frame = Frame(Lottery)
frame.pack()

Lottery.title('Generator Liczb Lotto')

num1=StringVar()
num2=StringVar()
num3=StringVar()
num4=StringVar()
num5=StringVar()
num6=StringVar()


var = StringVar()
var.set("Generator Liczb Lotto")
frame1 = Frame(Lottery)
frame1.pack(side = TOP)

label = Label (frame, textvariable = var, font =("Arial",48), width = 24)
label.pack(side = TOP)

label2 = Label(frame1, textvariable = "", width = 24)
label2.pack(side = TOP)
label2 = Label(frame1, textvariable = "", width = 24)
label2.pack(side = TOP)

frame2 = Frame(Lottery)
frame2.pack(side = TOP)
txtDisplay=Entry(frame2,textvariable = num1,bd=20,insertwidth=1, font =("Arial",30), justify='center', width=4)
txtDisplay.pack(side = LEFT)
txtDisplay=Entry(frame2,textvariable = num2,bd=20,insertwidth=1, font =("Arial",30), justify='center', width=4)
txtDisplay.pack(side = LEFT)
txtDisplay=Entry(frame2,textvariable = num3,bd=20,insertwidth=1, font =("Arial",30), justify='center', width=4)
txtDisplay.pack(side = LEFT)
txtDisplay=Entry(frame2,textvariable = num4,bd=20,insertwidth=1, font =("Arial",30), justify='center', width=4)
txtDisplay.pack(side = LEFT)
txtDisplay=Entry(frame2,textvariable = num5,bd=20,insertwidth=1, font =("Arial",30), justify='center', width=4)
txtDisplay.pack(side = LEFT)
txtDisplay=Entry(frame2,textvariable = num6,bd=20,insertwidth=1, font =("Arial",30), justify='center', width=4)
txtDisplay.pack(side = LEFT)

frame3 = Frame(Lottery)
frame3.pack(side = TOP)

button1 = Button(frame3, state=DISABLED, text="")
button1.pack(side = TOP)

button1 = Button(frame3,padx=8, width = 18, pady=8, bd=8, font =("Arial",26),text= "Losuj Lidio Losuj :D", bg="black", fg="white", command=Lotto_No)
button1.pack(side = TOP)

Lottery.mainloop()
