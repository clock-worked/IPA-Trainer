"""
IPA Trainer

This program is a simple tool to help you learn the International Phonetic Alphabet (IPA).
A random word in IPA is displayed in a label. Under the label is a progress bar that
counts down from 10 seconds. Below the progress bar is a text entry box where you can
type in your answer. When you press the "Submit" button or press enter, the program will check your
answer. If the answer is correct, color of the word will flash green and a new word will be displayed.
If the answer is incorrect, the word will flash red. If the timer runs out, the word will flash red and
a new word will be displayed. The program will keep track of how many words you get correct and how 
many you get incorrect. It will display your stats at the top of the window.

A file called "words.txt" must be in the same directory as this program. The file should contain
a list of words, one word per line. The program will use this file to generate random words.

There is also a file called "ipa.txt" that already contains the IPA for the words in "words.txt".

The program will start by creating a frame called Start with a button in the center. When the button is clicked,
the frame will be destroyed and the game frame and the stats frame will be created. The game frame will contain
the word label, progress bar, entry box, and submit button. The stats frame will contain the stats.

The stats frame will be a thin bar at the top of the window. It will contain the number of correct answers,
the number of incorrect answers, and in the center the current streak. The streak is the number of correct
answers in a row. If you get an incorrect answer, the streak will reset to 0.
"""

import customtkinter as ctk
import tkinter as tk
import random


class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("IPA Trainer")
        self.geometry("500x300")
        
        self.words = []
        self.ipa = []
        self.guess = tk.StringVar(value="")
        self.current_ipa = tk.StringVar(value="")
        self.current_word = tk.StringVar(value="Word")
        self.correct = tk.IntVar(value=0)
        self.incorrect = tk.IntVar(value=0)
        self.streak = tk.IntVar(value=0)
        self.progress = 0
        self.isGameRunning = False
        
        # Load the words and IPA
        self.load_words()
        self.load_ipa()
        
        # Create the start frame
        self.create_start_frame()
        
        # Set trace on the guess variable
        self.guess.trace("w", self.guess_changed)
        
        self.after(100, self.is_progress_done)
                
    def load_words(self):
        # Load from file
        with open("words.txt", "r", encoding="utf-8") as f:
            for line in f:
                self.words.append(line.strip())
                
    def load_ipa(self):
        # Load from file
        with open("ipa.txt", "r", encoding="utf-8") as f:
            for line in f:
                self.ipa.append(line.strip())
                
    def create_start_frame(self):
        self.start_frame = ctk.CTkFrame(self)
        self.start_frame.pack(fill="both", expand=True)
        
        self.start_button = ctk.CTkButton(self.start_frame, 
                                          text="Start", command=self.start)
        self.start_button.pack(fill="x", expand=True, padx=20)
        
    def start(self):
        self.start_frame.destroy()
        self.create_stats_frame()
        self.create_game_frame()
        
        self.isGameRunning = True
        self.next_word()

        
    def create_game_frame(self):
        self.game_frame = ctk.CTkFrame(self)
        self.game_frame.pack(fill="both", expand=True, pady=[0,10], padx=10)
        
        self.ipa_and_progress_frame = ctk.CTkFrame(self.game_frame)
        self.ipa_and_progress_frame.pack(fill="both", expand=True)
        
        self.ipa_label = ctk.CTkLabel(self.ipa_and_progress_frame, textvariable=self.current_ipa, font=("Arial", 32))
        self.ipa_label.pack(fill="both", expand=True, pady=10)
        
        # Create the progress bar and color it green
        self.progress_bar = ctk.CTkProgressBar(self.ipa_and_progress_frame)
        self.progress_bar.configure(mode="determinate", determinate_speed=0.1, progress_color="green")
        
        self.progress_bar.pack(fill="x", expand=True, pady=[10, 0], padx=20, side="bottom")
        
        self.entry = ctk.CTkEntry(self.game_frame, textvariable=self.guess)
        self.entry.pack(fill="both", expand=True, pady=5)
        
        self.submit_button = ctk.CTkButton(self.game_frame, text="Submit", command=self.submit)
        self.submit_button.pack(fill="both", expand=True)
        
        self.entry.bind("<Return>", self.submit)
        
    def create_stats_frame(self):
        self.stats_frame = ctk.CTkFrame(self)
        
        # Stats frame will be a thin bar at the top of the window
        # 3 frames will be placed inside the stats frame in a grid 
        # The first frame will contain the number of correct answers
        
        # Configure rows and columns
        self.stats_frame.grid_columnconfigure(0, weight=1)
        self.stats_frame.grid_columnconfigure(1, weight=1)
        self.stats_frame.grid_columnconfigure(2, weight=1)
        
        self.correct_frame = ctk.CTkFrame(self.stats_frame)
        
        self.correct_label = ctk.CTkLabel(self.correct_frame, text="Correct:", font=("Arial", 12))
        self.correct_label.pack(fill="x", padx=(0, 5))
        
        self.correct_count = ctk.CTkLabel(self.correct_frame, 
                                          textvariable=self.correct , 
                                          font=("Arial", 25), text_color="#4AB19D")
        self.correct_count.pack(fill="x", padx=(0, 5))
        
        self.correct_frame.grid(row=0, column=0, sticky="new")
        
        # The frame will contain the current streak
        self.streak_frame = ctk.CTkFrame(self.stats_frame)
        
        self.streak_label = ctk.CTkLabel(self.streak_frame, text="Streak:", font=("Arial", 12))
        self.streak_label.pack(fill="x", padx=(0, 5))
        
        self.streak_count = ctk.CTkLabel(self.streak_frame, 
                                         textvariable=self.streak, 
                                         font=("Arial", 25))
        self.streak_count.pack(fill="x", padx=(0, 5))
        
        self.streak_frame.grid(row=0, column=1, sticky="new")
        
        # The frame will contain the number of incorrect answers
        self.incorrect_frame = ctk.CTkFrame(self.stats_frame)

        self.incorrect_label = ctk.CTkLabel(self.incorrect_frame, text="Incorrect:", font=("Arial", 12))
        self.incorrect_label.pack(fill="x", padx=(0, 5))
        
        self.incorrect_count = ctk.CTkLabel(self.incorrect_frame, 
                                            textvariable=self.incorrect, 
                                            font=("Arial", 25), text_color="#EF3D59")
        self.incorrect_count.pack(fill="x", padx=(0, 5))
        
        self.incorrect_frame.grid(row=0, column=2, sticky="new")
        
        self.stats_frame.pack(fill="x", side="top", padx=10, pady=[10, 0])
        
    def guess_changed(self, *args):
        if self.isGameRunning:
            if self.guess.get().lower() == self.current_word.get().lower():
                self.handle_correct()

    def next_word(self): 
        # Reset the entry
        self.guess.set("")
        
        # Get a random number between 0 and the length of the words list
        index = random.randint(0, len(self.words) - 1)
        
        # Get the word and IPA at that index
        self.current_word.set(self.words[index])
        self.current_ipa.set(self.ipa[index])
        
        # Start the progress bar
        self.progress_bar.set(0)
        self.progress_bar.start()
        
        self.isGameRunning = True
        
        self.update_idletasks()
        
    def submit(self, event=None):
        if self.isGameRunning:
            if self.guess.get().lower() == self.current_word.get().lower():
                self.handle_correct()
            else:
                self.handle_incorrect()

    def handle_incorrect(self):
        self.progress_bar.stop()
        self.isGameRunning = False
        
        self.flash_red()
        self.streak.set(0)
        self.incorrect.set(self.incorrect.get() + 1)
        
        # Set the ipa label to the correct answer
        self.current_ipa.set(self.current_word.get())
        
        self.update_idletasks()
        
        # Wait 1 second then generate a new word
        self.after(1000, self.next_word)
        
    def handle_correct(self):
        self.progress_bar.stop()
        self.isGameRunning = False
        
        self.correct.set(self.correct.get() + 1)
        self.streak.set(self.streak.get() + 1)
        
        self.flash_green()
        self.next_word()
        
    def flash_green(self):
        self.ipa_label.configure(text_color="green")
        self.after(100, self.reset_color)
        
    def flash_red(self):
        self.ipa_label.configure(text_color="red")
        self.after(1000, self.reset_color)
        
    def reset_color(self):
        self.ipa_label.configure(text_color="black")

    def color_map(self, start_color, end_color, num):
        # Convert the hex colors to RGB
        start_rgb = tuple(int(start_color[i:i+2], 16) for i in (1, 3, 5))
        end_rgb = tuple(int(end_color[i:i+2], 16) for i in (1, 3, 5))

        # Calculate a color for each step between the start and end colors
        color_range = [(int(start_rgb[i] + (float(num)/100) * (end_rgb[i] - start_rgb[i]))) for i in range(3)]

        # Convert the calculated color back to hex
        intermediate_color = '#%02x%02x%02x' % tuple(color_range)

        return intermediate_color
        
    def is_progress_done(self):
        if self.isGameRunning:
            self.progress = self.progress_bar.get()
            
            color = self.color_map('#4AB19D', '#EF3D59', round(self.progress * 100))

            self.progress_bar.configure(progress_color=color)
            
            if self.progress > 0.99:
                self.handle_incorrect()
                
        self.after(100, self.is_progress_done)
            
if __name__ == "__main__":
    app = App()
    app.mainloop()
    
    
