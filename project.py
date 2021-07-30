from tkinter import *
root = Tk()
root.geometry("500x300")

Label(root, text="Python Registratialion Form", font="ar 15 bold").grid(row=0, column=3)

name = Label(root, text="Name")
phone = Label(root, text="Phone")
gender = Label(root, text="Gender")
emergency = Label(root, text="Emergency")
paymentmood = Label(root, text="Payment Mood")

name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
emergency.grid(row=4, column=2)
paymentmood.grid(row=5, column=2)

namevalue = StringVar
phonevalue = StringVar
gendervalue = StringVar
emergencyvalue = StringVar
paymentmoodvalue = StringVar
checkvalue = IntVar

nameEntry = Entry(root, textvariable = namevalue)
phoneEntry = Entry(root, textvariable = phonevalue)
genderEntry = Entry(root, textvariable = gendervalue)
emergencyEntry = Entry(root, textvariable = emergencyvalue)
paymentEntry = Entry(root, textvariable = paymentmoodvalue)
checkEntry = Entry(root, textvariable = checkvalue)

nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)
emergencyentry.grid(row=4, column=3)
paymentmoodentry.grid(row=5, column=3)
nameentry.grid(row=5, column=3)






root.mainloop()