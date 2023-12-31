import time
import sys
import random
from datetime import datetime
from tkinter import *
from PIL import ImageTk

tk=Tk()
w=800
h=600
tk.overrideredirect(1)
tk.geometry("%dx%d+0+0" % (w, h))
tk.focus_set()
tk.config(bg="black")
tk.bind("<Enter>", lambda e: e.widget.quit())
tk.bind("<Escape>", exit)


canvas = Canvas(tk, width=800, height=600, bg='green')


image = ImageTk.PhotoImage(file = "firework.gif")
canvas.create_image(0, 0, image = image, anchor = NW)
canvas.create_text(400, 110, text="New Year Countdown",
                       fill='white', font=('Times', 50))


canvas.pack(expand = YES, fill = BOTH)


def exit(event):
    sys.exit()

def update():
    global canvas, tk, t1, t2

    try:
        canvas.delete(t1)
        canvas.delete(t2)
    except:
        pass
    
    days = str(31 - int(datetime.now().strftime('%d')))
    hours = str(23 - int(datetime.now().strftime('%H')))
    mins = str(59 - int(datetime.now().strftime('%M')))
    secs = str(59 - int(datetime.now().strftime('%S')))

    time_str = days+' days '+hours+' hours '
    t1=canvas.create_text(400, 410, text=time_str,
                       fill='white', font=('Times', 50))
    time_str = mins+' mins '+secs+' seconds'
    t2=canvas.create_text(400, 490, text=time_str,
                       fill='white', font=('Times', 50))
    tk.update_idletasks() 
    tk.update()



try:
    while 1:
        update()
        time.sleep(0.05)
except:
    pass

