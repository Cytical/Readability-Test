#created by ezraguiao 5/20/20
from tkinter import *
from tkinter import filedialog
import time

window = Tk()
window.title("Readability Test")
window.resizable(False, False)
window.iconbitmap("C:/Windows/book.ico")
text_input = Text(window, borderwidth = 4, cursor = "spraycan")
text_input.grid(columnspan = 8, rowspan = 8)

def UploadAction(event=None):
    window.filename = filedialog.askopenfilename(initialdir= "C:/Users/win10/Downloads",title = "Select a Text File", filetypes=(("txt files","*.txt"), ("all files","*.*")))
    f = open(window.filename, "r")
    opened_file = f.read()
    text_input.delete('1.0', END)
    text_input.insert("1.0" , opened_file)

def convert_input():
    #timer
    start = time.time()
    value = text_input.get("1.0", "end-1c")

    word_count = 1 # to make up the last word which was not counted
    sentence_count = 0
    letter_count = 0

    for letter in value:
        if letter.isspace():
            word_count += 1
        elif letter == "." or letter == "?" or letter == "!":
            sentence_count += 1
        else:
            letter_count += 1
    #The Coleman-Liau index
    index = 0.0588 * (letter_count*100//word_count) - 0.296 * (sentence_count*100//word_count) - 15.8
    estimate = int(round(index,2))
    if estimate < 1:
        level = "Preschool"
    elif estimate > 16:
        level ="Collegiate"
    else:
        level = f"Grade {estimate}"

    wordfreq = {}
    sorter = []

    freq_counter = value.split()
    #print(freq_counter)
    lag = False
    if lag:
        for word in freq_counter:
            wordfreq[word] = wordfreq.get(word, 0) + 1
            for key, value in wordfreq.items():
                sorter.append((value, key))
    
    end = time.time()
    time_elapsed = round((end-start),3)

    word_display = Message(window, bd = 0, text = f"Words: {word_count}", width =64)
    word_display.grid(columnspan = 1, rowspan = 1, column = 1, row = 8,sticky = W)

    word_display = Message(window, bd = 0, text = f"Sentence: {sentence_count}", width =84)
    word_display.grid(columnspan = 1, rowspan = 1, column = 3, row = 8,sticky = W)

    word_display = Message(window, bd = 0, text = f"Characters: {letter_count}", width =84)
    word_display.grid(columnspan = 1, rowspan = 1, column = 5 ,row = 8,sticky = W)

    word_display = Message(window, bd = 0, text = f"{level}", width =64)
    word_display.grid(columnspan = 1, rowspan = 1, column = 7, row = 8,sticky = E)

    word_display = Message(window, bd = 0, text = f"Processing Time: {time_elapsed}s", width =64)
    word_display.grid(columnspan = 2, rowspan = 1, column = 2, row = 9,sticky = W)
    
readButton = Button(window, height=1, width=20, text="Read", activeforeground="Red",bg = "Gray",command= convert_input)
readButton.grid(columnspan = 1, rowspan = 1, row = 8, sticky = W)       

button = Button(window, text='Open',width = 20, command=UploadAction)
button.grid(column = 0, rowspan = 2, sticky = W)

window.mainloop()
