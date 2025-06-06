# use of tkinter
import tkinter as tk

window =tk.Tk()

window.title("My First GUI Program")
# draw a label
my_label = tk.Label(text="My Name Rajesh Kumar", font=("Arial", 20, "bold"))
my_label.pack()
my_label["text"] = "Rajesh Kumar Verma"
my_label.config(text="Rajesh Kumar Verma")


# Button
def button_click():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)

button = tk.Button(text="Click Me" , command=button_click)
button.pack()

# Entry
input = tk.Entry(width=30)
input.pack()
print(input.get())




window.minsize(width=500, height=300)




window.mainloop()