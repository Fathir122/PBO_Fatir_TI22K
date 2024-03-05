from tkinter import *
import tkinter as tk
from tkinter import filedialog
from pygame import mixer


class MP:
    def _init_(self, win):
        # Create Tkinter window
        win.geometry('250x200')
        win.title('Meh Player')
        win.resizable()

        # StringVar to change button text later
        self.play_restart = tk.StringVar()
        self.pause_resume = tk.StringVar()
        self.play_restart.set('Play')
        self.pause_resume.set('Pause')

        # The buttons and their positions
        load_button = Button(win, text='Load', width=10,
                             font=('Arial', 15), command=self.load)
        load_button.place(x=125, y=40, anchor='center')

        play_button = Button(win, textvariable=self.play_restart, width=10, font=(
            'Arial', 15), command=self.play)
        play_button.place(x=125, y=80, anchor='center')

        pause_button = Button(win, textvariable=self.pause_resume, width=10, font=(
            'Arial', 15), command=self.pause)
        pause_button.place(x=125, y=120, anchor='center')

        stop_button = Button(win, text='Stop', width=10,
                             font=('Arial', 15), command=self.stop)
        stop_button.place(x=125, y=160, anchor='center')

        self.music_file = False
        self.playing_state = False

    def load(self):
        self.music_file = filedialog.askopenfilename()
        print("Loaded: ", self.music_file)
        self.play_restart.set('Play')

    def play(self):
        if self.music_file:
            mixer.init()
            mixer.music.load(str(self.music_file))
            mixer.music.play()
            self.playing_state = False
            self.play_restart.set('Restart')
            self.pause_resume.set('Pause')

    def pause(self):
        if not self.playing_state:
            mixer.music.pause()
            self.playing_state = True
            self.pause_resume.set('Resume')
        else:
            mixer.music.unpause()
            self.playing_state = False
            self.pause_resume.set('Pause')

    def stop(self):
        mixer.music.stop()


root = Tk()
MP(root)
root.mainloop()
