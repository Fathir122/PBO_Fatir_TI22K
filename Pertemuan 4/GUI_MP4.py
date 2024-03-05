import tkinter as tk
from tkinter import filedialog
from moviepy.editor import VideoFileClip
from threading import Thread

class VideoPlayer:
    def _init_(self, master):
        self.master = master
        self.master.title("Video Player")

        self.video_path = ""
        self.video_clip = None
        self.playing = False

        # UI elements
        self.select_button = tk.Button(master, text="Select Video", command=self.select_video)
        self.select_button.pack(pady=10)

        self.play_button = tk.Button(master, text="Play", command=self.play_video)
        self.play_button.pack(pady=10)

    def select_video(self):
        file_path = filedialog.askopenfilename(title="Pilih File Video", filetypes=[("Video files", ".mp4;.avi;*.mkv")])

        if file_path:
            self.video_path = file_path

    def play_video(self):
        if not self.video_path:
            tk.messagebox.showwarning("Peringatan", "Pilih file video terlebih dahulu!")
            return

        if not self.playing:
            self.playing = True
            self.play_button.config(text="Pause")
            self.video_clip = VideoFileClip(self.video_path)
            self.video_thread = Thread(target=self._play_video_thread)
            self.video_thread.start()
        else:
            self.playing = False
            self.play_button.config(text="Play")

    def _play_video_thread(self):
        self.video_clip.preview()
        self.playing = False
        self.play_button.config(text="Play")

if _name_ == "_main_":
    root = tk.Tk()
    root.geometry("250x100")
    root.resizable(False,False)
    player = VideoPlayer(root)
    root.mainloop(