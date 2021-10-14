import tkinter as tk

def check():
    id = inp.get()
    if(id == "nguyen" or id == "Nguyen"):
        res.configure(text=str(inp.get() + " is my last name."))
    elif(id.isdigit() and id == "2729679"):
        res.configure(text=str(inp.get() + " is my ID."))
    else:
        res.configure(text=str(inp.get() + " is not valid."))

master = tk.Tk()
master.geometry("600x400")
tk.Label(master, text="Please enter my ID or my last name: ").pack()
inp = tk.Entry(master)
inp.pack()
res = tk.Label(master)
res.pack()
tk.Button(master, text="Check",command=check).pack()
tk.mainloop()