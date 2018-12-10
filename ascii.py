# Simple ASCII Encoder and Decoder Program with GUI
# By Prince Kelvin Onyenanu

import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox as mb
import string

root = tk.Tk()
root.title("ASCII Encoder|Decoder")
root.resizable(0,0)

ToEncode_sv = tk.StringVar()
ToDecode_sv = tk.StringVar()

def onEncode(*event):
    myList = []
    Letters = ToEncode_sv.get()
    for ch in Letters:
        myList.append(ord(ch))
        
    mb.showerror("Encoder",  "Here's your message in ASCII encoded form:\n" + str(myList),)

def onDecode(*event):
    split_by_n= lambda x, n: [x[i:i+n] for i in range(0, len(x), n)]
    Ascii = ToDecode_sv.get()
    message = ""
    Ascii = split_by_n(Ascii,2)
    for numStr in Ascii:
        asciiNum = eval(numStr) # convert digit string to a number
        message = message + chr(asciiNum)  # append character to message

    mb.showerror("Decoder",  "Here's your ASCII code in text form:\n" + message,)

def onReset(*event):
    ToEncode_sv.set("")
    ToDecode_sv.set("")
       
    
#Add GUI
Encodelabel = tk.Label(root, text="Text to Encode: ").grid(row=0, column=0, padx=10, pady=10, sticky='w')
Encodeentry = tk.Entry(root, textvariable=ToEncode_sv).grid(row=0, column=1, padx=10,pady=1-0)
EncodeButton = tk.Button(root, text="Encode", command=onEncode).grid(row=2, column=0, padx=10, pady=10, sticky='w')

Decodelabel = tk.Label(root, text="Text to Decode: ").grid(row=1, column=0, padx=10, pady=10, sticky='w')
Decodeentry = tk.Entry(root, textvariable=ToDecode_sv).grid(row=1, column=1, padx=10,pady=1-0)
DecodeButton = tk.Button(root, text="Decode", command=onDecode).grid(row=2, column=1, padx=10, pady=10, sticky='w')

ResetButton = tk.Button(root, text="Reset", command=onReset).grid(row=2, column=2, padx=10, pady=10, sticky='w')


root.mainloop()
    

