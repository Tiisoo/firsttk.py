import tkinter as tk
from tkinter import ttk
window = tk.Tk()
label =ttk.Label(window,text="enter two inputs")
numb1_entry =ttk.Entry(window)
numb2_entry =ttk.Entry(window)
numb1_entry.grid(row=5,column=2,padx=4)
numb2_entry.grid(rows=5,column=2,padx=4)
def add_numbers():
  try:
    numb1 =int(numb1_entry.get())
    numb2 =int(numb2_entry.get())
    result = numb1+numb2
    result_label.config(text=f"result:{result}")
  except:
    result_label.config(text=f"wrong input")
add_button =ttk.Button(window,text="add",command=add_numbers)
add_button.grid(row=3,column=0,padx=5)
result_label=ttk.Label(window,text="result")
result_label.grid(row=3,column=0,padx=5)
window.mainloop()