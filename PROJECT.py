from tkinter import *
from tkinter import messagebox as mb
from tkinter import Entry as E

#------------------------LOG IN FORM------------------------#

#create window
window = Tk()
window.geometry("400x250+400+400")
window.title("Log-in")
window.resizable(0, 0)
back = Frame(master=window,bg='white')
back.pack_propagate(0)
back.pack(expand=1)

#label
title = Label(text="Log in", font=("Arial",30,"bold"))
title.place(x=140,y=0)
text_username = Label(text="Username", font=("Arial", 15)).place(x=30,y=50)
text_password = Label(text="Password", font=("Arial", 15)).place(x=30,y=120)

#entry
initial_entry_username = E(window, width=55)
initial_entry_username.place(x=30,y=80)
initial_entry_password = E(window, width=55,show="*")
initial_entry_password.place(x=30,y=150)

#command
def data_processing():
    global file, cache, clear_data, index
    file = open("username and password.txt")
    cache= file.readlines()
    clear_data=[]
    for i in cache:
        clear_data.append(i.split("\t"))
    for y in clear_data:
        for x in y:
            index = y.index(x)
            y.pop(index)
            y.insert(index, x.removesuffix("\n"))
data_processing()
status = False
def check():
    global status, number_account, entry_username, entry_password, account_file_name
    entry_username = initial_entry_username.get()
    entry_password = initial_entry_password.get()
    for m in clear_data:
        if m[0] == entry_username and m[1] == entry_password:
            status = True
            account_file_name = str(entry_username) + ".txt"
            mb.showinfo(title="Notification",message="Log in successfully")
            window.destroy()
            overview()
            break
        else:
            status = False
            continue
    if status == False:
        mb.showerror(title="Notification",message="Log in failed")

#button
log_in = Button(window, text="Log in", command=check)
log_in.pack(side=BOTTOM)


#------------------------MAIN PROGRAM------------------------#

def overview():
    global window_overview
    #set up window
    window_overview = Tk()
    window_overview.geometry("400x400+400+400")
    window_overview.title("Overview")
    window_overview.resizable(0, 0)
    back_overview = Frame(master=window_overview, bg='white')
    back_overview.pack_propagate(0)
    back_overview.pack(expand=1)
    #title
    overview_title = Label(text="YOUR PROFILE", font=("Arial", 30, "bold"))
    overview_title.place(x=50,y=0)
    #profile
    get_account_profile()
    name = Label(text="Name:", font=("Arial", 14))
    name.place(x=30,y=110)
    name_info = Label(text=profile_info[0], font=("Arial", 14, "italic"))
    name_info.place(x=130, y=110)
    dob = Label(text="DOB:", font=("Arial",14))
    dob.place(x=30, y =150)
    dob_info=Label(text=profile_info[1], font=("Arial", 14, "italic"))
    dob_info.place(x=130,y=150)
    gender=Label(text="Gender:", font=("Arial",14))
    gender.place(x=30, y=190)
    gender_info= Label(text=profile_info[2], font=("Arial", 14, "italic"))
    gender_info.place(x=130, y=190)
    mobile = Label(text="Mobile:", font=("Arial", 14))
    mobile.place(x=30, y=230)
    mobile_info = Label(text=profile_info[3], font=("Arial", 14, "italic"))
    mobile_info.place(x=130, y=230)
    mail = Label(text="Email:", font=("Arial", 14))
    mail.place(x=30, y=270)
    mail_info = Label(text=profile_info[4], font=("Arial", 14, "italic"))
    mail_info.place(x=130,y=270)
    position = Label(text="Position:",font=("Arial", 14))
    position.place(x=30,y=310)
    position_info = Label(text=profile_info[5], font=("Arial", 14, "italic"))
    position_info.place(x=130,y=310)
    window_overview.mainloop()

def get_account_profile():
    global profile, profile_info
    profile = open(account_file_name)
    profile_info = profile.readlines()
    for y in profile_info:
        index = profile_info.index(y)
        profile_info.pop(index)
        profile_info.insert(index, y.removesuffix("\n"))

    # window_overview = Tk()
    # window_overview.title("Overview")
    # width = window_overview.winfo_screenwidth()
    # height = window_overview.winfo_screenheight()
    # window_overview.geometry("%dx%d" % (width, height))

window.mainloop()