from tkinter import *
from tkinter import messagebox
from tkcalendar import DateEntry
from mysql import connector as c


a = Tk()
a.geometry("650x650")
f = Frame(a, bg="white", height=550, width=500)
f.place(x=70, y=50)
a.resizable(False, False)
a.title("Login Page")


# 1st_screen_head_label
l1 = Label(f, text="LOGIN", bg="white", font=("Chillar", "30", "bold"))
l1.place(x=180, y=1)


# 1st_screen_login_labels
l2 = Label(f, text="Enter Your Name ", bg="white", font=("Chillar", "15"))
l2.place(x=20, y=100)
l3 = Label(f, text="Password", bg="white", font=("Chillar", "15"))
l3.place(x=20, y=200)


# 1st_screen_Login_button_function
def login():
    name = "Ashish"
    p = "1234"
    if var.get() == name and var2.get() == p:
        messagebox.showinfo("Logged in", "Successfully logged in")
        a.destroy()

        # 2nd_Screen
        z = Tk()
        z.geometry("700x700")
        width = z.winfo_screenwidth()
        height = z.winfo_screenheight()


        # setting tkinter window size
        z.geometry("%dx%d" % (width, height))
        z.title("Registration Page")

        # 2nd_Screen_head label
        z1 = Label(z, text="EMPLOYEE REGISTRATION FORM", font=("Chillar", "30", "bold"))
        z1.place(x=430, y=1)

        # 2nd_screen_labels
        l21 = Label(z, text="Employee First Name", font=("Chillar", "20"))
        l21.place(x=30, y=100)
        l212 = Label(z, text="Employee Last name", font=("Chillar", "20"))
        l212.place(x=700, y=100)
        l22 = Label(z, text="Employee ID", font=("Chillar", "20"))
        l22.place(x=30, y=150)
        l23 = Label(z, text="Employee Department", font=("Chillar", "20"))
        l23.place(x=30, y=200)
        l24 = Label(z, text="Employee Designation", font=("Chillar", "20"))
        l24.place(x=30, y=250)
        l25 = Label(z, text="Employee Phone No.", font=("Chillar", "20"))
        l25.place(x=30, y=300)
        l252 = Label(z, text="Date Of Birth", font=("Chillar", "20"))
        l252.place(x=700, y=300)
        l26 = Label(z, text="Employee Address ", font=("Chillar", "20"))
        l26.place(x=30, y=350)
        l262 = Label(z, text="Pincode", font=("Chillar", "20"))
        l262.place(x=700, y=350)
        l27 = Label(z, text="Date Of Joining", font=("Chillar", "20"))
        l27.place(x=30, y=400)
        l28 = Label(z, text="Gender", font=("Chillar", "20"))
        l28.place(x=30, y=450)
        l29 = Label(z, text="Salary", font=("Chillar", "20"))
        l29.place(x=30, y=500)
        l30 = Label(z, text="Marital Status", font=("Chillar", "20"))
        l30.place(x=30, y=550)
        l31 = Label(z, text="Experience (if any)", font=("Chillar", "20"))
        l31.place(x=30, y=600)
        l30 = Label(z, text="Residential Proof(Government Verified)", font=("Chillar", "20"))
        l30.place(x=30, y=650)


        # 2nd_Screen_entry
        z1 = StringVar()
        e21 = Entry(z, relief="raised", width=35, textvariable=z1)
        e21.place(x=350, y=110)
        z2 = StringVar()
        e212 = Entry(z, relief="raised", width=35, textvariable=z2)
        e212.place(x=1000, y=110)
        z3 = IntVar()
        e22 = Entry(z, relief="raised", width=35, textvariable=z3)
        e22.place(x=350, y=160)
        z4 = StringVar()
        e23 = Entry(z, relief="raised", width=35, textvariable=z4)
        e23.place(x=350, y=210)
        z5 = StringVar()
        e24 = Entry(z, relief="raised", width=35, textvariable=z5)
        e24.place(x=350, y=260)
        z6 = IntVar()
        e25 = Entry(z, relief="raised", width=35, textvariable=z6)
        e25.place(x=350, y=310)
        z7 = StringVar()
        e252 = DateEntry(z, relief="raised", width=30, textvariable=z7)
        e252.place(x=1000, y=310)
        z8 = StringVar()
        e26 = Entry(z, relief="raised", width=55, textvariable=z8)
        e26.place(x=350, y=360)
        z9 = IntVar()
        e262 = Entry(z, relief="raised", width=20, textvariable=z9)
        e262.place(x=1000, y=360)
        z10 = StringVar()
        e27 = DateEntry(z, relief="raised", width=30, textvariable=z10)
        e27.place(x=350, y=410)
        z12 = IntVar()
        e28 = Entry(z, relief="raised", width=20, textvariable=z12)
        e28.place(x=350, y=510)

        option1 = ["Male", "Female", "Others"]
        option2 = ["Married", "Unmarried"]
        option3 = ["Aadhar Card", "Pan Card", "Driving License", "10th DMC", "12th DMC", "Electricity/Water Bill"]

        # gender datatype of menu
        gender_option = StringVar()

        # dropdown of gender
        gender_option.set("Choose the Gender")

        # Dropdown menu for gender
        drop1 = OptionMenu(z, gender_option, *option1)
        drop1.place(x=350, y=460)

        # married datatype of menu
        married_option = StringVar()

        # dropdown of married
        married_option.set("Choose the Marital Status")

        # Dropdown menu for married
        drop2 = OptionMenu(z, married_option, *option2)
        drop2.place(x=350, y=560)
        z14 = IntVar()
        e31 = Entry(z, relief="raised", width=20, textvariable=z14)
        e31.place(x=350, y=610)

        # residential datatype of menu
        res_option = StringVar()

        # dropdown of residential
        res_option.set("Choose the Residential Proof")

        # Dropdown menu for residential
        drop3 = OptionMenu(z, res_option, *option3)
        drop3.place(x=550, y=650)

        # database connectivity
        def submit():
            global x
            e = c.connect(host="localhost", password="", port=3306, user="root", database="office")
            my_cursor = e.cursor()
            qry = "insert into entry1(emp_f_name, emp_l_name, emp_id, emp_dept, emp_designation, emp_ph, dob, address, pincode, doj, gender, salary, marital, experience, proof) " \
              "values (%s, %s, %d, %s, %s, %d, %s, %s, %d, %s, %s, %d, %s, %s, %s)"
            val = (z1.get(), z2.get(), z3.get(), z4.get(), z5.get(), z6.get(), z7, z8.get(), z9.get(), z10, gender_option, z12.get(), married_option, z14.get(), res_option)
            my_cursor.execute(qry, val)
            e.commit()
            e.close()

            messagebox.showinfo("Data Saved in Database", "Alert")

        # 2nd_Screen_Button
        b21 = Button(z, text="Submit", bg="azure3", fg="black", width=30, command=submit)
        b21.place(x=300, y=730)

        # 2nd_screen_clear function
        def clear():

            e21.delete(0, END)
            e22.delete(0, END)
            e23.delete(0, END)
            e24.delete(0, END)
            e25.delete(0, END)
            e26.delete(0, END)
            e27.delete(0, END)
            e28.delete(0, END)
            e212.delete(0, END)
            e252.delete(0, END)
            e262.delete(0, END)
            e31.delete(0, END)


        b22 = Button(z, text="Clear", bg="azure3", fg="black", width=30, command=clear)
        b22.place(x=700, y=730)
        b23 = Button(z, text="Cancel", bg="azure3", fg="black", width=30, command=exit)
        b23.place(x=1100, y=730)

        # 2nd_Screen_mainloop
        z.mainloop()

    else:
        messagebox.showinfo("Error", "Wrong Inputs")


# 1st_screen_label's Entry
var = StringVar()
e1 = Entry(f, relief="raised", width=40, bd=6, textvariable=var)
e1.place(x=240, y=100)
var2 = StringVar()
var3 = IntVar(value=0)
e2 = Entry(f, relief="raised", width=40, bd=6, textvariable=var2, show="*")
e2.place(x=240, y=200)

# password showing function
def show():
    if(var3.get()==1):
        e2.config(show='')
    else:
        e2.config(show='*')
e21 = Checkbutton(f, text='Show Password', variable=var3, onvalue=1, offvalue=0, command=show)
e21.place(x=240, y=250)


# 1st_screen_Login_Button
b1 = Button(f, text="Login", relief="raised", fg="black", width=20, command=login)
b1.place(x=70, y=300)
b1 = Button(f, text="Cancel", relief="raised", fg="black", width=20, command=exit)
b1.place(x=300, y=300)

# 1st_screen_mainloop
a.mainloop()


