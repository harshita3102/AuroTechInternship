import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import time

class TimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Timer and Stopwatch")
        self.root.geometry("400x300")
        self.root.configure(bg="#282c34")

        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("TButton", background="#61afef", foreground="white", font=("Helvetica", 12))
        self.style.configure("TLabel", background="#282c34", foreground="white", font=("Helvetica", 24))
        self.style.configure("TEntry", font=("Helvetica", 12))
        self.style.map("TButton", background=[("active", "#61afef")])

        self.running = False
        self.start_time = 0
        self.elapsed_time = 0
        self.total_time = 0

        self.timer_label = ttk.Label(root, text="00:00:00")
        self.timer_label.pack(pady=20)

        self.buttons_frame = tk.Frame(root, bg="#282c34")
        self.buttons_frame.pack(pady=10)

        self.start_button = ttk.Button(self.buttons_frame, text="Start", command=self.start)
        self.start_button.grid(row=0, column=0, padx=10)

        self.stop_button = ttk.Button(self.buttons_frame, text="Stop", command=self.stop)
        self.stop_button.grid(row=0, column=1, padx=10)

        self.reset_button = ttk.Button(self.buttons_frame, text="Reset", command=self.reset)
        self.reset_button.grid(row=0, column=2, padx=10)

        self.mode = tk.StringVar(value="stopwatch")
        self.mode_menu = ttk.OptionMenu(root, self.mode, "stopwatch", "stopwatch", "countdown", command=self.change_mode)
        self.mode_menu.pack(pady=10)

        self.countdown_entry = ttk.Entry(root, width=10)
        self.countdown_entry.pack(pady=10)
        self.countdown_entry.insert(0, "00:00:00")
        self.countdown_entry.pack_forget()

    def change_mode(self, mode):
        if mode == "countdown":
            self.countdown_entry.pack(pady=10)
        else:
            self.countdown_entry.pack_forget()
            self.timer_label.config(text="00:00:00")
            self.elapsed_time = 0
            self.total_time = 0

    def start(self):
        if not self.running:
            if self.mode.get() == "countdown":
                time_str = self.countdown_entry.get()
                self.total_time = self.convert_to_seconds(time_str)
                self.elapsed_time = self.total_time
                self.countdown_entry.pack_forget()
            self.running = True
            self.start_time = time.time() - (self.total_time - self.elapsed_time)
            self.update_timer()

    def stop(self):
        if self.running:
            self.running = False
            self.elapsed_time = self.total_time - (time.time() - self.start_time)

    def reset(self):
        self.running = False
        self.elapsed_time = 0
        self.total_time = 0
        self.timer_label.config(text="00:00:00")
        if self.mode.get() == "countdown":
            self.countdown_entry.pack(pady=10)

    def update_timer(self):
        if self.running:
            if self.mode.get() == "countdown":
                self.elapsed_time = self.total_time - (time.time() - self.start_time)
                if self.elapsed_time <= 0:
                    self.timer_label.config(text="00:00:00")
                    self.running = False
                    messagebox.showinfo("Time's up", "Countdown finished!")
                else:
                    self.timer_label.config(text=self.convert_to_time_str(self.elapsed_time))
            else:
                self.elapsed_time = time.time() - self.start_time
                self.timer_label.config(text=self.convert_to_time_str(self.elapsed_time))
            self.root.after(1000, self.update_timer)

    def convert_to_seconds(self, time_str):
        h, m, s = map(int, time_str.split(":"))
        return h * 3600 + m * 60 + s

    def convert_to_time_str(self, seconds):
        h = int(seconds // 3600)
        m = int((seconds % 3600) // 60)
        s = int(seconds % 60)
        return f"{h:02}:{m:02}:{s:02}"

if __name__ == "__main__":
    root = tk.Tk()
    app = TimerApp(root)
    root.mainloop()

