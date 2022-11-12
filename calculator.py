from tkinter import *
import tkinter.messagebox as tmsg
from PIL import Image,ImageTk
root=Tk()
root.geometry("265x385")
root.maxsize(height=385,width=265)
root.title("Nikhil\'calculator")
root.configure(bg="slate gray")
# Functions
def str_c(event):
        global va
        text=event.widget.cget("text")
        if text=="C":
                va.set("")
        elif text=="<X":
                st=va.get()                        
                # print(type(st))
                st=st[:-1]
                va.set(st)
        elif text=="=":
                try:
                        r=eval(va.get())
                        va.set(r)

                except :
                        tmsg.showerror("Warning","Entered value is't numerical\nplease enter numerical values only")
                        va.set("")
                        
                        
        elif text=="Exit":
                exit()
        else:
                va.set(va.get()+text)
                # txt.update()


va=StringVar()
va.set("")
f1=Frame(bg="white",width=241,height=80).place(x=10,y=20)
txt=Entry(textvar=va,width=17,font=("bold",19),justify=RIGHT,relief=FLAT).place(x=10,y=90)
b1=Button(text="Exit",bg="white",height=2,width=5,relief=RIDGE,font=("bold",14))
b1.place(y=131,x=10)
b1.bind("<Button-1>",str_c)
b2=Button(text="C",height=2,bg="white",width=5,relief=RIDGE,font=("bold",14))
b2.place(y=131,x=70)
b2.bind("<Button-1>",str_c)

b3=Button(text="<X",height=2,width=5,bg="White",relief=RIDGE,font=("bold",14))
b3.place(y=131,x=130)
b3.bind("<Button-1>",str_c)

b16=Button(text="/",height=2,width=5,bg="White",relief=RIDGE,font=("bold",14))
b16.place(y=131,x=190)
b16.bind("<Button-1>",str_c)

b4=Button(text="7",height=2,width=5,bg="white",relief=RIDGE,font=("bold",14))
b4.place(y=176,x=10)
b4.bind("<Button-1>",str_c)

b5=Button(text="8",height=2,width=5,bg="white",relief=RIDGE,font=("bold",14))
b5.place(y=176,x=70)
b5.bind("<Button-1>",str_c)

b6=Button(text="9",height=2,width=5,bg="White",relief=RIDGE,font=("bold",14))
b6.place(y=176,x=130)
b6.bind("<Button-1>",str_c)

b17=Button(text="*",height=2,width=5,bg="White",relief=RIDGE,font=("bold",14))
b17.place(y=176,x=190)
b17.bind("<Button-1>",str_c)

b7= Button(text="4",height=2,width=5,bg="White",relief=RIDGE,font=("bold",14))
b7.place(y=221,x=10)
b7.bind("<Button-1>",str_c)

b8=Button(text="5",height=2,width=5,bg="White",relief=RIDGE,font=("bold",14))
b8.place(y=221,x=70)
b8.bind("<Button-1>",str_c)

b9=Button(text="6",height=2,width=5,bg="white",relief=RIDGE,font=("bold",14))
b9.place(y=221,x=130)
b9.bind("<Button-1>",str_c)

b18=Button(text="+",height=2,width=5,bg="white",relief=RIDGE,font=("bold",14))
b18.place(y=221,x=190)
b18.bind("<Button-1>",str_c)

b10=Button(text="1",height=2,width=5,bg="white",relief=RIDGE,font=("bold",14))
b10.place(y=266,x=10)
b10.bind("<Button-1>",str_c)

b11=Button(text="2",height=2,width=5,bg="white",relief=RIDGE,font=("bold",14))
b11.place(y=266,x=70)
b11.bind("<Button-1>",str_c)

b12=Button(text="3",height=2,width=5,bg="white",relief=RIDGE,font=("bold",14))
b12.place(y=266,x=130)
b12.bind("<Button-1>",str_c)

b19=Button(text="-",height=2,width=5,bg="white",relief=RIDGE,font=("bold",14))
b19.place(y=266,x=190)
b19.bind("<Button-1>",str_c)

b13=Button(text="%",height=2,width=5,bg="White",relief=RIDGE,font=("bold",14))
b13.place(y=311,x=10)
b13.bind("<Button-1>",str_c)

b14=Button(text="0",height=2,bg="white",width=5,relief=RIDGE,font=("bold",14))
b14.place(y=311,x=70)
b14.bind("<Button-1>",str_c)

b15=Button(text=".",height=2,width=5,bg="White",relief=RIDGE,font=("bold",14))
b15.place(y=311,x=130)
b15.bind("<Button-1>",str_c)

b20=Button(text="=",height=2,width=5,bg="White",relief=RIDGE,font=("bold",14))
b20.place(y=311,x=190)
b20.bind("<Button-1>",str_c)

root.mainloop()