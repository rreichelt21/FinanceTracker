import tkinter as tk 
def create():
    win = tk.Toplevel(root)

root = tk.Tk()
root.wm_title("Finance App")
root.geometry('500x200')  
btn = tk.Button(root, text="Create an account!", command = create)
btn.pack(pady = 10) 
root.mainloop()