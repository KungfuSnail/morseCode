
from tkinter import *
from tkinter import filedialog
from decoder_encoder import *
import os
from pathlib import Path

class FilePath():
    def __init__(self):
        self.path = None

    def changePath(self, Newpath):
        holder = Path(Newpath)
        if holder.is_file():
            self.path = Path(Newpath)


def addFile(master, filePathClass):
    fileName = filedialog.askopenfilename(initialdir="/", title="Select a File",
                                          filetypes=(("text","*.txt"),("all files", "*.*")))
    filenameLabel = Label(master, text=fileName)
    filenameLabel.pack(side=TOP)

    filePathClass.changePath(fileName)

def decode(master, decode_file_path):

    decoded_message = decode_message(decode_file_path)
    label3 = Label(master, text=decoded_message)
    label3.pack(side=BOTTOM)

def encode(master, encode_file_path, given_secret_message, resultingFileName):
    try:
        encodeMessage(given_secret_message, encode_file_path, resultingFileName)
        label_done = Label(master, text="Success! Try decoding the same file to verify your code")
        label_done.pack(side=BOTTOM)
    except:
        if (encode_file_path == None):
            label_done = Label(master, text="Fail! choose a text file to be encoded.")
            label_done.pack(side=BOTTOM)
        else:
            label_done = Label(master, text="Fail! maybe the message is too long to fit, try shortening it.")
            label_done.pack(side=BOTTOM)


root = Tk()

decodeFile = FilePath()
encodeFile = FilePath()

canvas = Canvas(height=500, width=700)
canvas.pack()

window1 = Frame(root, bg="#444444")
window1.place(relheight=1, relwidth=.5)

# used decodeFile in addFile function because we are in the decode window.
btnGetFile = Button(window1, text="Find file", padx=10, pady=10, command=lambda: addFile(window1, decodeFile))
btnGetFile.pack(side=TOP)

btnDecode = Button(window1, text="Decode", padx=15, pady=15, command=lambda: decode(window1, decodeFile.path))
btnDecode.pack(side=BOTTOM)

# Window two
window2 = Frame(root)
window2.place(relheight=1, relwidth=0.5, relx=.5)

btnGetFile2 = Button(window2, text="Find file", padx=10, pady=10, bg="#606060", fg="white",
                     command=lambda : addFile(window2, encodeFile))
btnGetFile2.pack(side=TOP)


#Default name would be the name of the file we're encoding
spaceLabel = Label(window2, text=" ", pady=3)
spaceLabel.pack(side=TOP)

enterFileName_label = Label(window2, text="Enter the export file name:", pady=10, padx=10)
enterFileName_label.pack(side=TOP)
enterFileName = Entry(window2, width=10, borderwidth=8)
enterFileName.pack(side=TOP)

whatToEncode_label = Label(window2, text="The message to be encoded:", pady=10, padx=10)
whatToEncode_label.pack(side=TOP)
whatToEncode = Entry(window2, width=10, borderwidth=8)
whatToEncode.pack(side=TOP)


btnEncode = Button(window2, text="Encode", padx=15, pady=15, bg="#606060", fg="white",
                   command=lambda : encode(window2, encodeFile.path,whatToEncode.get(), enterFileName.get()))
btnEncode.pack(side=BOTTOM)



root.mainloop()
