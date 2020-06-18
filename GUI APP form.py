## starter code
import tkinter as tk
from tkinter import ttk
from csv import DictWriter
import os
win=tk.Tk()
win.title("GUI ")

## create labels
## widgets ---->labels,buttons,radio buttons -tk,ttk(for more graphical representation)
name_label=ttk.Label(win,text="Enter your name: ")
name_label.grid(row=0,column=0, sticky=tk.W) ##grid/pack(usse to give location)

email_label=ttk.Label(win,text="Enter your Email-Id: ")
email_label.grid(row=1,column=0,sticky=tk.W)
 
age_label=ttk.Label(win,text="Enter your age: ")
age_label.grid(row=2,column=0,sticky=tk.W)   ##sticky=tk.W(It is use to label all line in sequence.__ W(wesr))

gender_label=ttk.Label(win,text="Select your gender")
gender_label.grid(row=3,column=0,sticky=tk.W)


##create Entry box

name_var=tk.StringVar()
name_entrybox=ttk.Entry(win,width=20,textvariable=name_var)
name_entrybox.grid(row=0,column=1)
name_entrybox.focus()

email_var=tk.StringVar()
email_entrybox=ttk.Entry(win,width=20,textvariable=email_var)
email_entrybox.grid(row=1,column=1)

age_var=tk.StringVar()
age_entrybox=ttk.Entry(win,width=20,textvariable=age_var)
age_entrybox.grid(row=2,column=1)


## create Combobox

gender_var=tk.StringVar()
gender_combobox=ttk.Combobox(win,width=17,textvariable=gender_var,state="readonly")
gender_combobox["values"]=("Male","Female","Other")
gender_combobox.current(0) #It is use to select default value is male and 0 is use bcz male is on 0th poistion
gender_combobox.grid(row=3,column=1)

## create Radio button

usertype=tk.StringVar()
radiobtn1=ttk.Radiobutton(win,text="Student",value="Student",variable=usertype)
radiobtn1.grid(row=4,column=0)

radiobtn2=ttk.Radiobutton(win,text="Teacher",value="Teacher",variable=usertype)
radiobtn2.grid(row=4,column=1)

## create check button
checkbtn_var=tk.IntVar()
checkbtn1=ttk.Checkbutton(win,text="check if you want to subscribe our newsletter",variable=checkbtn_var)
checkbtn1.grid(row=5,columnspan=3)   # columnspan is use to combine 2 or more column instead spoil of other alignment

### create txt file

##def action():
##    username = name_var.get()
##    userage = age_var.get()
##    user_email = email_var.get()
##    print(f"{username} is {userage} years old and email_ID is {user_email}")
##    gendervar=gender_var.get()
##    user_type=usertype.get()
##    if checkbtn_var.get()==0:
##        subscribed="Yes"
##    else:
##        subscribed="No"
##
##    print(f"{gendervar} {user_type} {subscribed}")
##
##    with open("File.txt","a") as f:             #create a file and store all values in the file.......
##        f.write(f"{username},{userage},{user_email},{gendervar},{user_type},{subscribed}\n")
##
##    name_entrybox.delete(0,tk.END)
##    age_entrybox.delete(0,tk.END)    #It is use to remove all values from entry box after submission..........
##    email_entrybox.delete(0,tk.END)
##
##    name_label.configure(foreground="Blue")     #It is use to covert label into blue color after submission..........

### Create csv file

def action():
    username = name_var.get()
    userage = age_var.get()
    user_email = email_var.get()
    gendervar=gender_var.get()
    user_type=usertype.get()
    if checkbtn_var.get()==0:
        subscribed="Yes"
    else:
        subscribed="No"
 
    with open("file.csv","a",newline="" ) as f:             #create a file and store all values in the file.......
        
        dict_writer=DictWriter(f,fieldnames=["User name","User age","User email","User gender","User type","Subcribed"])
        if os.stat("file.csv").st_size==0:     ## this line is use to not repeat header again and again in csv file.............
            dict_writer.writeheader()
            
        dict_writer.writerow({
            "User name":username,
            "User age":userage,
            "User email":user_email,
            "User gender":gendervar,
            "User type":user_type,
            "Subcribed":subscribed})


        
    name_entrybox.delete(0,tk.END)
    age_entrybox.delete(0,tk.END)    #It is use to remove all values from entry box after submission..........
    email_entrybox.delete(0,tk.END)

    name_label.configure(foreground="Blue")

#### create submit button
    
Submit_button= ttk.Button(win,text="Sumbit",command=action) ## after command given we have to define action command is use to perform action
Submit_button.grid(row=6,column=0)

win.mainloop() 
