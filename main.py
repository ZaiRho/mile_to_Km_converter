from tkinter import *

kilometer = 0


def button_clicked():
    global kilometer
    new_text = int(input.get())
    kilometer = new_text * 1.60934
    answer.config(text=f"{kilometer}")


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=200)
window.config(padx=50, pady=50)


#Label
my_label = Label(text="", font=("Arial", 10, "bold"))
my_label.config(text="is equal to")
my_label.grid(column=1, row=2)
my_label.config(padx=10, pady=10)


#Label_miles
miles = Label(text="miles", font=("Arial", 10, "bold"))
miles.grid(column=3, row=1)
miles.config(padx=10, pady=10)


#Label_Km
km = Label(text="Km", font=("Arial", 10, "bold"))
km.grid(column=3, row=2)
km.config(padx=10, pady=10)


#Label_answer
answer = Label(text=f"{kilometer}", font=("Arial", 10, "bold"))
answer.grid(column=2, row=2)
answer.config(padx=10, pady=10)


#Button
button = Button(text="Calculate", command=button_clicked)
button.grid(column=2, row=3)

# new_button = Button(text="New Button")
# new_button.grid(column=2, row=0)

#Entry
input = Entry(width=10)
# print(input.get())
input.grid(column=2, row=1)









window.mainloop()