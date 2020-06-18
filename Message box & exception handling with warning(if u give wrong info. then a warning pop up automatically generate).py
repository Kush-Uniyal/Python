from tkinter import ttk
from tkinter import messagebox as m_box 
import tkinter as tk
win=tk.Tk()
win.title("Message box")

label=ttk.LabelFrame(win,text="Message")
label.grid(row=0,column=0 ,padx=20,pady=20)


email=ttk.Label(label,text="Email",font=("Helvelica",14))
email.grid(row=0,column=0,padx=10,pady=10)

message=ttk.Label(label,text="Message",font=("Helvelica",14) )
message.grid(row=0,column=2,padx=10,pady=10)

email_var=tk.StringVar()
email=ttk.Entry(label,width=20,textvariable=email_var)
email.grid(row=1,column=0,padx=10,pady=10)

message_var=tk.StringVar()
message=ttk.Entry(label,width=20,textvariable=message_var)
message.grid(row=1,column=2,padx=10,pady=10)


def submit():
##    m_box.showwarning("Title","Content of this message box !!")
##    m_box.showerror("Title","Content of this message box !!")
##    m_box.showinfo("Title","Content of this message box !!")
    email=email_var.get()
    message=message_var.get()
    if email=="" or message== "":
        m_box.showinfo("Error","Enter your info:")
    else:
        try:
            message=int(message)
        except ValueError:
             m_box.showerror("Error","fill message in digits")
        else:
            if message>18:
                m_box.showwarning("Warning","you ar not above 18, visit this on your own risk")
            print(f"{email} {message}")
        


submit_btn=ttk.Button(win,text="Submit",command=submit)
submit_btn.grid(row=2, columnspan=3)


win.mainloop()
