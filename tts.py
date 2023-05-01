from gtts import gTTS
from playsound import playsound
import tkinter as tk

# create display window
root = tk.Tk()
root.geometry("500x300")
root.configure(bg='#264653')
root.title("JOHN SWANSON | CYBER 100 | TEXT TO SPEECH")

# Writing Labels for window
text_label = tk.Label(root, text="Enter text to convert into speech:", font=("Arial", 14), bg='#264653', fg='#e9c46a')
text_label.pack(pady=(20, 0))
# create text input
text_input = tk.Entry(root, font=("Arial", 14), width=40)
text_input.pack(pady=(0, 20))

title_label = tk.Label(text="Make John Swanson Speak!!", font=("Arial", 20), bg='#264653', fg='#2a9d8f', width='40')
title_label.pack(pady=(0, 20), side='top')


# define function to convert text to speech and save as mp3
def convert_to_mp3():
    # get text from user input
    text = text_input.get()

    # convert text to speech
    tts = gTTS(text)
    tts.save("speech.mp3")

    # play speech using playsound
    playsound("speech.mp3")


# create button to convert texto speech and save as mp3
mp3_button = tk.Button(root, text="Save as MP3", font=("Arial", 14), bg='#e9c46a', fg='#001219', command=convert_to_mp3)
mp3_button.pack()


# make function to convert text to speech and save as wav
def convert_to_wav():
    # get text from user input
    text = text_input.get()

    # convert text to speech
    tts = gTTS(text)
    tts.save("speech.wav")

    # play speech sound using playsound
    playsound("speech.wav")


# create button to convert text to speech and save as wav
wav_button = tk.Button(root, text="Save as WAV", font=("Arial", 14), bg='#2a9d8f', fg='#001219', command=convert_to_wav)
wav_button.pack(pady=(10, 10))


# define function to convert text to speech and save as ogg
def convert_to_ogg():
    # get text from user input
    text = text_input.get()

    # convert text to speech
    tts = gTTS(text)
    tts.save("speech.ogg")

    # play speech sound using playsound
    playsound("speech.ogg")


# create button to convert text to speech and save as ogg
ogg_button = tk.Button(root, text="Save as OGG", font=("Arial", 14), bg='#e76f51', fg='#001219', command=convert_to_ogg)
ogg_button.pack(pady=(0, 20))


# exit the app
def exit_tts():
    root.destroy()


# create exit button
exit_button = tk.Button(root, text="Exit", font=("Arial", 14), bg='#2a9d8f', fg='#001219', command=exit_tts)
exit_button.pack(pady=(0, 0))

# run GUI
root.mainloop()
