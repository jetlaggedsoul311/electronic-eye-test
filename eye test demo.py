import tkinter as tk
from tkinter import font
import random

# Setting up the tkinter window
root = tk.Tk()
root.title("Electronic Eye Test")
root.geometry("500x500")

# Making the letter display random
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

cnt = 0
font_size = 25
left_eye_done = False

# Setting up the text widget
text_widget = tk.Text(root, font=('Courier', font_size), height=1, width=2)
text_widget.pack(pady=20)

# Function to handle the "Yes" response
def on_yes():
    global cnt, font_size

    cnt += 1

    if cnt == 2:
        font_size = 12
    elif cnt == 3:
        font_size = 8
    elif cnt == 4:
        font_size = 6
    elif cnt == 5:
        font_size = 5
    elif cnt == 6:
        font_size = 4
    elif cnt == 7:
        font_size = 3

    text_widget.config(font=('Courier', font_size))
    text_widget.delete(1.0, tk.END)
    text_widget.insert(tk.END, random.choice(letters))

    if cnt == 7:
        yes_button.config(state=tk.DISABLED)  # Disable the yes button after the last size

# Function to handle the "No" response
def on_no():
    global left_eye_done

    left_eye_done = True
    if cnt == 1:
        result_label.config(text='You have failed the test, your degree is 20/200')
    elif cnt == 2:
        result_label.config(text='You have failed the test, your degree is 20/100')
    elif cnt == 3:
        result_label.config(text='You have failed the test, your degree is 20/70')
    elif cnt == 4:
        result_label.config(text='You have failed the test, your degree is 20/50')
    elif cnt == 5:
        result_label.config(text='You have failed the test, your degree is 20/40')
    elif cnt == 6:
        result_label.config(text='You have failed the test, your degree is 20/30')
    elif cnt == 7:
        result_label.config(text='You have failed the test, your degree is 20/25')

    yes_button.config(state=tk.DISABLED)  # Disable the yes button
    no_button.config(state=tk.DISABLED)   # Disable the no button

# Yes and No buttons for user input
yes_button = tk.Button(root, text="Yes", command=on_yes)
yes_button.pack(side=tk.LEFT, padx=20, pady=20)

no_button = tk.Button(root, text="No", command=on_no)
no_button.pack(side=tk.RIGHT, padx=20, pady=20)

# Label to display the result after the test
result_label = tk.Label(root, text="")
result_label.pack(pady=20)

# Initial display of a random letter
text_widget.insert(tk.END, random.choice(letters))

root.mainloop()