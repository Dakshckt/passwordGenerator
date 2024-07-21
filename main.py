import tkinter as tk
from tkinter.ttk import *
from tkinter import messagebox
import random
from Operation import allGenerate , txtGenerate , numGenerate , charGenerate , specialGenerate

def display(result):
    displayText.delete("1.0" , tk.END)
    displayText.insert("1.0" , result)

def generate():
    try:
        length = int(lenEntry.get())
        textInclude = var1.get()
        numInclude = var2.get()
        specialInclude = var3.get()

        if length:
            if length < 13:
                if textInclude and numInclude and specialInclude:
                    values = allGenerate()
                    numValues = numGenerate()
                    specificValue = random.sample(values , length-1)
                    numSingleSelect = random.sample(numValues , 1)
                    result = txtGenerate(specificValue)
                    for val in numSingleSelect:
                        result += chr(val)
                    display(result)

                elif textInclude and numInclude:
                    numValues = numGenerate()
                    charValues = charGenerate()
                    for val in numValues:
                        charValues.append(val)
                    for val in charValues:
                        numValues.append(val)
                    specifiedValues = random.sample(numValues , length)
                    result = txtGenerate(specifiedValues)
                    display(result)

                elif textInclude and specialInclude:
                    charValues = charGenerate()
                    specialValues = specialGenerate()
                    for val in specialValues:
                        charValues.append(val)
                    specifiedValues = random.sample(charValues , length)
                    result = txtGenerate(specifiedValues)
                    display(result)

                elif specialInclude and numInclude:
                    numValues = numGenerate()
                    specialValues = specialGenerate()
                    for val in specialValues:
                        numValues.append(val)
                    specifiedValues = random.sample(numValues , length)
                    result = txtGenerate(specifiedValues)
                    display(result) 
                
                elif textInclude:
                    charValues = charGenerate()
                    specifiedValues = random.sample(charValues , length)
                    result = txtGenerate(specifiedValues)
                    display(result)

                elif numInclude:
                    numValues = numGenerate()
                    specifiedValues = random.sample(numValues , length)
                    result = txtGenerate(specifiedValues)
                    display(result)

                elif specialInclude:
                    specialValues = specialGenerate()
                    specifiedValues = random.sample(specialValues , length)
                    result = txtGenerate(specifiedValues)
                    display(result)

                else:
                    messagebox.showerror("Error","Include any one of the given options")
            else:
                messagebox.showerror("Error","The length can be equal to or less than 12")

    except Exception as err:
        messagebox.showerror("Error" , "Error in the process")

base = tk.Tk()
base.geometry("350x450")
base.title("Password Generator")
var1 = tk.IntVar()
var2 = tk.IntVar()
var3 = tk.IntVar()
titleLabel = Label(base , text="Password Generator" , font=("Arial" , 20))
titleLabel.grid(row=0 , column=0 , columnspan=2 , pady=30)
lenEntry = Entry(base , width=20)
lenEntry.grid(row=1 , column=0 , pady=10 , padx=0)
lenLabel = Label(base , text="Enter the Length of the password")
lenLabel.grid(row=1 , column=1 , pady=10 )
textCheck = tk.Checkbutton(base , text="Text" , variable = var1)
numCheck = tk.Checkbutton(base , text="Numbers" , variable = var2)
specialCheck = tk.Checkbutton(base , text="Special Numbers" , variable = var3)
textCheck.grid(row=2 , column=0 , pady=10 , padx=20 , sticky="W")
numCheck.grid(row=3 , column=0 , pady=10 , padx=20 , sticky="W")
specialCheck.grid(row=4 , column=0 , pady=10 , padx=20 , sticky="W")
button = Button(base , text="Submit" , command=generate)
button.grid(row=5 , column=1 , pady=10 , padx=20)
displayText = tk.Text(base , width=20 , height=1 , font=("Arial" , 20))
displayText.grid(row=6 , column=0 , columnspan=2 , pady=10 , padx=20)

base.mainloop()