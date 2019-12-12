from pygame import mixer
from tkinter import *
import os
import random

class Music_Player:
    def __init__(self):
        self.cur_path = os.getcwd()+'\\downloads'
        self.filelist = []
        self.playlist = []
        self.ispause = False
        self.loop_play_times = 0
        self.isloop_play = False
        self.count = 0
        self.is_next_song = False
        self.volume = 0.3
        self.israndom_play = False
        self.nowplaying = str()
        
        mixer.init()
        self.window = Tk()
        self.window.geometry("800x380")
        self.window.title("mp3 player")
        
        frame1 = Frame(self.window)
        frame1.pack()
        
        file_tree = os.walk(self.cur_path)
        #print(file_tree)
        for i,j,files in file_tree:
            self.filelist = files
        
        print(self.filelist)
    
        for file_index in range(len(self.filelist)):
            self.filelist[file_index] = 'downloads\\'+ self.filelist[file_index]
            
        self.playlist = self.filelist+[]
        #print(self.filelist)
        
        self.pause_text = StringVar()
        self.pause_text.set("play" if self.ispause else "pause")
        self.loop_text = StringVar()
        self.loop_text.set("single play" if self.isloop_play else "loop play")
        self.random_text = StringVar()
        self.random_text.set("order play" if self.israndom_play else "random play")
        self.label_text = StringVar()
        
        
        button1 = Button(frame1, textvariable = self.pause_text , width = 20 , command = self.pause)
        button1.grid(row = 0, column = 0, padx = 5, pady = 5)
        button2 = Button(frame1, textvariable = self.loop_text , width = 20, command = self.loop_play)
        button2.grid(row = 0, column = 1, padx = 5, pady = 5)
        button3 = Button(frame1, textvariable = self.random_text , width = 20, command = self.random_play)
        button3.grid(row = 0, column = 2, padx = 5, pady = 5)
        button4 = Button(frame1, text = "next song", width = 20, command = self.next_song)
        button4.grid(row = 0, column = 3, padx = 5, pady = 5)
        
        frame2 = Frame(self.window)
        frame2.pack()
        label = Label(frame2,textvariable = self.label_text)
        label.pack()
        
        mixer.music.load(self.playlist[self.count])
        mixer.music.play(loops = 0)
        self.nowplaying = self.playlist[self.count]
        self.label_text.set(self.nowplaying)
        
        
        
        self.window.protocol("WM_DELETE_WINDOW",self.stop)
        self.window.mainloop()
        
        
                
                
    def counter(self):
        if self.count == len(self.playlist)-1 or self.isloop_play:
            self.count = 0
        else:
            self.count += 1
    
    def random_play(self):
        if not self.israndom_play:
            
            random.shuffle(self.playlist)
            self.label_text.set(self.nowplaying)
            self.israndom_play = True
            
        else:
            self.playlist = self.filelist
            self.count = self.playlist.index(self.nowplaying)
            self.israndom_play = False
        
        self.random_text.set("order play" if self.israndom_play else "random play")
        
    def pause(self):
        if self.is_next_song:
            self.is_next_song = False
        
        if not self.ispause:
            mixer.music.pause()
            self.ispause = True
        else:
            mixer.music.unpause()
            self.ispause = False
            
        self.pause_text.set("play" if self.ispause else "pause")
        
        
    def next_song(self):
        self.ispause = False
        self.pause_text.set("play" if self.ispause else "pause")
        mixer.music.stop()
        self.counter()
        mixer.music.load(self.playlist[self.count])
        mixer.music.play(loops = 0)
        self.nowplaying = self.playlist[self.count]
        self.label_text.set(self.nowplaying)
        
    def loop_play(self):
        if self.isloop_play:
            self.playlist = self.filelist
            self.count = self.playlist.index(self.nowplaying)
            self.isloop_play = False
        else:
            self.playlist = [self.nowplaying]
            self.isloop_play = True
        
        self.loop_text.set("single play" if self.isloop_play else "loop play")
        
    def set_volume(self,volume):
        mixer.music.set_volume(volume/100)
        
    def stop(self):
        mixer.music.stop()
        self.window.destroy()
        

Music_Player()