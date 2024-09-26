#this imports tkinter for the gui
from tkinter import *

#this creates the root window/main window
root = Tk()

#this gives the window a title
root.title("BMI Calculator")

#this changes the background color of the window
root.config(bg = "skyblue")

#this is the function that updates the height and weight inputs based on what the user selects as their units
def printResults():
    unit = Unit.get()
    
    #this updates the height and weight based on the selected unit
    if unit == "Metric":
        Height_Label.config(text="Enter your Height (meters):")
        Weight_Label.config(text="Enter your Weight (kg):")
    else:
        Height_Label.config(text="Enter your Height (inches):")
        Weight_Label.config(text="Enter your Weight (lbs):")

#this is the function to calculate the bmi
def calcBMI():
    
    #we want to make sure that height and weight are integers
    try:
        h = float(Height.get()) #this will get the height from the entry field
        w = float(Weight.get()) #this will get the weight from the entry field
    except:
        Result.config(text="Please enter numeric inputs for height and weight.", bg="skyblue")
    
    #this defines u as the the metric or imperial value from the radio button
    u = Unit.get()
    
    #this will calculate the bmi based on the types of units provided
    if u == "Metric":
        bmi = w / (h**2)
    else:
        bmi = (w / (h**2)) * 703
    
    #this will update the result label with the bmi and bmi category
    Result.config(text=f"Your BMI is: {bmi:.2f} ({catBMI(bmi)})")

def catBMI(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Healthy Weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    elif 30 <= bmi < 35:
        return "Class I Obesity"
    elif 35 <= bmi < 40:
        return "Class II Obesity"
    elif 40 <= bmi:
        return "Class III Obesity"

#this will create the label that will ask the person to pick imperial or metric; anchor="w" tells it to place this below any other thing in the window
Label(root, text="Select your preferred unit of measurement: ").pack(anchor="w")

#this will define the function to switch to imperial or metric
Unit = StringVar(root, "Metric") #this is a variable for the string and intialize it to metric
Radiobutton(root, text="Imperial", variable=Unit, value="Imperial", command=printResults).pack(anchor='w')
Radiobutton(root, text="Metric", variable=Unit, value="Metric", command=printResults).pack(anchor='w')

#this will be the label for the weight box, it is done in this way so that it can update based on what the user selects as their unit
Weight_Label = Label(root, text="Enter Your Weight:", bg="skyblue")
Weight_Label.pack(anchor="w")

#this is where weight is inputted/variable is stored
Weight = Entry(root)
Weight.pack(anchor="w")

#this will be the label for the height box, it uses the same method as the weight label to make it dynamic
Height_Label = Label(root, text="Enter Your Height:", bg="skyblue")
Height_Label.pack(anchor="w")

#this will be the input area/variable for height
Height = Entry(root)
Height.pack(anchor="w")

#this is the button that a person should press if they want to calculate bmi
Button(root, text="Calculate BMI", command=calcBMI).pack(anchor="w")

#this will display the result in the window
Result = Label(root, text="", bg="skyblue")
Result.pack(anchor="w")

#this will run the application/open the window
root.mainloop()