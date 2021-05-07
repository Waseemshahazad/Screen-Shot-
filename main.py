import pyautogui
from tkinter import filedialog
import tkinter as tk
from tkinter.messagebox import askyesno

root = tk.Tk()
root.title('Screen Shot')

canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()


def takeScreenshot():
    shot = pyautogui.screenshot()
    file_path = filedialog.asksaveasfilename(defaultextension='.png')
    shot.save(file_path)


def Exit():
    answer = askyesno(title='confirmation', message='Are you sure that you want to quit')
    if answer:
        root.destroy()


btn = tk.Button(text='Screen Shot', command=takeScreenshot, bg='yellow', fg= 'black', font=12)
canvas.create_window(150, 140, window=btn)


btn = tk.Button(text='Exit Window', command=Exit, bg='yellow', fg= 'black', font=12)
canvas.create_window(150, 180, window=btn)

root.mainloop()