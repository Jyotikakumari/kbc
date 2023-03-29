from tkinter import*
root=Tk()
root.geometry("400x500")
root.title("calculator by jyotika")
expression=""
displaytext=StringVar()
def press(num):
    global expression
    expression+=num
    displaytext.set(expression)
def equal():
    global expression
    total=eval(expression)
    displaytext.set(total) 
def cleardisplay():
    global expression
    expression=""
    displaytext.set("0")   
        
display=Entry(root,width=20,font=("arial",22),textvariable=displaytext)

btn1=Button(root,text="1",padx=10,pady=10,font=("arial",22),command=lambda:press("1"))
btn2=Button(root,text="2",padx=10,pady=10,font=("arial",22),command=lambda:press("2"))
btn3=Button(root,text="3",padx=10,pady=10,font=("arial",22),command=lambda:press("3"))
btn4=Button(root,text="+",padx=10,pady=10,font=("arial",22),command=lambda:press("+"))

btn5=Button(root,text="4",padx=10,pady=10,font=("arial",22),command=lambda:press("4"))
btn6=Button(root,text="5",padx=10,pady=10,font=("arial",22),command=lambda:press("5"))
btn7=Button(root,text="6",padx=10,pady=10,font=("arial",22),command=lambda:press("6"))
btn8=Button(root,text="-",padx=10,pady=10,font=("arial",22),command=lambda:press("-"))

btn9=Button(root,text="7",padx=10,pady=10,font=("arial",22),command=lambda:press("7"))
btn10=Button(root,text="8",padx=10,pady=10,font=("arial",22),command=lambda:press("8"))
btn11=Button(root,text="9",padx=10,pady=10,font=("arial",22),command=lambda:press("9"))
btn12=Button(root,text="/",padx=10,pady=10,font=("arial",22),command=lambda:press("/"))

btn13=Button(root,text="0",padx=10,pady=10,font=("arial",22),command=lambda:press("0"))
btn14=Button(root,text="=",padx=10,pady=10,font=("arial",22),command=equal)
btn15=Button(root,text="C",padx=10,pady=10,font=("arial",22), bg="purple",fg="white",command=cleardisplay)
btn16=Button(root,text="X",padx=10,pady=10,font=("arial",22),command=lambda:press("*"))

display.grid(row=0,column=0,columnspan=4,padx=10,pady=10)


btn1.grid(row=1,column=0,padx=10,pady=10)
btn2.grid(row=1,column=1,padx=10,pady=10)
btn3.grid(row=1,column=2,padx=10,pady=10)
btn4.grid(row=1,column=3,padx=10,pady=10)

btn5.grid(row=2,column=0,padx=10,pady=10)
btn6.grid(row=2,column=1,padx=10,pady=10)
btn7.grid(row=2,column=2,padx=10,pady=10)
btn8.grid(row=2,column=3,padx=10,pady=10)

btn9.grid(row=3,column=0,padx=10,pady=10)
btn10.grid(row=3,column=1,padx=10,pady=10)
btn11.grid(row=3,column=2,padx=10,pady=10)
btn12.grid(row=3,column=3,padx=10,pady=10)

btn13.grid(row=4,column=0,padx=10,pady=10)
btn14.grid(row=4,column=1,padx=10,pady=10)
btn15.grid(row=4,column=2,padx=10,pady=10)
btn16.grid(row=4,column=3,padx=10,pady=10)




root.mainloop()

