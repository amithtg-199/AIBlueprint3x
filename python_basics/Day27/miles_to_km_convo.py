from tkinter import *

def convert_mil_km():
    miles = float(entry.get())
    km_miles = round(miles * 1.6, 2)
    value_km.config(text=f"{km_miles}")

'''Setup windows'''
windows = Tk()
windows.title("Miles to Km converter")
windows.geometry("400x200")
windows.config(padx=100, pady=50)

'''Entery'''
entry = Entry(width=10)
entry.grid(row=0, column=1)
'''Setup Lables'''
#Miles
miles = Label(text="Miles", font=("Sans-serif", 17, "bold"))
miles.grid(row=0, column=2)

#is_equal
is_equal = Label(text="is equal to", font=("Sans-serif", 17, "bold"))
is_equal.grid(row=1, column=0)

#value in km
value_km = Label(text= "0", font=("Sans-serif", 17, "bold"))
value_km.grid(row=1, column=1)

#km lable
km_label = Label(text="km", font=("Sans-serif", 17, "bold"))
km_label.grid(row=1, column=2)

#Calculate Button
calculate = Button(text="Calculate", command=convert_mil_km)
calculate.grid(row=3, column=1)


windows.mainloop()