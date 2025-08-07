
import tkinter as tk
from tkinter import ttk
import json
import threading
from playsound import playsound
import random

kitten_state = {"energy": 100, "affection": 50, "emotion": "happy", "brain": {}}
emotions = ["happy", "curious", "sleepy", "excited"]

def meow():
    threading.Thread(target=lambda: playsound("meow.mp3")).start()

def save_brain():
    with open("kitten_brain.json", "w") as f:
        json.dump(kitten_state["brain"], f)

def load_brain():
    try:
        with open("kitten_brain.json", "r") as f:
            kitten_state["brain"] = json.load(f)
    except FileNotFoundError:
        kitten_state["brain"] = {}

def update_emotion():
    kitten_state["emotion"] = random.choice(emotions)
    emotion_label.config(text="Emotion: " + kitten_state["emotion"])

def draw_kitten():
    canvas.delete("all")
    canvas.create_oval(50, 50, 150, 150, fill="gray")  # head
    canvas.create_oval(80, 120, 120, 160, fill="gray")  # body
    canvas.create_line(130, 140, 180, 130, fill="gray", width=4)  # tail
    canvas.create_oval(70, 70, 80, 80, fill="white")  # left eye
    canvas.create_oval(120, 70, 130, 80, fill="white")  # right eye
    canvas.create_text(100, 180, text="=^.^=", font=("Arial", 16))

def change_breed(event):
    breed = breed_var.get()
    kitten_state["brain"]["breed"] = breed
    breed_label.config(text="Breed: " + breed)
    update_emotion()
    draw_kitten()

root = tk.Tk()
root.title("AI Kitten Bot")

breed_var = tk.StringVar()
breed_menu = ttk.Combobox(root, textvariable=breed_var, values=["Tuxedo", "Siamese", "Tabby", "Tuxedo (real tux)"])
breed_menu.bind("<<ComboboxSelected>>", change_breed)
breed_menu.set("Choose a breed")
breed_menu.pack()

breed_label = tk.Label(root, text="Breed: None")
breed_label.pack()

emotion_label = tk.Label(root, text="Emotion: happy")
emotion_label.pack()

meow_button = tk.Button(root, text="Meow", command=meow)
meow_button.pack()

canvas = tk.Canvas(root, width=300, height=200, bg="white")
canvas.pack()

save_button = tk.Button(root, text="Save Brain", command=save_brain)
save_button.pack()

load_button = tk.Button(root, text="Load Brain", command=load_brain)
load_button.pack()

draw_kitten()
root.mainloop()
