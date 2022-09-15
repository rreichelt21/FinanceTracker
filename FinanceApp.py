import tkinter as tk 
def create():
    win = tk.Toplevel(root)
root = tk.Tk()
root.geometry('500x200')  
btn = tk.Button(root, text="Create a new window", command = create)
btn.pack(pady = 10) 
root.mainloop()