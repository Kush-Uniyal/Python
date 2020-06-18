import tkinter as tk
from tkinter import ttk
win=tk.Tk()
win.title("Label frame")

label_frame=ttk.LabelFrame(win,text="Enter your details")
label_frame.grid(row=0,column=0,padx=20 )

labels=['Enter your name','Enter your age','Enter your gender','Enter your Country','State','City']

for i in range(len(labels)):
    cur_label=ttk.Label(label_frame,text=labels[i])
    cur_label.grid(row=i,column=0,sticky=tk.W)

info_var=tk.StringVar()
info_person={
    'name':tk.StringVar(),
    'age':tk.StringVar(),
    'gender':tk.StringVar(),
    'country':tk.StringVar(),
    'state':tk.StringVar(),
    'city':tk.StringVar()
    }
counter=0
for i in info_person:
    cur_entry=ttk.Entry(label_frame,width=16,textvariable=info_person[i])
    cur_entry.grid(row=counter,column=1)
    counter+=1


def action():
    print(info_person["name"].get())
    print(info_person["age"].get())
    print(info_person["gender"].get())
    print(info_person["country"].get())
    print(info_person["state"].get())
    print(info_person["city"].get())

sumbit_button=ttk.Button(win,text="Submit",command=action)
sumbit_button.grid(row=1,columnspan=2)

for child in label_frame.winfo_children():
    child.grid_configure(padx=4,pady=4)

win.mainloop()
