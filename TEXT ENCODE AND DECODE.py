import tkinter as tk
from tkinter import *
import base64

def encode_message():
    message = entry_message.get()
    message_bytes = message.encode("ascii")
    base64_bytes = base64.b64encode(message_bytes)
    encoded_message = base64_bytes.decode("ascii")
    entry_encoded.delete(0, END)
    entry_encoded.insert(0, encoded_message)

def decode_message():
    encoded_message = entry_encoded.get()
    encoded_bytes = encoded_message.encode("ascii")
    message_bytes = base64.b64decode(encoded_bytes)
    decoded_message = message_bytes.decode("ascii")
    entry_decoded.delete(0, END)
    entry_decoded.insert(0, decoded_message)

N = Tk()
N.geometry("1500x1500")
N.config(bg="blue")

frame = Frame(width=400, height=400, bg="green")
frame.place(x=650, y=250)

title = Label(N, text="MESSAGE ENCODE AND DECODE", font=("times", 30, "italic"))
title.place(x=500, y=70)

lbl = Label(N, text="developed by NANTHA KUMAR(developer)", font=("times", 10, "italic"))
lbl.place(x=1100, y=650)

btn_encode = Button(N, text="ENCODE", font=("times"), command=encode_message)
btn_encode.place(x=750, y=300)

btn_decode = Button(N, text="DECODE", font=("times"), command=decode_message)
btn_decode.place(x=750, y=400)

entry_message = Entry(N)
entry_message.place(x=500, y=300)

entry_encoded = Entry(N)
entry_encoded.place(x=500, y=400)

entry_decoded = Entry(N)
entry_decoded.place(x=500, y=500)

N.mainloop()
