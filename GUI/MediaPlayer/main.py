import tkinter as tk
from pygame import mixer
from tkinter import filedialog
from tkinter import messagebox

"""
    https://www.youtube.com/playlist?list=PLhTjy8cBISEp6lNKUO3iwbB1DKAkRwutl
"""
root = tk.Tk()

mixer.init()
mixer.music.set_volume(0.15)

def play_file(file):
    try:
        paused
        print("Inside try")
    except NameError:
        print("Inside except")
        try:
            mixer.music.load(file)
            mixer.music.play()
        except:
            print("Wrong media file format\n[" + file + "]")
            tk.messagebox.showerror("File error", "Wrong media file format\n[" + file + "]")
    else:
        print("Inside else")
        mixer.music.unpause()
        statusbar['text'] = "Music resumed"

def play():
    play_file('media/song1.mp3')
    statusbar['text'] = "Music play"

def stop():
    mixer.music.stop()
    statusbar['text'] = "Music stoped"

def pause():
    global paused
    paused = True
    mixer.music.pause()
    statusbar['text'] = "Music paused"

def set_media_volume(val):
    volume = int(val) / 100
    mixer.music.set_volume(volume)

def browse_file():
    print("Get file")
    fileName = filedialog.askopenfilename()
    play_file(fileName)

root.title('Media player')
root.iconbitmap('img/app.ico')

menubar = tk.Menu(root)
root.config(menu=menubar)

# --------------------------------------------------------------------------
menu_file = tk.Menu(menubar, tearoff=0)
menu_file.add_command(label="Open", command=browse_file)
menu_file.add_command(label="Exit", command=root.destroy)
menubar.add_cascade(label='File', menu=menu_file)

# --------------------------------------------------------------------------

frame_buttons = tk.Frame(root)

# --------------------------------------------------------------------------
lbl_msg = tk.Label(root, text='Music is life')

# --------------------------------------------------------------------------
img_play = tk.PhotoImage(file='img/play.png')
btn_play = tk.Button(frame_buttons, text='', image=img_play, command=play)

img_stop = tk.PhotoImage(file='img/stop.png')
btn_stop = tk.Button(frame_buttons, text='', image=img_stop, command=stop)

img_pause = tk.PhotoImage(file='img/pause.png')
btn_pause = tk.Button(frame_buttons, text='', image=img_pause, command=pause)

# --------------------------------------------------------------------------
scale_volum = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, command=set_media_volume)
scale_volum.set(15)

# --------------------------------------------------------------------------
statusbar = tk.Label(root, text='Welcom to Media player', bg='yellow')

# --------------------------------------------------------------------------
btn_play.grid(row=2, column=0, padx=5)
btn_stop.grid(row=2, column=2, padx=5)
btn_pause.grid(row=2, column=4, padx=5)

lbl_msg.grid(row=0, column=0, columnspan=10, pady=15)
frame_buttons.grid(row=2, column=0, columnspan=8, padx=15)
scale_volum.grid(row=3, column=0, columnspan=10, pady=10)
statusbar.grid(row=99, column=0, columnspan=10, sticky=tk.S)

root.mainloop()
