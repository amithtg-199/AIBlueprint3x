from tkinter import *

windows = Tk()
windows.title("My fist GUI project")
windows.minsize(width=500, height=500)
'''Used to add padding across the whole window so the widgets are not at the extreme corners of the screen'''
windows.config(padx=50, pady=50)

#Label
my_label = Label(text="My Label", font=("Arial", 24, "bold"))
# '''We can set where our label needs to be'''
# my_label.pack(side="left")
'''used to position the text-box at 0,0 grid system'''
my_label.grid(row=0, column=0)
# '''Since we have setup lable directly as aruguments while init class, here we can modify it as below'''
# my_label["text"] = "New Text"
# '''OR'''
# my_label.config(text="New Text")

#Buttons
'''To do certain action when button is clicked then we do as below'''
def button_clicked():
    '''The get function will actually retrun the value entered by user in text box set by Entry class or input object'''
    input_value = input.get()
    '''Used to change the label when button is clicked and set the value to what user inputs in the text-input box'''
    my_label.config(text=input_value)

'''Here the Button class has an attribute called command where we can pass the function that needs to be executed when button is clicked'''
my_button = Button(text="Click Me", command=button_clicked)
'''used to position the text-box at 1,1 grid system'''
my_button.grid(row=1, column=1)

#New button
new_button = Button(text="Click Me")
new_button.grid(row=0, column=2)

#Input text field
'''To get input from customer we need to have something similar to text filed'''

input = Entry(width=10)
'''used to position the text-box at 2,2 grid system'''
input.grid(row=2,column=3)
windows.mainloop()