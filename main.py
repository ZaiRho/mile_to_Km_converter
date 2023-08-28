from tkinter import *

kilometer = 0


def calculate():
    global kilometer
    new_text = int(input.get())
    kilometer = new_text * 1.60934
    answer.config(text=f"{kilometer}")


window = Tk()
window.title("Mile to Km Converter")
# window.minsize(width=200, height=100)
window.config(padx=30, pady=30)


#Label
my_label = Label(text="", font=("Arial", 10, "bold"))
my_label.config(text="is equal to")
my_label.grid(column=0, row=1)
my_label.config(padx=10, pady=10)


#Label_miles
miles = Label(text="miles", font=("Arial", 10, "bold"))
miles.grid(column=2, row=1)
miles.config(padx=10, pady=10)


#Label_Km
km = Label(text="Km", font=("Arial", 10, "bold"))
km.grid(column=2, row=1)
km.config(padx=10, pady=10)


#Label_answer
answer = Label(text=f"{kilometer}", font=("Arial", 10, "bold"))
answer.grid(column=1, row=1)
answer.config(padx=10, pady=10)


#Button
button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)


#Entry
input = Entry(width=10)
# print(input.get())
input.grid(column=1, row=0)


window.mainloop()
