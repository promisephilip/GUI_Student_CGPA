#Importing Library
import tkinter as tk
import os
from tkinter import *
from tkinter import messagebox

#Craeting a new tkinter window
main = tk.Tk() 

# assigning a title 
main.title("STUDENT DATA ANALYSIS - SDA") 

# specifying geomtery for window size 
main.geometry("630x300")

# declaring objects for entering data 
e1 = tk.Entry(main) 
e2 = tk.Entry(main) 
e3 = tk.Entry(main) 
e4 = tk.Entry(main) 
e5 = tk.Entry(main) 
e6 = tk.Entry(main) 
e7 = tk.Entry(main)
e8 = tk.Entry(main)
e9 = tk.Entry(main)
e10 = tk.Entry(main)
e11 = tk.Entry(main)

# taking entries of first name, last name,reg & roll number respectively 
e1 = tk.Entry(main)
e2 = tk.Entry(main)
e3 = tk.Entry(main)
e4 = tk.Entry(main)

# organizing them in the grid 
e1.grid(row=0, column=1) 
e2.grid(row=1, column=1) 
e3.grid(row=0, column=5)
e4.grid(row=1, column=5)

#about
def about():
    messagebox.showinfo('STUDENT DATA ANALYSIS - SDA','This program aims to help calculate CGPA of a computer science student in a certain (anonymous) University student in Nigeria.\nNote that the maximum CGPA is 5.0.')
    
def refresh():
    main.destroy()
    os.popen("GUI_Student_CGPA.py")
    
#course credit & cgpa to grades entered
def display():
    
    #variable to store total marks
    tot = 0
    if e5.get().upper() == "A": 
        tk.Label(main, text ="15").grid(row=3, column=4) 
        tot += 15
    elif e5.get().upper() == "B": 
        tk.Label(main, text ="12").grid(row=3, column=4) 
        tot += 12
    elif e5.get().upper() == "C": 
        tk.Label(main, text ="9").grid(row=3, column=4) 
        tot += 9
    elif e5.get().upper() == "D": 
        tk.Label(main, text ="6").grid(row=3, column=4) 
        tot += 6
    elif e5.get().upper() == "E": 
        tk.Label(main, text ="3").grid(row=3, column=4) 
        tot += 3
    elif e5.get().upper() == "F": 
        tk.Label(main, text ="0").grid(row=3, column=4) 
        tot += 0
    else:
        messagebox.showinfo('Invalid Grade','Kindly enter grade from A - E.')
        tk.Label(main, text = "-").grid(row=3, column=4)
    
    if e6.get().upper() == "A": 
        tk.Label(main, text ="15").grid(row=4, column=4)
        tot += 15
    elif e6.get().upper() == "B": 
        tk.Label(main, text ="12").grid(row=4, column=4)
        tot += 12
    elif e6.get().upper() == "C": 
        tk.Label(main, text ="9").grid(row=4, column=4)
        tot += 9
    elif e6.get().upper() == "D": 
        tk.Label(main, text ="6").grid(row=4, column=4)
        tot += 6
    elif e6.get().upper() == "E": 
        tk.Label(main, text ="3").grid(row=4, column=4)
        tot += 3
    elif e6.get().upper() == "F": 
        tk.Label(main, text ="0").grid(row=4, column=4)
        tot += 0
    else:
        messagebox.showinfo('Invalid Grade','Kindly enter grade from A - E.')
        tk.Label(main, text = "-").grid(row=4, column=4)

    if e7.get().upper() == "A": 
        tk.Label(main, text ="15").grid(row=5, column=4)
        tot += 15
    elif e7.get().upper() == "B": 
        tk.Label(main, text ="12").grid(row=5, column=4)
        tot += 12
    elif e7.get().upper() == "C": 
        tk.Label(main, text ="9").grid(row=5, column=4)
        tot += 9
    elif e7.get().upper() == "D": 
        tk.Label(main, text ="6").grid(row=5, column=4) 
        tot += 6
    elif e7.get().upper() == "P": 
        tk.Label(main, text ="3").grid(row=5, column=4) 
        tot += 3
    elif e7.get().upper() == "F": 
        tk.Label(main, text ="0").grid(row=5, column=4) 
        tot += 0
    else:
        messagebox.showinfo('Invalid Grade','Kindly enter grade from A - E.')
        tk.Label(main, text = "-").grid(row=5, column=4)
        
    if e8.get().upper() == "A": 
        tk.Label(main, text ="10").grid(row=6, column=4) 
        tot += 10
    elif e8.get().upper() == "B": 
        tk.Label(main, text ="8").grid(row=6, column=4) 
        tot += 8
    elif e8.get().upper() == "C": 
        tk.Label(main, text ="6").grid(row=6, column=4) 
        tot += 6
    elif e8.get().upper() == "D": 
        tk.Label(main, text ="4").grid(row=6, column=4) 
        tot += 4
    elif e8.get().upper() .upper()== "E":
        tk.Label(main, text ="2").grid(row=6, column=4) 
        tot += 2
    elif e8.get().upper() == "F": 
        tk.Label(main, text ="0").grid(row=6, column=4) 
        tot += 0
    else:
        messagebox.showinfo('Invalid Grade','Kindly enter grade from A - E.')
        tk.Label(main, text = "-").grid(row=6, column=4)

    if e9.get().upper() == "A": 
        tk.Label(main, text ="15").grid(row=7, column=4) 
        tot += 15
    elif e9.get().upper() == "B": 
        tk.Label(main, text ="12").grid(row=7, column=4) 
        tot += 12
    elif e9.get().upper() == "C": 
        tk.Label(main, text ="9").grid(row=7, column=4) 
        tot += 9
    elif e9.get().upper() == "D": 
        tk.Label(main, text ="6").grid(row=7, column=4) 
        tot += 6
    elif e9.get().upper() == "E": 
        tk.Label(main, text ="3").grid(row=7, column=4) 
        tot += 3
    elif e9.get().upper() == "F": 
        tk.Label(main, text ="0").grid(row=7, column=4) 
        tot += 0
    else:
        messagebox.showinfo('Invalid Grade','Kindly enter grade from A - E.')
        tk.Label(main, text = "-").grid(row=7, column=4)
    

    if e10.get().upper() == "A": 
        tk.Label(main, text ="10").grid(row=8, column=4) 
        tot += 10
    elif e10.get().upper() == "B": 
        tk.Label(main, text ="8").grid(row=8, column=4) 
        tot += 8
    elif e10.get().upper() == "C": 
        tk.Label(main, text ="6").grid(row=8, column=4) 
        tot += 6
    elif e10.get().upper() == "D": 
        tk.Label(main, text ="4").grid(row=8, column=4) 
        tot += 4
    elif e10.get().upper() == "E": 
        tk.Label(main, text ="2").grid(row=8, column=4) 
        tot += 2
    elif e10.get().upper() == "F": 
        tk.Label(main, text ="0").grid(row=8, column=4) 
        tot += 0
    else:
        messagebox.showinfo('Invalid Grade','Kindly enter grade from A - E.')
        tk.Label(main, text = "-").grid(row=8, column=4)
        
    if e11.get().upper() == "A": 
        tk.Label(main, text ="10").grid(row=9, column=4) 
        tot += 10
    elif e11.get().upper() == "B": 
        tk.Label(main, text ="8").grid(row=9, column=4) 
        tot += 8
    elif e11.get().upper() == "C": 
        tk.Label(main, text ="6").grid(row=9, column=4) 
        tot += 6
    elif e11.get().upper() == "D": 
        tk.Label(main, text ="4").grid(row=9, column=4) 
        tot += 4
    elif e11.get().upper() == "E": 
        tk.Label(main, text ="2").grid(row=9, column=4) 
        tot +=  2
    elif e11.get().upper() == "F": 
        tk.Label(main, text ="0").grid(row=9, column=4) 
        tot += 0
    else:
        tk.Label(main, text ="-").grid(row=9, column=4)
        messagebox.showinfo('Invalid Grade',"Kindly enter Enter 'A','B','C','D','E, or 'F'.")
    
    # to display totalgrade points
    tk.Label(main, text=str(tot)).grid(row=11, column=4)
    
    # to display CGPA
    tk.Label(main, text=str(tot/18)).grid(row=12, column=4)     

#Menu
menu = Menu(main)
main.config(menu=menu)

filemenu = Menu(menu,background='#ff8000',
                foreground='black', 
                activebackground='white', 
                activeforeground='black')
menu.add_cascade(label='File',
                 menu=filemenu,
                 background='#ffcc99',
                underline=0)

filemenu.add_separator()
filemenu.add_command(label='Exit', command=main.destroy)
helpmenu = Menu(menu)

menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About', command=about)

# label to enter first name 
tk.Label(main, text="First Name: ").grid(row=0, column=0) 

# label to enter last name 
tk.Label(main, text="Last Name: ").grid(row=1, column=0) 

# label for registration number 
tk.Label(main, text="Matric No: ").grid(row=0, column=4)

# label for examination Number 
tk.Label(main, text="Examination No: ").grid(row=1, column=4)

# labels for serial numbers 
tk.Label(main, text="S/N").grid(row=2, column=0) 
tk.Label(main, text="1").grid(row=3, column=0) 
tk.Label(main, text="2").grid(row=4, column=0) 
tk.Label(main, text="3").grid(row=5, column=0) 
tk.Label(main, text="4").grid(row=6, column=0)
tk.Label(main, text="5").grid(row=7, column=0) 
tk.Label(main, text="6").grid(row=8, column=0) 
tk.Label(main, text="7").grid(row=9, column=0)

# labels for course codes 
tk.Label(main, text="Course Title").grid(row=2, column=1) 
tk.Label(main, text="CSC 101").grid(row=3, column=1) 
tk.Label(main, text="CSC 102").grid(row=4, column=1) 
tk.Label(main, text="CSC 103").grid(row=5, column=1) 
tk.Label(main, text="CSC 104").grid(row=6, column=1)
tk.Label(main, text="MTH 112").grid(row=7, column=1)
tk.Label(main, text="MTH 114").grid(row=8, column=1)
tk.Label(main, text="GES 101").grid(row=9, column=1)

# label for grades 
tk.Label(main, text="Grade Point").grid(row=2, column=4)
e5.grid(row=3, column=2)
e6.grid(row=4, column=2)
e7.grid(row=5, column=2) 
e8.grid(row=6, column=2) 
e9.grid(row=7, column=2) 
e10.grid(row=8, column=2) 
e11.grid(row=9, column=2)

# labels for course credit
tk.Label(main, text="Credit Unit").grid(row=2, column=3) 
tk.Label(main, text="3").grid(row=3, column=3) 
tk.Label(main, text="3").grid(row=4, column=3) 
tk.Label(main, text="3").grid(row=5, column=3) 
tk.Label(main, text="2").grid(row=6, column=3)
tk.Label(main, text="3").grid(row=7, column=3) 
tk.Label(main, text="2").grid(row=8, column=3) 
tk.Label(main, text="2").grid(row=9, column=3)

#button to display calculated credit score & cgpa
button1 = tk.Button(main, text="Submit", 
                    bg="Lightblue",
                    fg="black",
                    command=display)
button1.grid(row=13, column=3)

tk.Label(main, text="Total Credit = ").grid(row=11, column=3) 
tk.Label(main, text="CGPA (5.0) = ").grid(row=12, column=3) 

main.mainloop()
