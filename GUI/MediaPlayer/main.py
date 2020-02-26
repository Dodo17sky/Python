import tkinter as tk
from pygame import mixer
from tkinter import filedialog
from tkinter import messagebox

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

def pause():
    global paused
    paused = True
    mixer.music.pause()
    statusbar['text'] = "Music stoped"

def set_media_volume(val):
    volume = int(val) / 100
    mixer.music.set_volume(volume)

def browse_file():
    print("Get file")
    fileName = filedialog.askopenfilename()
    play_file(fileName)

root.title('Media player')
root.iconbitmap('img/app.ico')
root.geometry('600x400')

menubar = tk.Menu(root)
root.config(menu=menubar)

# --------------------------------------------------------------------------
menu_file = tk.Menu(menubar, tearoff=0)
menu_file.add_command(label="Open", command=browse_file)
menu_file.add_command(label="Exit", command=root.destroy)
menubar.add_cascade(label='File', menu=menu_file)

# --------------------------------------------------------------------------
img_piano = tk.PhotoImage(file='img/piano.png')
lbl_msg = tk.Label(root, text='Welcome to Media player')
lbl_img_piano = tk.Label(root, image=img_piano)

# --------------------------------------------------------------------------
img_play = tk.PhotoImage(file='img/play.png')
btn_play = tk.Button(root, text='', image=img_play, command=play)

img_pause = tk.PhotoImage(file='img/pause.png')
btn_pause = tk.Button(root, text='', image=img_pause, command=pause)

# --------------------------------------------------------------------------
scale_volum = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, command=set_media_volume)
scale_volum.set(15)

# --------------------------------------------------------------------------
statusbar = tk.Label(root, text='Welcom to Media player', bg='yellow')

# --------------------------------------------------------------------------
lbl_msg.grid(row=0, column=0, columnspan=10)
lbl_img_piano.grid(row=1, column=0, columnspan=10)
btn_play.grid(row=2, column=0)
btn_pause.grid(row=2, column=3)
scale_volum.grid(row=3, column=0, columnspan=3)
statusbar.grid(row=99, column=0, columnspan=10, sticky=tk.S)

root.mainloop()
