import tkinter as tk
import re

class OneLine(tk.Tk):
    """
    Simple app to remove line breaks
    and make just single line of text from input.
    """
    def __init__(self): # Tkinter main window
        tk.Tk.__init__(self)
        # window title
        self.title('One Line')
        # field for input text
        self.entry = tk.Text(self, height=10, width=100)
        self.entry.pack()
        # input of character or string to replace end of the line
        self.replacement = tk.Label(self, text="Replacement for the end of the line:", width=100)
        self.replacement.pack()
        self.replacement = tk.Entry(self, width=20)
        self.replacement.pack()
        # removing multiple spaces
        self.multiSpace = tk.BooleanVar()
        self.multiSpace.set(False)
        self.choices = tk.Checkbutton(self, text="Remove multiple spaces", variable=self.multiSpace)
        self.choices.pack()
        # exec button
        self.button = tk.Button(self, text="NO END", command=self.noEnd)
        self.button.pack()
        # output field
        self.result = tk.Text(self, height=5, width=100)
        self.result.pack()
        # button to quit the app
        self.button = tk.Button(self, text="exit", padx=20, command=self.destroy)
        self.button.pack(anchor="e")
        

    def noEnd(self): # function to remove line breaks
        # obtaining replacement string
        replaceCharacter = self.replacement.get()
        # reading the input with avoiding the last linebreak
        inputText = self.entry.get('1.0','end-1c')
        # checking if multiple spaces are enabled
        removeSpaces = self.multiSpace.get()
        # removing multiple consecutive linebreaks on empty lines
        inputText = re.sub("\n+", '\n', inputText)
        # removing linebreak and tabulator at the beginning of string, if any and avoiding only linebreak input
        if len(inputText) > 0:
            while inputText[0] == "\n" or inputText[0] == "\t":
                inputText = inputText[1:]
                if len(inputText) < 1:
                    break
        # removing linebreak and tabulator at the end of string, if any and avoiding only linebreak input
        if len(inputText) > 0:
            while inputText[-1] == "\n" or inputText[-1] == "\t":
                inputText = inputText[:-1]
                if len(inputText) < 1:
                    break
        # replacing tabulators with single spaces
        inputText = re.sub("\t", ' ', inputText)
        # replacing line breaks
        outputText = inputText.replace("\n", replaceCharacter)
        # removing multiple spaces if enabled
        if removeSpaces == True:
            outputText = re.sub(' +', ' ', outputText)
        # emptying output field before writing the result
        self.result.delete('1.0', 'end-1c')
        # writing output
        self.result.insert('1.0', outputText)

#initializing the main loop
app = OneLine()
app.mainloop()
