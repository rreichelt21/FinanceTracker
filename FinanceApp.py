import tkinter as tk
import Creditcards

app = tk.Tk()
app.title("Finance App")
app.configure(bg = "black", width = 500, height = 500)

Label = tk.Label(text="Welcome to the Finance App",
                bg="black", fg="white", font="none 12 bold")

Button1 = tk.Button(text="Credit Cards", bg = "white", fg = "black", 
                    font = "none 15 bold", width = 10, height = 1)                

# Button2 = tk.Button(text="Account Balance", bg = "white", fg = "black", 
#                     font = "none 15 bold", width = 15, height = 1)

# Button3 = tk.Button(text="Finance Tracking", bg = "white", fg = "black", 
#                     font = "none 15 bold", width = 15, height = 1)

Label.pack()
Button1.pack()
# Button2.pack()
# Button3.pack()
app.mainloop()