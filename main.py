from tkinter import *

window = Tk()
window.title("Body Mass Index")
window.minsize(width=300, height=200)

# Define global variables
value1 = 0
value2 = 0


def weightinput():
    global value1
    value1 = entry_1.get()


def heightinput():
    global value2
    value2 = entry_2.get()


def calculate_bmi():
    global value1, value2

    # Get the values
    weightinput()
    heightinput()

    try:
        # Calculate BMI
        bmi = float(value1) / ((float(value2) / 100) ** 2)

        # Display the result
        label_output.config(text="Your Body Mass Index (BMI): " + str(bmi))
    except ValueError:
        label_output.config(text="Invalid input. Please enter numeric values.")


label_1 = Label(width=20, text="Enter your Weight (kg)")
label_1.pack()
entry_1 = Entry(width=20)
entry_1.pack()

label_2 = Label(width=20, text="Enter your Height (cm)")
label_2.pack()
entry_2 = Entry(width=20)
entry_2.pack()

button = Button(text="Submit", command=calculate_bmi)
button.pack()

label_output = Label(text="")
label_output.pack()

window.mainloop()
