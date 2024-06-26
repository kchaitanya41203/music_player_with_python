import tkinter as tkr
import fnmatch
import os
from pygame import mixer

music=tkr.Tk()
music.title("music player")
music.geometry("600x900")
music.config(bg= 'black')

roothpath = "D:\\CHAIT\mpyth"
pattern="*.mp3"

mixer.init()

def select():
    label.config(text = l_Box.get("anchor"))
    mixer.music.load(roothpath + "\\" + l_Box.get("anchor"))
    mixer.music.play()
    
def pause():
    mixer.music.pause()
    
def unpause(): 
    mixer.music.unpause()

def play_prev():
    next_song = l_Box.curselection()
    next_song = next_song[0] - 1
    next_song_name = l_Box.get(next_song)
    label.config(text = next_song_name)

    mixer.music.load(roothpath + "\\" + next_song_name)
    mixer.music.play()

    l_Box.select_clear(0, 'end')
    l_Box.activate(next_song)
    l_Box.select_set(next_song)
    
def forward_next():
    next_song = l_Box.curselection()
    next_song = next_song[0] + 1
    next_song_name = l_Box.get(next_song)
    label.config(text = next_song_name)

    mixer.music.load(roothpath + "\\" + next_song_name)
    mixer.music.play()

    l_Box.select_clear(0, 'end')
    l_Box.activate(next_song)
    l_Box.select_set(next_song)
    
l_Box=tkr.Listbox(music,fg="black",bg="white",width=100,font="Calibri")
l_Box.pack(padx = 15, pady = 15)

label=tkr.Label(music,text='',fg="yellow",bg="black",width=100,height=3,font="Elephant")
label.pack(pady = 15)

b1=tkr.Button(music,width=100,height=4,font="Elephant",text="prev",command=play_prev,bg="black",fg="white").pack()
b2=tkr.Button(music,width=100,height=4,font="Elephant",text="play",bg="black",command=select,fg="white").pack()
b3=tkr.Button(music,width=100,height=4,font="Elephant",text="pause",bg="black",command=pause,fg="white").pack()
b4=tkr.Button(music,width=100,height=4,font="Elephant",text="forward_next",bg="black",command=forward_next,fg="white").pack()
b5=tkr.Button(music,width=100,height=4,font="Elephant",text="unpause",bg="black",command=unpause,fg="white").pack()

for root, dirs, files in os.walk(roothpath):
    for filename in fnmatch.filter(files,pattern):
        l_Box.insert('end', filename)

music.mainloop()