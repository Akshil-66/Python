# import some libraries and modules

import time
import tkinter as tk

root = tk.Tk()
root.title("Standard Digital Clock")

def currentTime():
    # find current time and display on the clock
    # update the time in every 1000 miliseconds
    string = time.strftime('%H:%M:%S %p \n %D')
    label.config(text=string)
    label.after(1000,currentTime)

label = tk.Label(
    root,
    font = ('calibri' , 60 , 'bold'),
    background='pink',
    foreground='black'
)

label.pack(anchor='center')

currentTime()

root.mainloop()