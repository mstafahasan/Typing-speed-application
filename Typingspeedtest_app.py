import tkinter as tk
from tkinter import messagebox
import time
import random

# Sample sentences for the typing test
SAMPLE_TEXTS = [
    "The quick brown fox jumps over the lazy dog as we here.",
    "Python is an interpreted, high-level programming language.",
    "Typing fast and accurately is a valuable skill.",
    "Artificial intelligence will revolutionize technology.",
    "Practice makes perfect, especially in typing speed tests."
]

class TypingSpeedTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")
        self.root.geometry("700x400")
        self.root.config(bg="#f0f0f0")
        
        self.sample_text = random.choice(SAMPLE_TEXTS)
        self.start_time = None
        self.history = []  # To store history

        # Sample text display
        self.sample_text_label = tk.Label(root, text="Type the following text:", font=("Arial", 14), bg="#f0f0f0")
        self.sample_text_label.pack(pady=10)

        self.text_display = tk.Label(root, text=self.sample_text, wraplength=600, font=("Arial", 14), bg="white", bd=1, relief="solid")
        self.text_display.pack(pady=10, padx=20, fill="x")

        # Typing area
        self.input_text = tk.Text(root, height=5, width=60, font=("Arial", 12), wrap="word")
        self.input_text.pack(pady=10)
        
        # Buttons
        self.start_button = tk.Button(root, text="Start", command=self.start_test, font=("Arial", 12), bg="#4CAF50", fg="white", width=10)
        self.start_button.pack(pady=5)

        self.history_button = tk.Button(root, text="Show History", command=self.show_history, font=("Arial", 12), bg="#2196F3", fg="white", width=12)
        self.history_button.pack(pady=5)

        # Result display
        self.result_label = tk.Label(root, text="", font=("Arial", 14), bg="#f0f0f0")
        self.result_label.pack(pady=20)

    def start_test(self):
        # Reset and start a new test
        self.input_text.delete(1.0, tk.END)
        self.input_text.focus()
        
        # Choose a new sentence and reset UI
        self.sample_text = random.choice(SAMPLE_TEXTS)
        self.text_display.config(text=self.sample_text)
        self.result_label.config(text="")
        
        # Start timer and change button to submit
        self.start_time = time.time()
        self.start_button.config(text="Submit", command=self.calculate_speed)
    
    def calculate_speed(self):
        if not self.start_time:
            return
        
        # Calculate the elapsed time
        end_time = time.time()
        elapsed_time = end_time - self.start_time
        
        # Get typed text and calculate Words Per Minute (WPM)
        typed_text = self.input_text.get(1.0, tk.END).strip()
        word_count = len(typed_text.split())
        wpm = (word_count / elapsed_time) * 60

        # Calculate accuracy
        sample_words = self.sample_text.split()
        typed_words = typed_text.split()
        correct_words = sum(1 for i, word in enumerate(typed_words) if i < len(sample_words) and word == sample_words[i])
        accuracy = (correct_words / len(sample_words)) * 100

        # Display results
        result_message = f"Time: {elapsed_time:.2f} seconds\nWPM: {wpm:.2f}\nAccuracy: {accuracy:.2f}%"
        self.result_label.config(text=result_message)

        # Save results in history
        self.history.append({
            "text": self.sample_text,
            "time": elapsed_time,
            "wpm": wpm,
            "accuracy": accuracy
        })

        # Reset start button
        self.start_button.config(text="Start", command=self.start_test)
        self.start_time = None

    def show_history(self):
        # Create a new window for history
        history_window = tk.Toplevel(self.root)
        history_window.title("Typing History")
        history_window.geometry("600x400")
        history_window.config(bg="#f0f0f0")

        # Display history
        if not self.history:
            tk.Label(history_window, text="No history available.", font=("Arial", 14), bg="#f0f0f0").pack(pady=20)
        else:
            for index, entry in enumerate(self.history, start=1):
                history_text = (
                    f"Test {index}:\n"
                    f"Sample Text: {entry['text']}\n"
                    f"Time: {entry['time']:.2f} seconds\n"
                    f"WPM: {entry['wpm']:.2f}\n"
                    f"Accuracy: {entry['accuracy']:.2f}%\n"
                    f"{'-' * 40}"
                )
                tk.Label(history_window, text=history_text, font=("Arial", 12), bg="#f0f0f0", justify="left", anchor="w", wraplength=580).pack(pady=5)

# Main application
root = tk.Tk()
app = TypingSpeedTestApp(root)
root.mainloop()
