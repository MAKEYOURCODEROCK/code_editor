from tkinter import *
import pygame
from tkinter import filedialog
import getpass
import time
from mutagen.mp3 import MP3
import tkinter.ttk as ttk
import os

root = Tk()
root.title("Music Player")
root.geometry("500x400")

pygame.mixer.init()


def download_song():
    pass


def slide(x):
    #slider_label.config(text=f'{int(my_slider.get())} of {int(song_length)}')
    user = getpass.getuser()
    song = song_box.get(ACTIVE)
    song = f'/Users/{user}/.music/{song}.mp3'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0, start=int(my_slider.get()))

def play_time():
    if stopped:
        return 

    current_time = pygame.mixer.music.get_pos() / 1000


    user = getpass.getuser()
    current_song = song_box.curselection()
    song = song_box.get(ACTIVE)
    
    song = f'/Users/{user}/.music/{song}.mp3'
    song_mut = MP3(song)

    global song_length

    song_length = song_mut.info.length
    converted_song_length = time.strftime("%H:%M:%S", time.gmtime(song_length))
    


    #slider_label.config(text=f'Slider: {int(my_slider.get())} and Song Pos: {int(current_time)}')

    converted_current_time = time.strftime("%H:%M:%S", time.gmtime(current_time))

    current_time += 1

    if int(my_slider.get()) == int(song_length):
        status_bar.config(text=f'Time Elapsed: {converted_song_length}')
    elif paused:
        pass
    elif int(my_slider.get()) == int(current_time):
        slider_position = int(song_length)
        my_slider.config(to=slider_position, value=int(current_time))
    else:
        slider_position = int(song_length)
        my_slider.config(to=slider_position, value=int(my_slider.get()))

        converted_current_time = time.strftime("%H:%M:%S", time.gmtime(int(my_slider.get())))

        status_bar.config(text=f'Time Elapsed: {converted_current_time} of {converted_song_length}')

        next_time = int(my_slider.get()) + 1

        my_slider.config(value=next_time)

    #user = getpass.getuser()
    #current_song = song_box.curselection()
    #song = song_box.get(ACTIVE)
    
    #song = f'/Users/{user}/.music/{song}.mp3'
    #song_mut = MP3(song)

    #global song_length

    #song_length = song_mut.info.length
    #converted_song_length = time.strftime("%H:%M:%S", time.gmtime(song_length))


    #status_bar.config(text=f'Time Elapsed: {converted_current_time} of {converted_song_length}')
    #my_slider.config(value=int(current_time))

    #current_time += 1

    #slider_position = int(song_length)
    #my_slider.config(to=slider_position, value=int(current_time))

    status_bar.after(1000, play_time)

def add_song():
    user = getpass.getuser()
    if os.path.exists("/users/" + user + "/.music/") == False:
        os.mkdir("/users/" + user + "/.music/")
    else:
        pass
    song = filedialog.askopenfilename(initialdir="/users/" + user + "/.music/", title="Choose A Song", filetypes=(("mp3 Files", "*.mp3"), ))
    change = str("/Users/" + user + "/.music/")
    song = song.replace(change, "")
    song = song.replace(".mp3", "")
    song_box.insert(END, song)

def add_many_songs():
    user = getpass.getuser()
    songs = filedialog.askopenfilenames(initialdir="/users/" + user + "/.music/", title="Choose A Song", filetypes=(("mp3 Files", "*.mp3"), ))
    
    for song in songs:
        change = str("/Users/" + user + "/.music/")
        song = song.replace(change, "")
        song = song.replace(".mp3", "")
        song_box.insert(END, song)

def play():
    global stopped
    stopped = False
    user = getpass.getuser()
    song = song_box.get(ACTIVE)
    song = f'/Users/{user}/.music/{song}.mp3'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    play_time()

    #slider_position = int(song_length)
    #my_slider.config(to=slider_position, value=0)
global stopped
stopped = False
def stop():
    status_bar.config(text='')
    my_slider.config(value=0)

    pygame.mixer.music.stop()
    song_box.selection_clear(ACTIVE)

    status_bar.config(text='')

    global stopped
    stopped = True

def next_song():
    slider_position = int(song_length)
    my_slider.config(to=slider_position, value=0)
    user = getpass.getuser()
    next_one = song_box.curselection()
    next_one = next_one[0] + 1
    song = song_box.get(next_one)
    
    song = f'/Users/{user}/.music/{song}.mp3'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    song_box.selection_clear(0, END)

    song_box.activate(next_one)

    song_box.selection_set(next_one, last=None)


def prev_song():
    slider_position = int(song_length)
    my_slider.config(to=slider_position, value=0)
    user = getpass.getuser()
    next_one = song_box.curselection()
    next_one = next_one[0] - 1
    song = song_box.get(next_one)
    
    song = f'/Users/{user}/.music/{song}.mp3'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    song_box.selection_clear(0, END)

    song_box.activate(next_one)

    song_box.selection_set(next_one, last=None)

def delete_song():
    stop()
    song_box.delete(ANCHOR)
    pygame.mixer.music.stop()

def delete_all_songs():
    stop()
    song_box.delete(0, END)
    pygame.mixer.music.stop()

global pasued
paused = False

def pause(is_paused):
    global paused
    paused = is_paused

    if paused:
        pygame.mixer.music.unpause()
        paused = False
    else:
        pygame.mixer.music.pause()
        paused = True


song_box = Listbox(root, bg="black", fg="green", width=60, selectbackground="gray", selectforeground="black")
song_box.pack(pady=20)


back_btn_img = PhotoImage(file="images/back.png")
forward_btn_img = PhotoImage(file="images/forward.png")
play_btn_img = PhotoImage(file="images/play.png")
pause_btn_img = PhotoImage(file="images/pause.png")
stop_btn_img = PhotoImage(file="images/stop.png")


controls_frame = Frame(root)
controls_frame.pack()

back_button = Button(controls_frame, image=back_btn_img, borderwidth=0, command=prev_song)
forward_button = Button(controls_frame, image=forward_btn_img, borderwidth=0, command=next_song)
play_button = Button(controls_frame, image=play_btn_img, borderwidth=0, command=play)
pause_button = Button(controls_frame, image=pause_btn_img, borderwidth=0, command=lambda: pause(paused))
stop_button = Button(controls_frame, image=stop_btn_img, borderwidth=0, command=stop)

back_button.grid(row=0, column=0 ,padx=10)
forward_button.grid(row=0, column=1 ,padx=10)
play_button.grid(row=0, column=2 ,padx=10)
pause_button.grid(row=0, column=3 ,padx=10)
stop_button.grid(row=0, column=4 ,padx=10)


my_menu = Menu(root)
root.config(menu=my_menu)


add_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Music", menu=add_song_menu)
add_song_menu.add_command(label="Add One Song To Playlist", command=add_song)
add_song_menu.add_command(label="Add Multiple Songs", command=add_many_songs)
add_song_menu.add_command(label="Download Songs", command=download_song())

remove_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Remove Songs", menu=remove_song_menu)
remove_song_menu.add_command(label="Delete A Song From The Playlist", command=delete_song)
remove_song_menu.add_command(label="Delete All Songs From Playlist", command=delete_all_songs)


status_bar = Label(root, text="", bd=1, relief=GROOVE, anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=2)


my_slider = ttk.Scale(root, from_=0, to=100, orient=HORIZONTAL, value=0, command=slide, length=360)
my_slider.pack(pady=30)

#slider_label = Label(root, text="0")
#slider_label.pack(pady=10)

root.mainloop()